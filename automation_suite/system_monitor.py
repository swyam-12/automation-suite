import psutil
import time

print("System Monitor Started...\n")

with open("system_report.txt", "w") as file:
    file.write("SYSTEM MONITOR REPORT\n")
    file.write("=" * 30 + "\n")

    for _ in range(10):  # collect 10 readings
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        line = f"CPU: {cpu}% | Memory: {memory}%\n"
        print(line.strip())
        file.write(line)

        # Alerts
        if cpu > 80:
            alert = "⚠️ High CPU Usage Alert!\n"
            print(alert.strip())
            file.write(alert)

        if memory > 80:
            alert = "⚠️ High Memory Usage Alert!\n"
            print(alert.strip())
            file.write(alert)

        file.write("-" * 30 + "\n")

        time.sleep(2)

print("\nReport saved as system_report.txt")