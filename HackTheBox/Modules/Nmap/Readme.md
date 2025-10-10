# Nmap — README.md (Comprehensive, Practical & Technical)

> A detailed guide to **Nmap** (Network Mapper): installation, common scan types, key options, NSE (Nmap Scripting Engine), output formats, performance tuning, interpretation of results, workflow for reconnaissance, limitations, and ethics. Intended for network engineers, pentesters and learners.

---

## Table of Contents

- [What is Nmap](#what-is-nmap)  
- [Installation](#installation)  
- [Privileges & Behavioral Differences](#privileges--behavioral-differences)  
- [Common Scan Types (what they do & when to use)](#common-scan-types-what-they-do--when-to-use)  
- [Essential Options & Flags (concise reference)](#essential-options--flags-concise-reference)  
- [Nmap Scripting Engine (NSE)](#nmap-scripting-engine-nse)  
- [Output Formats & Integration](#output-formats--integration)  
- [Performance Tuning & Stealth Considerations](#performance-tuning--stealth-considerations)  
- [Interpreting Results — pitfalls & caveats](#interpreting-results--pitfalls--caveats)  
- [Limitations & False Positives/Negatives](#limitations--false-positivesnegatives)  
- [Best Practices, Security & Legal Notice](#best-practices-security--legal-notice)   
- [Further Reading & Resources](#further-reading--resources)

---

## What is Nmap
Nmap (Network Mapper) is an open-source tool for network discovery and security auditing. It can:
- discover hosts and services on a network,
- identify open TCP/UDP ports,
- perform service/version detection,
- guess operating systems (OS fingerprinting),
- run scripts that detect vulnerabilities, configuration issues, or gather information (NSE).

Nmap is used in network inventory, monitoring, security audits and penetration testing.

---

## Installation

### Debian / Ubuntu
```bash
sudo apt update
sudo apt install nmap
```
### MacOs

```bash
brew install nmap
```
### Windows

Download the official installer from https://nmap.org and run; nmap.exe is available in PowerShell/CMD.

- From source :
```bash
git clone https://github.com/nmap/nmap.git
cd nmap
./configure
make
sudo make install
```

## Privileges & Behavioral Differences

- Raw socket scans (e.g., TCP SYN -sS) require root/administrator privileges to craft packets.
- Connect scan (-sT) uses the OS TCP stack and does not require special privileges, but is noisier and slower.
- OS detection (-O) and some advanced features may require additional privileges and live network access.
- Running with elevated privileges often yields more accurate and faster results.




## Common Scan Types (what they do & when to use)

- -sS SYN scan (half-open): fast, stealthier than full connect; requires root. Good default for TCP port scanning.
- -sT TCP connect scan: uses OS connect; no raw sockets needed. Use when non-root.
- -sU UDP scan: UDP is slower and stateful; requires many probes and retries. Use when UDP services are relevant.
- -sN, -sF, -sX TCP NULL/FIN/Xmas: stealth/evade simplistic IDS; behavior depends on target TCP/IP stack.
- -sA ACK scan: used to map firewall rules and determine if ports are filtered.
- -sn (formerly -sP) Ping scan: discovers live hosts without port scanning.
- -sV Service/version detection: probes open ports to guess service and version.
- -O OS detection: fingerprint the remote OS (needs sufficient open/closed ports and privileges).
- -Pn No ping: treats all hosts as up; useful when ICMP is blocked.
- -p Port selection: list or range of ports to scan (e.g., -p 22,80,443 or -p 1-65535).
- -p- shorthand to scan all 65535 TCP ports.
- -sL List scan: DNS resolution and list of targets, no probes.




## Essential Options & Flags (concise reference)

- -p <ports>    ports to scan.
- -T<0-5>   timing template (0 slowest/stealthiest → 5 fastest).
- -sS / -sT / -sU — SYN / Connect / UDP scans.
- -sV   version detection.
- -O OS   fingerprinting.
- -A   aggressive: -sV -O --script=default combined (convenient but noisy).
- -Pn   skip host discovery; treat hosts as up.
- --open   show only open ports in output.
- -oN <file>   normal output.
- -oX <file>   XML output (machine-readable).
- -oG <file>   grepable output (legacy).
- -oA <base>   save in all three formats (normal, XML, grepable).
- --script <script-name|category>   run NSE scripts (e.g., --script http-enum or --script vuln).
- --script-args key=value   pass args to scripts.
- --top-ports <N>   scan top N most common ports.
- --version-intensity <0-9>   tune   -sV   aggressiveness.
- --reason  display the reason a port is reported in the output.
- --traceroute   run traceroute after scan.


## Nmap Scripting Engine (NSE)

NSE allows automated scripting across many tasks: discovery, vulnerability detection, brute forcing, info-gathering, exploitation helpers, malware detection, and more. Scripts are grouped into categories:

auth, brute, default, discovery, exploit, external, intrusive, malware, safe, vuln, etc.


## Output Formats & Integration

### Human-readable:

- -oN output.txt — normal format.

### Machine-readable:

- -oX output.xml  XML, useful for parsers and other tools.
- -oG output.gnmap  grepable (deprecated but still used).

- -oA base   writes .nmap, .xml, .gnmap.

### JSON:

- Newer Nmap builds/aux tools (or ndiff/xml2json) can convert XML to JSON for downstream processing.

### Integration:

- Use XML outputs to feed vulnerability scanners, SIEMs, or custom tooling.
- Combine with masscan for large-range discovery (masscan discovers, nmap verifies).


## Performance Tuning & Stealth Considerations

### Timing templates (-T0..-T5)

- -T0 paranoid — maximum stealth (very slow).
- -T1 sneaky — evade IDS with long delays.
- -T2 polite — reduce load on network.
- -T3 normal — default.
- -T4 aggressive — faster, assumes reliable network and low IDS sensitivity.
- -T5 insane — fastest and loudest; use only in controlled networks.

### Parallelism / Host/Port tuning

- --min-rate, --max-rate (if supported)  control probes per second.
- --min-parallelism / --max-parallelism  control parallel probe threads.

### Fragmentation & evasions

- -f   fragment packets (some old IDS evasion).
- --data-length   append random data to probes.
- --source-port   set source port to try and bypass ACLs (not reliable).

### Stealth vs Accuracy trade-offs

- Lower timing/retries increases stealth but increases false negatives.
- Aggressive scans risk detection and generate noisy logs.


## Interpreting Results pitfalls & caveats

### Open vs Filtered vs Closed:

- open: service responded / port appears accessible.
- closed: port reachable but no service listening.
- filtered: probes blocked/dropped by firewall/IPS — further probing needed.

### Service detection errors:

- False version matches may happen; manual banner grabbing and validation are recommended.

### OS detection accuracy:

- Requires multiple probes and characteristic responses; firewalls, NAT, virtualization and packet normalization can distort results.

### NSE script outputs:

- Scripts can generate false positives. Corroborate with multiple methods and manual checks.

## Limitations & False Positives/Negatives

- UDP scanning is inherently unreliable (no handshake); many UDP services silently drop unknown packets.
- Firewalls / IPS / WAF may block or alter responses, yielding false negatives or incorrect OS/service guesses.
- Rate-limiting on hosts may throttle responses — slower scans required.
- IPv6 scanning differs; ensure Nmap version and flags support desired IPv6 behavior.

## Best Practices, Security & Legal Notice

- Always get explicit written permission before scanning systems you do not own.
- Use --script vuln and aggressive NSE only in authorized testbeds.
- Keep output artifacts secure; they may contain sensitive data (service banners, version info).
- Use isolated environments (VPNs, bastion hosts, containers) when possible.
- Maintain an audit trail (scan logs, timestamps, purpose, authorization).

## Further Reading & Resources

- Official: https://nmap.org docs, reference, download, NSE script docs.
- man nmap / nmap --help   built-in reference.
- Nmap book: Nmap Network Scanning (Gordon "Fyodor" Lyon)  deep dive into internals and advanced usage.

## Closing Notes

Nmap is a powerful and flexible tool; mastery requires practice, reading script code for nuance, and understanding network behaviors (firewalls, NAT, rate-limiting). Use responsibly and always with authorization.