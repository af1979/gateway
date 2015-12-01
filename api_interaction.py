#Python 3.4.3
import requests
import json

def sanitize_input(message, desired_type, error_message):
    while True:
        try:
            data = determine_input_handling(message, desired_type)
        except (ValueError, KeyError):
            print(error_message)
            continue
        else:
            return data

def determine_input_handling(message, desired_type):
    if desired_type == int:
        return int(input(message))
    if desired_type == bool:
        return { 'y': True, 'n': False }[input(message).lower()]

def main():
    while True:
        option = input('Option (fetch, create, delete, exit): ')
        if option == 'fetch':
            resp = requests.get('http://jsonplaceholder.typicode.com/todos')
            print(resp.text)
        elif option == 'create':
            title  = input('Title: ')
            user_id = sanitize_input('User ID: ', int, 'You must enter an integer')
            completed = sanitize_input('Completed? (y/n): ', bool, 'You must type either y or n')
            data = { "title": title, "userId": user_id, "completed": completed }
            resp = requests.post('http://jsonplaceholder.typicode.com/todos', data = json.dumps(data), headers = { "Content-type": "application/json" })
            print(resp.text)
        elif option == 'delete':
            todo_id = input('TODO ID: ')
            resp = requests.delete('http://jsonplaceholder.typicode.com/todos/' + todo_id)
            print(resp.text)
        elif option == 'exit':
            print('Bye')
            exit()
        else:
            print('Invalid option')

if __name__ == "__main__":
    main()