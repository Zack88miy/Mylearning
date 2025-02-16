def load_tasks(filename="tasks.txt"):
    try:
        with open(filename,"r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename,"w") as file:
        file.write("\n".join(tasks))

def display_tasks(tasks):
    if not tasks:
        print("現在のタスクはないです")
    else:
        print('\n現在のタスク:')
        for i, task in enumerate(tasks,1):
            print(f'{i}.{task}')

def main():
    print('=== ToDo List App ===')
    tasks = load_tasks()

    while True:
        print("\nメニュー:")
        print("1. タスク追加")
        print("2. タスク表示")
        print("3. タスク削除")
        print("4. アプリ終了")

        choice = input("Pleese Choice (1-4): ")

        match choice:
            case "1":
                new_task = input('新しいタスクを入力: ')
                tasks.append(new_task)
                save_tasks(tasks)
                print('タスクを追加しました')
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
                    print('番号を入力してください')
            case "4":
                print('アプリを終了します')
                break
            case _:
                print('無効な入力です')
            
                    
if __name__ == '__main__':
    main()
    