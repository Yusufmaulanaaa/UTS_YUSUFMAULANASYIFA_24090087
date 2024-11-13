
def hitung_bmi(berat_badan, tinggi_badan):
    # Menghitung nilai BMI
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

def main():
    berat_badan = float(input("Masukkan Berat Badan (Kg): "))
    tinggi_badan = float(input("Masukkan Tinggi Badan (M): "))
    
    bmi = hitung_bmi(berat_badan, tinggi_badan)
    
    kategori = kategori_bmi(bmi)
    
    print(f"\nBerat Badan: {berat_badan} Kg")
    print(f"Tinggi Badan: {tinggi_badan} M")
    print(f"Nilai BMI Anda: {bmi:.2f}")
    print(f"Kategori BMI: {kategori}")

if __name__ == "__main__":
    main()