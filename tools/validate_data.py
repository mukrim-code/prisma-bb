"""Semakan data.json sebelum diterbitkan. Dijalankan automatik oleh GitHub Actions
setiap kali data.json diubah, dan boleh dijalankan sendiri:  python3 tools/validate_data.py"""
import json, re, sys, unicodedata

DT = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-\d{2}$")

def nk(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def fail(msg):
    print("RALAT:", msg)
    sys.exit(1)

try:
    d = json.load(open("data.json", encoding="utf-8"))
except Exception as e:
    fail(f"data.json bukan JSON yang sah ({e})")

if d.get("app") != "rekod-program-jawhar":
    fail("data.json bukan daripada app Rekod Program JAWHAR")
P = d.get("programs")
if not isinstance(P, list) or not P:
    fail("senarai 'programs' kosong atau tidak sah")
if len(P) > 5000:
    fail("terlalu banyak program (had 5000)")

seen = {}
for i, p in enumerate(P, 1):
    t = f"program #{i}"
    if not isinstance(p, dict):
        fail(f"{t}: bukan objek")
    if not isinstance(p.get("nama"), str) or not p["nama"].strip():
        fail(f"{t}: nama kosong")
    if len(p["nama"]) > 300:
        fail(f"{t}: nama terlalu panjang")
    if not DT.match(str(p.get("tarikh", ""))):
        fail(f"{t} ({p['nama'][:40]}): tarikh mula tidak sah")
    if p.get("akhir"):
        if not DT.match(str(p["akhir"])) or p["akhir"] < p["tarikh"]:
            fail(f"{t} ({p['nama'][:40]}): tarikh akhir tidak sah")
    if p.get("kategori") not in ("Dianjurkan", "Dihadiri"):
        fail(f"{t}: kategori tidak sah")
    pe = p.get("peserta")
    if pe not in ("", None) and not (isinstance(pe, (int, float)) and 0 <= pe <= 100000):
        fail(f"{t}: bilangan peserta tidak sah")
    for k in ("kp", "tkp"):
        if p.get(k) not in ("", None, "hadir", "wakil", "tidak"):
            fail(f"{t}: nilai {k} tidak sah")
    key = (nk(p["nama"]), p["tarikh"])
    if key in seen:
        fail(f"rekod pendua: program #{seen[key]} dan #{i} ({p['nama'][:50]}, {p['tarikh']})")
    seen[key] = i

print(f"OK: {len(P)} program disemak, tiada pendua tepat, format sah.")
