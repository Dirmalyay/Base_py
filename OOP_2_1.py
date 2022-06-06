# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том, что редактирование документов недоступно
# для бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.

class Editor:
    def __init__(self, document):
        self.document = document

    def __repr__(self):
        return f"{self.document}"

    def view_document(self):
        print(f"{self.document}")

    def edit_document(self):
        print("Document editing is not available for the free version.")


class ProEditor(Editor):
    right_key = "123"

    def __init__(self, key, document):
        self.key = key
        super().__init__(document)


    def edit_document(self, key):
        self.key = str(input("Enter the key: "))
        if self.key == self.right_key:
            self_class_object = ProEditor(key, self.document)
            self_class_object.view_document()
            print("You can change the text")
        else:
            parent_class_object = super()
            parent_class_object.view_document()
            print("Wrong key. Only reading.")

print("Объект первого класса:")
doc_1 = Editor("text text text")
doc_1.view_document()
doc_1.edit_document()
print()
print("Объект второго класса:")
doc_2 = ProEditor("123", "some text")
doc_2.view_document()
doc_2.edit_document("123")






