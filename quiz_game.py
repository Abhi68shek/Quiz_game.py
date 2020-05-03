import requests
import json
import html
endgames = ''
while endgames != "quits":
    url = 'https://opentdb.com/api.php?amount=1'
    r =  requests.get(url)
    if(r.status_code != 200):
        print('The request is invalid')
    else:
        valid_answer = False
        question_json = json.loads(r.text)
        category1 = html.unescape(question_json['results'][0]['category'])
        question1 = html.unescape(question_json['results'][0]['question'])
        answers = html.unescape(question_json['results'][0]['incorrect_answers'])
        correct_answer1 = html.unescape(question_json['results'][0]['correct_answer'])
        answers.append(correct_answer1)
        print("\nquestion:  ", html.unescape(question1))
        print("\nThe options are : ")
        #The code for displaying the answers(options)
        i = 0 
        for answer in answers:
            i = i + 1
            print(i,answer)
        print('############################################################################')
        while valid_answer == False:
            user_input = (input("write the correct answer "))
            try:
                user_input = int(user_input)
                if user_input > len(answers) or user_input <= 0:
                    print("INVALID Answer")
                else:
                    valid_answer = True
            except:
                print('\nOnly the integer value allowed')
        print('############################################################################')
        user_answer = answers[(user_input)-1] #getting the user answer from the list
        #comparing the user answer with the correct answer
        if(user_answer == correct_answer1):
            print('Congratulations the answer is correct', html.unescape(correct_answer1))
        else:
            print('sorry,The correct answer is ',html.unescape(correct_answer1))
        endgames = input('\nPlease press enter to continue or write quits to quit ').lower()
print("Thanks for playing")