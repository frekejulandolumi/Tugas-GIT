todo_list = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def show_tasks():
    if not todo_list:
        print("Belum ada tugas.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Masukkan tugas baru: ")
    todo_list.append(task)
    print("Tugas ditambahkan!")

def delete_task():
    show_tasks()
    if todo_list:
        index = int(input("Pilih nomor tugas yang ingin dihapus: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"Tugas '{removed}' dihapus!")
        else:
            print("Nomor tidak valid.")

while True:
    show_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")
# End of file todolist.py