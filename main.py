from pyswip import Prolog
import time
import json


def prolog_query(query_string):
    prolog = Prolog()
    prolog.consult("knowledge.pl")
    results = []
    for res in prolog.query(query_string):
        results.append(res)

    return results


def ask_question(query_string):
    answers = prolog_query(query_string)
    return answers


def make_json(data):
    json_str = ""
    for c in data:
        if c == "'":
            json_str += '"'
            continue
        json_str += c
    return json_str


def say_answers(prefix, suffix, question_i, answers_i):
    for ansi in answers_i:
        ansi = make_json(str(ansi))
        obj = json.loads(str(ansi))
        print(obj[question_i])
        text = prefix + " " + obj[question_i] + " " + suffix
        print(">>>> ", text)


print(
    "Hi, I'm here to tell you about UFC - campus jardins de anita university. \
                what do you want to know about ufc university?"
)
flg = True
while flg:
    # Q/A
    print("\n\n")
    asked_question = str(input("O que você tem em mente?: ")).lower()

    if (
        "nome da universidade" in asked_question
        or "universidade" in asked_question
    ):
        # Q: qual é o nome da universidade?
        question = "UniversityName"
        query = "name(" + question + ")."
        answers = ask_question(query)
        say_answers("O nome da universidade ", "", question, answers)

    elif (
        "introduction" in asked_question
        or "about ju" in asked_question
        or "about ufc university" in asked_question
    ):
        # Q: what is ufc university?
        question = "Introduction"
        query = "introduction('ufc - campus jardins de anita', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "history of ju" in asked_question
        or "history of ufc university" in asked_question
    ):
        # Q: history of ufc university.
        question = "History"
        query = "history('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers("Brief history: ", "", question, answers)

    elif (
        "location of ufc university" in asked_question
        or "situated" in asked_question
    ):
        # Q: onde fica a ufc?
        question = "Loction"
        query = "location('ufc campus itapaje', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif "area of ufc university" in asked_question:
        # Q: onde fica a ufc?
        question = "Area"
        query = "area('ufc', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "total area of ufc university is about ", "", question, answers
        )

    elif (
        "current" in asked_question
        or "present" in asked_question
        or "now" in asked_question
    ) and ("vice chancellor" in asked_question or "vc" in asked_question):
        # Q: qual é o atual diretor da ufc?
        question = "Vice_chancellor"
        query = "vice_chancellor('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "The current vice chancellor of ufc university is ",
            "",
            question,
            answers,
        )

    elif (
        "number of faculties" in asked_question
        or "how many faculties" in asked_question
        and asked_question.find("faculty of") == -1
    ):
        # Q how many faculties are in jahangirnagr university
        question = "Number_of_faculties"
        query = "number_of_faculties('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "faculties in ufc university", question, answers
        )

    elif (
        "number of departments" in asked_question
        or "how many departments" in asked_question
    ):
        # Q how many departments are in jahangirnagr university
        question = "Number_of_departments"
        query = "number_of_departments('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "departments in ufc university", question, answers
        )

    elif (
        "number of institutes" in asked_question
        or "how many institutes" in asked_question
    ):
        # Q how many institutes are in jahangirnagr university
        question = "Number_of_institutes"
        query = "number_of_institutes('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "institutes in ufc university", question, answers
        )

    elif (
        "names of the faculties" in asked_question
        or "what are the faculties" in asked_question
    ):
        # Q what are the faculties in ufc university
        question = "Facultiy"
        query = "faculties('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "there are 3 faculties are in ufc university, they are, ",
            "",
            question,
            answers,
        )

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
    ) and "under the faculty of" in asked_question:
        # Q what are the names departments in faculty of X?
        faculties = [
            "curso de segurança da informação",
            "curso de ciências de dados",
            "curso de análise e desenvolvimento de sistemas",
            
        ]
        id = -1
        for i in range(6):
            if faculties[i] in asked_question:
                id = i
                break
        if id != -1:
            print(faculties[id])
            question = "Departments"
            query = (
                "departments_under_faculty('ufc university', '"
                + faculties[id]
                + "',"
                + question
                + ")."
            )
            answers = ask_question(query)
            print(">>>>> ", "the departments under " + faculties[id] + " are, ")
            say_answers("", "", question, answers)

        else:
            print(">>>>> ", "sorry, there is no such faculty.")

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
    ):
        # Q what are the departments in ufc university
        question = "Departments"
        query = "departments('ufc university', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "there are 34 departments in ufc university, they are, ",
            "",
            question,
            answers,
        )

    elif (
        "about department of cse" in asked_question
        or "about cse" in asked_question
        or "about computer science and engineering" in asked_question
        or "about department of computer science and engineering" in asked_question
    ):
        # Q what you know about dept of CSE ufc university
        question = "Cse"
        query = (
            "about_department_of_computer_science_and_engineering(\
                'ufc university', "
            + question
            + ")."
        )
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "chairman of department of cse" in asked_question
        or "chairman of cse" in asked_question
        or "chairman of computer science and engineering" in asked_question
        or "chairman of department of computer science and engineering"
        in asked_question
    ):
        # Q who is the chairman of dept of CSE JU?
        question = "Chairman"
        query = (
            "chairman_of_cse('department of computer science and engineering', "
            + question
            + ")."
        )
        answers = ask_question(query)
        say_answers(
            "",
            "is the chairman of department of computer science and engineering",
            question,
            answers,
        )

    elif (
        "who are the developers of this project" in asked_question
        or "who developed" in asked_question
        or "who created" in asked_question
    ):
        # Q who developed this program?
        question = "Developers"
        query = "developers(" + question + ")."
        answers = ask_question(query)
        print(
            ">>>>> ",
            "This project is supervised by professor doctor mohammad shorif uddin.",
        )
        say_answers("the developers are", "", question, answers)

    elif "stop" in asked_question or "exit" in asked_question:
        print(">>>>> ", "thank you, hope you have enjoyed the session")
        break

    else:
        if asked_question != "-----------------":
            confirmation = str(
                input(
                    "Sorry, this is out of my knowledge. whould you like to continue? "
                )
            ).lower()
            
            if "no" in confirmation or "nope" in confirmation or "stop" in confirmation:
                print(">>>>> ", "thank you, hope you have enjoyed the session")
                break
            else:
                continue

        time.sleep(2)
