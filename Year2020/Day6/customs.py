import string

questions = list(string.ascii_letters[0:26])


def unique_answers(answers: [str]) -> int:
    joined_answers = "".join(answers).replace("\n", "")
    return len("".join(set(joined_answers)))


def load_data(filename: str):
    with open(filename) as file:
        answers = file.read().split('\n\n')
    return answers


def count_any_answers(answers: [str]):
    return sum(unique_answers(group) for group in answers)


def every_answers(group: [str]):
    answers = group.split('\n')
    counter = 0
    for question in questions:
        if _check_question_in_all_answers(answers, question):
            counter += 1

    return counter


def _check_question_in_all_answers(group, question):
    for answer in group:
        if question not in answer:
            return False
    return True


def count_every_answers(answers: [str]):
    return sum(every_answers(group) for group in answers)


def main():
    answers = load_data('input.txt')
    print(count_any_answers(answers))
    print(count_every_answers(answers))


if __name__ == '__main__':
    main()
