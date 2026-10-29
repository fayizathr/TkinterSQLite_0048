

tk.Button(root, text="Simpan & Prediksi", command=prediksi, bg="#d0f0c0", width=20).pack(pady=10)
tk.Button(root, text="Lihat Data", command=lihat_data, width=20).pack()

hasil_label = tk.Label(root, text="Hasil: -", font=("Arial", 12, "bold"))
hasil_label.pack(pady=15)

root.mainloop()

# Menutup koneksi database ketika aplikasi ditutup
conn.close()