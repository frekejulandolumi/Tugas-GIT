def tambah(a, b):
    """Menambahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangi dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

def kalkulator():
    """Fungsi utama kalkulator"""
    print("=" * 40)
    print("KALKULATOR SEDERHANA".center(40))
    print("=" * 40)
    
    while True:
        print("\nPilih operasi:")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (×)")
        print("4. Bagi (÷)")
        print("5. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1-5): ")
        
        if pilihan == '5':
            print("\nTerima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan in ['1', '2', '3', '4']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    hasil = tambah(angka1, angka2)
                    print(f"\n{angka1} + {angka2} = {hasil}")
                elif pilihan == '2':
                    hasil = kurang(angka1, angka2)
                    print(f"\n{angka1} - {angka2} = {hasil}")
                elif pilihan == '3':
                    hasil = kali(angka1, angka2)
                    print(f"\n{angka1} × {angka2} = {hasil}")
                elif pilihan == '4':
                    hasil = bagi(angka1, angka2)
                    print(f"\n{angka1} ÷ {angka2} = {hasil}")
                    
            except ValueError:
                print("\nError: Masukkan angka yang valid!")
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-5.")

# Run
if __name__ == "__main__":
    kalkulator()
