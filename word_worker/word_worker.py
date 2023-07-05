"""

Class word_worker

Get list of words from any txt file (one row one word) and selection without repetition

Portfolio: Typing Speed Test
#100DaysOfCode with Python
Day: 85
Date: 2023-07-03
Author: MC

"""

from random import choice


class word_worker:

    def __init__(self):
        self.words_list = []
        self.file_path = None
        self.selected_words = []

    def set_file_path(self,
                      path: str):
        """
        Path to database txt file (*.txt)
        :param path: path to file
        """

        if path is None:
            raise ValueError('The Path must be set!')

        self.file_path = path

    def get_words_list(self,
                       path=None):
        """
        Read and create list of words from txt file - lowercase
        :param path: path to file
        :return: words list
        """

        if path is not None:
            self.set_file_path(path)

        try:
            with open(self.file_path, 'r') as f:
                lines = f.readlines()

                for line in lines:
                    self.words_list.append(line.replace('\n', ''))

        except FileNotFoundError:
            return f"File not found!"

        except FileExistsError:
            return f"File not exist!"

        return self.words_list

    def choice_word(self):
        """
        Function returns the selected word from readed list.
        :return: Some word :)
        """
        if len(self.words_list) == 0:
            raise ValueError("The words list is empty!")

        ok_flag = False
        my_choice = None

        while not ok_flag:
            my_choice = choice(self.words_list).__str__().lower()
            ok_flag = self._check_choice(my_choice)

        return my_choice

    def _check_choice(self,
                      word):
        """
        Check if the word is in word selected list
        :param word: word to check
        :return: True - word isn't on The List, False - word is on The List
        """
        if word is None:
            raise ValueError("Word to check myst be set.")

        result = True

        for item in self.selected_words:
            if word == item:
                result = False
                break

        return result


# some test
if __name__ == '__main__':
    x = word_worker()
    x.set_file_path('../word_db.txt')
    # print(x.get_words_list())
    x.get_words_list()
    print(x.choice_word())
    print(x.choice_word())
    print(x.choice_word())
    print(x.choice_word())
