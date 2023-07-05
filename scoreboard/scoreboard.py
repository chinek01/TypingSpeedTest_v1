"""

Scoreboard

Portfolio: Typing Speed Test
#100DaysOfCode with Python
Day: 85
Date: 2023-07-05
Author: MC

Another version of this project. Previous wos so bad :)

"""

from tkinter.messagebox import showinfo


class scoreboard:

    def __init__(self):
        self._answers = []
        self._corr_answer = 0
        self._n_corr_answer = 0

    def reset_results(self):
        """
        Reset resultqs :)
        """
        self._answers.clear()
        self._corr_answer = 0
        self._n_corr_answer = 0

    def add_answer(self,
                   answer: bool):
        """
        Get answer from user
        :param answer:
        :return:
        """
        if answer is None:
            raise ValueError("Answer must be set!")

        if not isinstance(answer, bool):
            raise ValueError("Answer must by bool type value!")

        self._answers.append(answer)

    def get_answers(self):
        """
        :return: answers
        """
        return self._answers

    def result(self):
        """
        Calculate result form typing
        :return: correct words per min
        """

        # calculate correct answers
        for n in range(len(self._answers)):
            if self._answers[n] is True:
                self._corr_answer += 1
            else:
                self._n_corr_answer += 1

        return self._corr_answer


# some test
if __name__ == '__main__':
    x = scoreboard()
    x.add_answer(False)
    x.add_answer(False)
    x.add_answer(True)
    x.add_answer(False)
    x.add_answer(True)
    x.add_answer(True)
    x.add_answer(True)
    print(x.result())
