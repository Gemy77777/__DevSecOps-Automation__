import os
import re
import json
import shutil
import ipaddress
from collections import Counter
from datetime import datetime

class LogFilter:
    CRITICAL_WORDS = {
        'critical', 'error', 'fatal', 'failure', 
        'failed', 'warning', 'warn', 'exception'
    }
     
    def __init__(self, log_path):
        self.log_path = log_path.strip('"').strip("'")
        self.backup_dir = None
        self.output_file = None
    
    def filter_critical(self):
        if not os.path.exists(self.log_path):
            raise FileNotFoundError("Log file not found.")
        
        # Create backup directory
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.backup_dir = os.path.join(
            os.path.dirname(os.path.abspath(self.log_path)),
            f"Backup_{timestamp}"
        )
        os.makedirs(self.backup_dir, exist_ok=True)
        
        self.output_file = os.path.join(self.backup_dir, "filtered_errors.txt")
        count = 0
        
        with open(self.log_path, "r", encoding="utf-8") as f_in, \
             open(self.output_file, "w", encoding="utf-8") as f_out:
            
            for line in f_in:
                if any(word in line.lower() for word in self.CRITICAL_WORDS):
                    f_out.write(line)
                    count += 1
        
        print(f"[+] Found {count} critical lines.")
        return count
    
    def archive(self):
        """Create zip archive of backup directory."""
        if not self.backup_dir:
            return
        
        zip_path = shutil.make_archive(
            base_name=self.backup_dir,
            format="zip",
            root_dir=self.backup_dir
        )
        print(f"[+] Archive created: {zip_path}")
        return zip_path


class IPExtractor:
    """Extracts and validates IP addresses from log files."""
    
    IP_PATTERN = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    
    def __init__(self, file_path):
        self.file_path = file_path.strip('"').strip("'")
    
    def extract(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("File not found.")
        
        raw_ips = []
        with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                found = re.findall(self.IP_PATTERN, line)
                raw_ips.extend(found)
        
        return self._validate(raw_ips)
    
    def _validate(self, ips):
        valid = []
        for ip in ips:
            try:
                ipaddress.ip_address(ip)
                valid.append(ip)
            except ValueError:
                continue
        return valid


class IPAnalyzer:
    """Analyzes IP addresses: counts, types, and risk levels."""
    
    def __init__(self, ips):
        self.ips = ips
        self.counter = Counter(ips)
    
    def get_summary(self):
        return {
            "total_extracted": len(self.ips),
            "unique_ips": len(self.counter)
        }
    
    def classify_ip(self, ip):
        ip_obj = ipaddress.ip_address(ip)
        count = self.counter[ip]
        
        if ip_obj.is_private:
            return "Private", "Safe"
        elif ip_obj.is_loopback:
            return "Loopback", "Safe"
        else:
            if count > 100:
                return "Public", "HIGH RISK"
            elif count > 30:
                return "Public", "Warning"
            else:
                return "Public", "Normal"
    
    def get_detailed_results(self):
        results = []
        for ip, count in self.counter.most_common():
            ip_type, status = self.classify_ip(ip)
            results.append({
                "ip": ip,
                "type": ip_type,
                "count": count,
                "status": status
            })
        return results


class Report:
    """Handles report generation and output."""
    
    def __init__(self, data, output_dir=None):
        self.data = data
        self.output_dir = output_dir or os.getcwd()
    
    def display(self):
        print(f"\n[+] Total: {self.data['summary']['total_extracted']} | "
              f"Unique: {self.data['summary']['unique_ips']}\n")
        print(f"{'IP':<18} | {'Type':<10} | {'Count':<8} | Status")
        print("-" * 70)
        
        for item in self.data["ips"]:
            print(f"{item['ip']:<18} | {item['type']:<10} | "
                  f"{item['count']:<8} | {item['status']}")
    
    def save_json(self, filename="log_analysis_report.json"):
        full_path = os.path.join(self.output_dir, filename)
        with open(full_path, "w") as f:
            json.dump(self.data, f, indent=4)
        print(f"[+] Report saved to: {full_path}")


class LogAnalyzer:
    """Main orchestrator — runs everything."""
    
    def __init__(self, file_path):
        self.file_path = file_path.strip('"').strip("'")
        self.base_dir = os.path.dirname(os.path.abspath(self.file_path))
    
    def run(self):
        print("[+] Starting full log analysis...")
        
        # 1. Filter critical lines
        print("\n--- Phase 1: Critical Word Filter ---")
        log_filter = LogFilter(self.file_path)
        log_filter.filter_critical()
        log_filter.archive()
        
        # 2. Extract IPs
        print("\n--- Phase 2: IP Extraction ---")
        extractor = IPExtractor(self.file_path)
        valid_ips = extractor.extract()
        
        if not valid_ips:
            print("[-] No valid IPs found.")
            return
        
        # 3. Analyze IPs
        analyzer = IPAnalyzer(valid_ips)
        detailed = analyzer.get_detailed_results()
        summary = analyzer.get_summary()
        
        # 4. Generate report
        report_data = {
            "summary": summary,
            "ips": detailed
        }
        report = Report(report_data, output_dir=self.base_dir)
        report.display()
        report.save_json()
        
        print("\n[+] Analysis complete.")


if __name__ == "__main__":
    try:
        path = input("Enter the log file path: ")
        analyzer = LogAnalyzer(path)
        analyzer.run()
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except PermissionError:
        print("[-] Error: Permission denied.")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")