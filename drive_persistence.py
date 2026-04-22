from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
# Carga las credenciales o inicia el flujo
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Si no hay credenciales, usa el archivo que acabamos de crear
    gauth.LocalWebserverAuth(launch_browser=False)
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

print("\n[+] ARCH-PROT-2025: Persistencia activa en ZTE V30")
print("[+] Sincronización con Drive establecida.")
