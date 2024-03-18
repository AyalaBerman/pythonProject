from Task8 import Task8
class Task8Main:
    task = Task8()
    task.check_email_correct("UsersEmail.txt")
    print(task.get_gmail_emails("UsersEmail.txt"))
    task.check_username_in_email("UsersEmail.txt", "UsersName.txt")

