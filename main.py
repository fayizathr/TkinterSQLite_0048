

        # Warna teks hasil prediksi
        warna = {
            "Rendah": "green",
            "Waspada": "blue",
            "Sedang": "orange",
            "Tinggi": "red",
            "Sangat Tinggi": "darkred"
        }
        hasil_label.config(text="Hasil: " + hasil, fg=warna[hasil])
        
        messagebox.showinfo("Sukses", "Data berhasil disimpan dan diprediksi!")

    except ValueError:
        messagebox.showerror("Error", "Periksa kembali semua input! Pastikan semua kolom terisi dan usia, gula darah, serta BMI berupa angka.")


