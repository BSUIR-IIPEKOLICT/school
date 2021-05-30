class Subject:
    def __init__(self, name, id = None) -> None:
        self.name = name
        self.id = id

    def subject_list(par) -> None:
        for index, subject in enumerate(par[2]):
            print('#{0} - {1}.'.format(index + 1, subject.name))