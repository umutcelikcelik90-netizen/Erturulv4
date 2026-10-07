import subprocess
import os

print("--- Erturulv4 Gradle & V4 Yükleyici ---")
token = input("Token'ını buraya yaz (harfler görünecektir): ").strip()

if not token:
    print("Token boş olamaz!")
    exit(1)

if os.path.exists(".git"):
    subprocess.run(["rm", "-rf", ".git"])

subprocess.run(["git", "init"])
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "config", "--global", "user.name", "Ertuğrul"])
subprocess.run(["git", "config", "--global", "user.email", "ertugrul@users.noreply.github.com"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Gradle ve V4 Dosyalari Eklendi"])

remote_url = f"https://umutcelikcelik90-netizen:{token}@github.com/umutcelikcelik90-netizen/Erturulv4.git"
subprocess.run(["git", "remote", "add", "origin", remote_url])

result = subprocess.run(["git", "push", "-u", "origin", "main", "--force"])

if result.returncode == 0:
    print("\nSuccessfully")
    print("Kanka bak GitHub geldi, Gradle dosyaları eklendi.")
else:
    print("\nHata oluştu. Token yetkilerini kontrol et.")
