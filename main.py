

        # Simpan ke Database SQLite
        cursor.execute("""
        INSERT INTO pasien 
        (nama_pasien, usia, gula_darah, bmi, riwayat_ortu, hasil_prediksi)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nama, usia, gula, bmi, riwayat, hasil))
        conn.commit()

       