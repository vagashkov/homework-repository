"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):

    def decorated_init(self):
        """ increment instances counter every time
        an object is created"""
        cls.__instance_counter += 1

    @classmethod
    def get_created_instances(cls):
        """ instance counter checker (works for the whole class)"""
        return cls.__instance_counter

    def reset_instances_counter(self):
        """ before reset instance counter we have to remember
        its value to return it to caller"""
        old_counter = cls.__instance_counter
        cls.__instance_counter = 0
        return old_counter

    # setting instance counter initial value
    cls.__instance_counter = 0
    # redefine object constructor
    cls.__init__ = decorated_init
    # append two additional methons
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    # and return decorated class
    return cls


@instances_counter
class User:
    pass
