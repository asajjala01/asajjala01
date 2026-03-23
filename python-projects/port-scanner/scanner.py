import socket
import concurrent.futures
from datetime import datetime

def scan_port(target, port):

    # Validate port range before attempting connection
    if not isinstance(port, int) or port < 0 or port > 65535:
        return None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            return port
        return None
    except (socket.error, TypeError, OSError):
        return None


def grab_banner(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
        sock.close()
        return banner if banner else None
    except:
        return None


def run_scan(target, start_port, end_port, threads=100):
    open_ports = []
    port_range = range(start_port, end_port + 1)
    print(f"\n[*] Scanning {target} — ports {start_port} to {end_port}")
    print(f"[*] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in port_range}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                open_ports.append(result)
                print(f"  [+] Port {result} OPEN")
    return sorted(open_ports)

def main():
    parser = argparse.ArgumentParser(
        description="Python Port Scanner — for authorized use only"
    )
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Thread count (default: 100)")
    parser.add_argument("-b", "--banner", action="store_true", help="Enable banner grabbing")
    
    args = parser.parse_args()
    
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {args.target}")
        sys.exit(1)
    
    open_ports = run_scan(target_ip, args.start, args.end, args.threads)
    
    if args.banner and open_ports:
        print("\n[*] Grabbing banners...")
        for port in open_ports:
            banner = grab_banner(target_ip, port)
            if banner:
                print(f"  Port {port}: {banner[:80]}")
    
    print(f"\n[*] Scan complete. {len(open_ports)} open port(s) found.")
    print(f"[*] Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()

