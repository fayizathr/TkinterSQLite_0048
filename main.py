

nama_entry = tk.Entry(root, width=25)
usia_entry = tk.Entry(root, width=25)
gula_entry = tk.Entry(root, width=25)
bmi_entry = tk.Entry(root, width=25)

for teks, entry in [
    ("Nama Pasien", nama_entry),
    ("Usia", usia_entry),
    ("Gula Darah (mg/dL)", gula_entry),
    ("BMI", bmi_entry)
]:
    tk.Label(root, text=teks).pack(anchor="w", padx=45)
    entry.pack(pady=2)

tk.Label(root, text="Riwayat Diabetes Orang Tua").pack(anchor="w", padx=45)
ortu_box = ttk.Combobox(root, values=["Ya", "Tidak"], state="readonly", width=22)
ortu_box.set("Tidak")  # <-- Perbaikan: Mengisi nilai default agar tidak kosong
ortu_box.pack(pady=2)

