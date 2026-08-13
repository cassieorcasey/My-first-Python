import random

# variabel
secret_number = random.randint(1, 100)
ronde = 0
max_ronde = 9

# Header
print("=" * 30)
print("       TEBAK ANGKA")
print("=" * 30)
print("Komputer telah memilih angka dari 1 - 100")
print(f"Anda punya {max_ronde} kesempatan untuk menebak!")
print("-" * 30)

# Game loop
while ronde < max_ronde:
    try:
        print(f"\nKesempatan ke-{ronde + 1} dari {max_ronde}")
        tebakan = int(input("Masukkan tebakan Anda (1-100): "))
        
        # validasi input
        if tebakan < 1 or tebakan > 100:
            print(" Tolong masukkan angka antara 1-100!")
            continue
            
        ronde += 1
        
        # System Cek Tebakan
        if tebakan < secret_number:
            print(" Tebakan Anda terlalu KECIL!")
            print(f"   Sisa kesempatan: {max_ronde - ronde}")
        elif tebakan > secret_number:
            print(" Tebakan Anda terlalu BESAR!")
            print(f"   Sisa kesempatan: {max_ronde - ronde}")
        else:
            print(" SELAMAT! Anda berhasil menebak angka yang benar!")
            print(f" Angka yang benar adalah: {secret_number}")
            print(f" Anda menebak dengan benar dalam {ronde} kali percobaan!")
            break
            
    except ValueError:
        print(" Input tidak valid! Masukkan angka saja.")
        continue

# System Gagal Menembak
else:
    print("\n" + "=" * 30)
    print(" GAME OVER!")
    print(f"Angka yang benar adalah: {secret_number}")
    print("   Coba lagi lain kali!")
    print("=" * 30)
