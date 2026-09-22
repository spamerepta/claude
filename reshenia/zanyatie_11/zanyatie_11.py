import json
import tkinter as tk
import urllib.request

FIELDS = ["company", "created_at", "email", "id", "name", "url"]


def get_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "python"})
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def get_owner_info(repository):
    repository = repository.strip().replace("https://github.com/", "").strip("/")
    if "/" in repository:
        repo_data = get_json("https://api.github.com/repos/" + repository)
        login = repo_data["owner"]["login"]
    else:
        login = repository
    user_data = get_json("https://api.github.com/users/" + login)
    return {field: user_data.get(field) for field in FIELDS}


def save_info(info, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(info, file, indent=2, ensure_ascii=False)


def on_click():
    repository = entry.get()
    if not repository.strip():
        result.config(text="Введите имя репозитория")
        return
    try:
        info = get_owner_info(repository)
    except Exception as error:
        result.config(text="Ошибка: " + str(error))
        return
    file_name = repository.strip().strip("/").replace("/", "_") + ".json"
    save_info(info, file_name)
    result.config(text=json.dumps(info, indent=2, ensure_ascii=False) + "\n\nСохранено в " + file_name)


window = tk.Tk()
window.title("GitHub")
window.geometry("520x360")
tk.Label(window, text="Имя репозитория (например kubernetes/kubernetes):").pack(pady=5)
entry = tk.Entry(window, width=50)
entry.pack(pady=5)
tk.Button(window, text="Получить", command=on_click).pack(pady=5)
result = tk.Label(window, text="", justify="left", font=("Courier", 10))
result.pack(pady=5)
window.mainloop()
