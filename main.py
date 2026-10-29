

        if not nama or not riwayat:
            raise ValueError

        if usia < 1 or usia > 120 or gula <= 0 or bmi <= 0:
            messagebox.showerror("Error", "Data tidak valid! Masukkan angka yang sesuai.")
            return

      