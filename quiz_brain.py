

class QuizBrain:
    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_ans = input(f"Q. {self.question_number}: {self.current_question.question} (True/False): ").capitalize()


    def still_more_question(self):
        self.still_question = len(self.question_list)
        if self.question_number < self.still_question:
            return True
        else:
            return False


    def is_correct(self):
        if self.user_ans == self.current_question.answer:
            self.score += 1
            print(f"You Got it Right👍🤩")
        else:
            print(f"You Got it Wrong 😫🥵")
            print(f"Correct Answer is: {self.current_question.answer}")
        print(f"Your Current Score Is: {self.score}/{self.question_number}")
        print("\n")































































# class Car:
#     def __init__(self, make, model,color, year):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year


# Car1 = Car("Toyota", "Camry", "Titanium Black", "2025")
# print(f"Car Model: {Car1.model}\nCar Maker: {Car1.make}")


# Car2 = Car("Mercedes Benz", "May back", "Silver", "2022")
# print(f"Car Model: {Car2.model}\nCar Maker: {Car2.make}")


# class User:
#     def __init__(self, username, userid):
#         self.username = username
#         self.id = userid
#         self.following = 0
#         self.followers = 0

#     def follow(self, users):
#         users.followers += 1
#         self.following += 1

        

# user_1 = User("Adebayo", "001")
# user_2 = User("Raymond", "002")
# user_3 = User("Gabriel", "003")

# user_1.follow(user_2)
# user_3.follow(user_1)
# user_2.follow(user_1)

# print(f"{user_1.username} Following: {user_1.following}, Followers: {user_1.followers}")
# print(f"{user_2.username} Following: {user_2.following}, Followers: {user_2.followers}")
# print(f"{user_3.username} Following: {user_3.following}, Followers: {user_3.followers}")


