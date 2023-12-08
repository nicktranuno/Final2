import tkinter as tk


class TriviaView:
    """ View class for the Trivia GUI. """
    def __init__(self, root, controller: 'TriviaController'):
        """
        Initializes the TriviaView.

        :param root: The root Tkinter window.
        :param controller: The associated controller.

        :attributes:
            root: The root Tkinter window.
            controller: The associated controller.
            question_label: Displays the current question.
            answer_buttons: List of answer buttons.
            score_label: Label to display the current score.
            fail_message: Window displayed to indicate fail.
        """
        self.root = root
        self.controller = controller

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(2):
            button_frame = tk.Frame(root)
            button_frame.pack(pady=5)

            for j in range(2):
                index = i * 2 + j
                button = tk.Button(button_frame, text="", command=lambda idx=index, i=i, j=j: self.controller.handle_answer_click(idx), width=15, height=3)
                button.pack(side=tk.LEFT, padx=5)
                self.answer_buttons.append(button)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack(pady=10)

        self.fail_message = tk.Toplevel(root)
        self.fail_message.withdraw()
        self.fail_message.protocol("WM_DELETE_WINDOW", self.controller.retry_question)

        fail_label = tk.Label(self.fail_message, text="Incorrect answer! Retry or close the GUI.")
        fail_label.pack(pady=10)

        retry_button = tk.Button(self.fail_message, text="Retry", command=self.controller.retry_question)
        retry_button.pack(side=tk.LEFT, padx=10)

        close_button = tk.Button(self.fail_message, text="Close", command=self.root.destroy)
        close_button.pack(side=tk.RIGHT, padx=10)

    def update_view(self) -> None:
        """ Updates the view with the current question and answers. """
        current_question = self.controller.get_current_question()
        self.question_label.config(text=current_question['question'])

        for i, button in enumerate(self.answer_buttons):
            button.config(text=current_question['answers'][i])

        self.score_label.config(text=f"Score: {self.controller._score}")

    def show_game_over_message(self) -> None:
        """ Shows the game over message with final score. """
        tk.messagebox.showinfo("Game Over", f"Your final score is: {self.controller.score}")
        self.root.destroy()

    def show_fail_message(self) -> None:
        """ Shows the fails message when there is an incorrect answer. """
        self.fail_message.deiconify()

    def hide_fail_message(self) -> None:
        """ Hides the fail message. """
        self.fail_message.withdraw()