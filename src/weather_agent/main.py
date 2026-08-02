from agent import Weather_Agent
import time 

def main():
    agent = Weather_Agent()
    
    while True:
        user_question = input("You..!")
        if user_question.lower() == 'exit':
            break
        agent_response = agent.run(user_question)
        printAnimate(agent_response)
def printAnimate(data):
    if type(data)!=str:
        print(data)
        return 
    for char in data:
        print(char, end="", flush=True)
        time.sleep(0.01)
 

if __name__ == "__main__":
    main()
 
 