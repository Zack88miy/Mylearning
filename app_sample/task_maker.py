import os
from datetime import datetime, timedelta

TASKS_FILE = "tasks.txt"
COMPLETED_FILE = "completed_tasks.txt"
BACKUP_FILE = "tasks_backup.txt"
LOG_FILE = "log.txt"

# ログを記録する
def log_action(action):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")

# タスクを読み込む
def load_tasks(filename=TASKS_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

# タスクを保存する
def save_tasks(tasks, filename=TASKS_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(tasks) + "\n")
    log_action(f"タスク保存: {filename}")

# バックアップ作成
def backup_tasks():
    tasks = load_tasks()
    save_tasks(tasks, BACKUP_FILE)
    print("バックアップを作成しました!")
    log_action("バックアップ作成")

# タスクを表示
def display_tasks(tasks):
    if not tasks:
        print("現在のタスクはありません")
    else:
        print("\n現在のタスク一覧:")
        print("=" * 50)
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("=" * 50)

# タスクを追加
def add_task(tasks):
    name = input("新しいタスクを入力: ")
    tag = input("タグを入力: ")

    # 締切日
    while True:
        due_date = input("締切日 (YYYY-MM-DD) または Enter: ")
        if due_date == "":
            due_date = "未設定"
            break
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("日付の形式が間違っています。")

    # 優先度
    while True:
        priority = input("優先度 (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("正しい値を入力してください!")

    task_entry = f"{name} | {tag} | {due_date} | {priority}"
    tasks.append(task_entry)
    save_tasks(tasks)
    print("タスクを追加しました!")
    log_action(f"タスク追加: {name}")

# タスクの削除
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("削除するタスク番号を入力: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"タスク '{removed_task}' を削除しました!")
            log_action(f"タスク削除: {removed_task}")
        else:
            print("無効な番号です")
    except ValueError:
        print("数字を入力してください!")

# タスク完了処理
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("完了したタスクの番号: ")) - 1
        if 0 <= task_num < len(tasks):
            completed_task = tasks.pop(task_num)
            save_tasks(tasks)

            completed_tasks = load_tasks(COMPLETED_FILE)
            completed_tasks.append(completed_task)
            save_tasks(completed_tasks, COMPLETED_FILE)

            print(f"タスク '{completed_task}' を完了しました!")
            log_action(f"タスク完了: {completed_task}")
        else:
            print("無効な番号です")
    except ValueError:
        print("数字を入力してください!")

# タスクの並び替え
def sort_tasks(tasks):
    choice = input("ソート方法を選択 (1: 優先度, 2: 締切日): ")
    if choice == "1":
        tasks.sort(key=lambda x: x.split("|")[-1], reverse=True)
    elif choice == "2":
        tasks.sort(key=lambda x: x.split("|")[2])
    save_tasks(tasks)
    print("タスクを並び替えました!")
    log_action("タスク並び替え")

# キーワード検索
def search_task(tasks):
    keyword = input("検索キーワードを入力: ")
    results = [task for task in tasks if keyword in task]
    if results:
        print("検索結果:")
        for task in results:
            print(task)
    else:
        print("該当するタスクはありません")

# メニュー
def main():
    print("=== ToDoリストアプリ ===")

    while True:
        tasks = load_tasks()

        print("\nメニュー:")
        print("1. タスク追加")
        print("2. タスク表示")
        print("3. タスク削除")
        print("4. タスク完了")
        print("5. タスク並び替え")
        print("6. キーワード検索")
        print("7. バックアップ作成")
        print("8. アプリ終了")

        choice = input("選択 (1-8): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            search_task(tasks)
        elif choice == "7":
            backup_tasks()
        elif choice == "8":
            print("アプリを終了します")
            break
        else:
            print("無効な入力です")

if __name__ == "__main__":
    main()