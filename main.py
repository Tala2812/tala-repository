class Task:
    def __init__(self, description, term, status=False):

        self.description = description
        self.term = term
        self.status = status

    def mark_as_done(self):

        self.status = True

    def __str__(self):

        status_str = "Выполнено" if self.status else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.term}, Статус: {status_str}"


class TaskManager:
    def __init__(self):

        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, term):
        """Добавляю новую задачу в список задач."""
        task = Task(description, term)
        self.tasks.append(task)

    def mark_task_as_done(self, description):
        """
        Отмечает задачу как выполненную по её описанию и перемещает её в список выполненных задач.
        Если задача с данным описанием не найдена, ничего не делает.
        """
        for task in self.tasks:
            if task.description == description and not task.status:
                task.mark_as_done()
                self.completed_tasks.append(task)
                self.tasks.remove(task)
                break

    def get_pending_tasks(self):

        return [str(task) for task in self.tasks]

    def get_completed_tasks(self):

        return [str(task) for task in self.completed_tasks]

    def __str__(self):
        """Возвращает строковое представление всех задач."""
        return "\n".join(str(task) for task in self.tasks)

task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2024-11-15")
task_manager.add_task("Помыть полы", "2024-11-15")
task_manager.add_task("Сделать домашнее задание", "2024-11-15")
print("Текущие задачи:")
print(task_manager)

task_manager.mark_task_as_done("Купить продукты")
task_manager.mark_task_as_done("Сделать домашнее задание")
print("\nТекущие (не выполненные) задачи:")
print("\n".join(task_manager.get_pending_tasks()))

print("\nВыполненные задачи:")
print("\n".join(task_manager.get_completed_tasks()))

