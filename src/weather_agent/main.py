from agent import Weather_Agent
from error import Error
import time 
import traceback

def main():
    agent = Weather_Agent()
    error = Error()

    printAnimate("Welcome to ai bird.....")
    while True:
        user_question = input("\nYou..!")
        if user_question.lower() == 'exit':
            printAnimate("Thank You! See you again...!")
            break
        try:
            agent_response = agent.run(user_question)
            printAnimate(agent_response)
        except Exception as e:
            error.log(e)
            
def printAnimate(data):
    if type(data)!=str:
        print(data)
        return 
    for char in data:
        print(char, end="", flush=True)
        time.sleep(0.01)
 

if __name__ == "__main__":
    main()
 
 