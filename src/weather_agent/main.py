from agent import Weather_Agent

def main():
    agent = Weather_Agent()
    
    while True:
        user_question = input("You..! ")
        if user_question.lower() == 'exit':
            break
        agent_response = agent.run(user_question)
        print("Agent: ",agent_response)
if __name__ == "__main__":
    main()
 
 