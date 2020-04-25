from survey import AnonymousSurvey
"""定义一个问题，并创建一个表示调查的AnonymousSurver对象"""
question = "What language did you first learn to sperk?"
my_surver = AnonymousSurvey(question)
# 显示问题并存储答案
my_surver.show_question()
print("Enter 'q' at any time to quit,\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_surver.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the surver!")
my_surver.show_results()