


def lihat_data():
    # Membuat jendela baru (Toplevel)
    jendela_data = tk.Toplevel(root)
    jendela_data.title("Data Riwayat Pasien")
    jendela_data.geometry("680x350")

    # Membuat Treeview (Tabel)
    columns = ("ID", "Nama", "Usia", "Gula Darah", "BMI", "Riwayat", "Hasil")
    tree = ttk.Treeview(jendela_data, columns=columns, show="headings")

    # Mengatur judul dan lebar kolom
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=90, anchor="center")
    
    tree.column("Nama", width=120, anchor="w")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Mengambil seluruh data dari database pasien
    cursor.execute("SELECT * FROM pasien")
    rows = cursor.fetchall()

    # Memasukkan data ke dalam tabel GUI
    for row in rows:
        tree.insert("", "end", values=row)


