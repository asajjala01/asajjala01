import socket
import concurrent.futures
import argparse
import sys
from datetime import datetime

def scan_port(target, port):
    """
    Attempts a TCP connection to a single port.
    Returns the port number if open, None if closed/filtered.
    """
    try:
        # AF_INET = IPv4, SOCK_STREAM = TCP connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Timeout prevents hanging on filtered ports
        sock.settimeout(1)
        
        # connect_ex returns 0 on success (port open), error code otherwise
        result = sock.connect_ex((target, port))
        sock.close()
        
        if result == 0:
            return port
        return None
        
    except socket.error:
        return None

def grab_banner(target, port):
    """
    Attempts to grab the service banner from an open port.
    Banners often reveal software name and version — critical for vuln assessment.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target, port))
        
        # Some services send a banner immediately on connect
        # Others need a prompt — we send a generic HTTP-style request
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        
        banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
        sock.close()
        return banner if banner else None
        
    except:
        return None

  def run_scan(target, start_port, end_port, threads=100):
    """
    Runs the full scan across a port range using a thread pool.
    Returns a sorted list of open ports.
    """
    open_ports = []
    port_range = range(start_port, end_port + 1)
    
    print(f"\n[*] Scanning {target} — ports {start_port} to {end_port}")
    print(f"[*] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # ThreadPoolExecutor manages a pool of worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        # Map each port to a future (a pending result)
        futures = {executor.submit(scan_port, target, port): port for port in port_range}
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                open_ports.append(result)
                print(f"  [+] Port {result} OPEN")
    
    return sorted(open_ports)
