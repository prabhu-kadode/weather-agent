from agent import Weather_Agent

def main():
    agent = Weather_Agent()
    
    while True:
        user_question = input("What...!")
        if user_question.lower() == 'exit':
            break
        agent.run(user_question)
if __name__ == "__main__":
    main()
 
 