from datetime import datetime,timedelta

#タスクを読み込む
def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

#タスクを保存する
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename,"w",encoding='utf-8') as file:
        file.write("\n".join(tasks) + '\n')

#タスクを表示する
def display_tasks(tasks):
    if not tasks:
        print("現在のタスクはありません")
    else:
        print('\n現在のタスク:')
        for i, task in enumerate(tasks,start=1):
            print(f'{i}.{task}')

#タスクを追加する
def add_tasks(tasks):
    new_task = input('新しいタスクを入力: ')
    tag = input('タグを入力 (ex. work study): ')
    # タスクとタグを保存
    task_entry = f"{new_task} | {tag}"  
    tasks.append(task_entry)
    save_tasks(tasks)
    print('タスクを追加しました')

#タグ検索
def search_by_tag(tasks,tag):
    found = [task for task in tasks if f"| {tag}" in task]
    if found:
        print(f"Tag '{tag}' のタスク:")
        for i, task in enumerate(found, 1):
            print(f"{i}. {task}")
    else:
        print(f"Tag '{tag}' に一致するタスクはありません。")

#締め切りの報告(検討中)
#登録するデータ形式を変更する予定
#strptime():文字列を日付形式に変更
def check_due_tasks(tasks):
    today = datetime.today().date()
    for task in tasks:
        parts = task.split("|")
        if len(parts) > 1:
            try:
                due_date = datetime.strptime(parts[1],"%Y-%m-%d").date()
                if due_date <= today + timedelta(days=1):
                    print(f'締め切り間近: {parts[0]} (締め切り: {parts[1]})')
            except ValueError:
                pass

def main():
    print('=== ToDo List App ===')
    
    while True:
        #タスク読み込みとメニューの表示
        tasks = load_tasks()
        print("\nメニュー:")
        print("1. タスク追加")
        print("2. タスク表示")
        print("3. タスク削除")
        print("4. タスク検索")
        print("5. アプリ終了")

        choice = input("Pleese Choice (1-5): ")

        match choice:
            case "1":
                tasks = add_tasks(tasks)
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    task_num = int(input('削除するタスク番号を入力'))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num-1)
                        save_tasks(tasks)
                        print(f"タスク '{removed_task}'を削除")
                    else:
                        print("無効です")
                except ValueError:
                    print('番号を入力してください : ')
            case "4":
                tag = input('検索するタグを入力してください')
                search_by_tag(tasks,tag)
            case "5":
                print('アプリを終了します')
                break
            case _:
                print('無効な入力です')
            
                    
if __name__ == '__main__':
    main()
    