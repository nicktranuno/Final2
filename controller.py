import tkinter as tk
from view import TriviaView
from questions import questions
import random


class TriviaController:
    """Controller class for the Trivia game."""

    def __init__(self, root: tk.Tk) -> None:
        """
        Initializes the TriviaController.

        Parameters:
            master (tk.Tk): The root Tkinter window.
        """
        self._root = root
        self._questions = questions
        self._current_question_index = 0
        self._score = 0

        # Shuffle the list of questions
        random.shuffle(self._questions)

        self._view = TriviaView(root, self)

        self.update_view()

    def get_current_question(self) -> dict:
        """
        Gets the current trivia question.

        Returns:
            dict: The current trivia question.
        """
        try:
            return self._questions[self._current_question_index]
        except IndexError:
            print("Error: No questions available or index out of range.")
            return {}

    def update_view(self) -> None:
        """Updates the view with the current question and answers."""
        self._view.update_view()

    def handle_answer_click(self, selected_index: int) -> None:
        """
        Handles a user's answer click.

        Parameters:
            selected_index (int): The index of the selected answer.
        """
        correct_answer = self.get_current_question()['correct_answer']
        if selected_index == correct_answer:
            self._score += 1
            self._current_question_index += 1

            if self._current_question_index < len(self._questions):
                self.update_view()
            else:
                self._view.show_game_over_message()
        else:
            self._view.show_fail_message()

    def retry_question(self) -> None:
        """Resets the score and shuffles questions for a new game."""
        self._score = 0
        self._current_question_index = 0
        random.shuffle(self._questions)

        self._view.hide_fail_message()
        self.update_view()