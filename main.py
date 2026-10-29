

        # Logika Prediksi Risiko Diabetes
        if gula >= 200:
            hasil = "Sangat Tinggi" if bmi >= 30 or riwayat == "Ya" else "Tinggi"
        elif gula >= 140:
            hasil = "Tinggi" if bmi >= 30 and riwayat == "Ya" else "Sedang"
        elif bmi >= 30:
            hasil = "Sedang" if riwayat == "Ya" else "Waspada"
        elif riwayat == "Ya":
            hasil = "Waspada"
        else:
            hasil = "Rendah"

       