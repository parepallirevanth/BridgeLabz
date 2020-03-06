import json


def userdata():
    file = open("UsersData", 'r')
    data = json.load(file)
    file.close()
    print(data['Users'])

    for key, value in data.items():
        print(f"The {key} details are as follows: ")
        for user in value:
            for key, value in user.items():
                print(f"{key} Details:")
                for detail in value:
                    for key, values in detail.items():
                        print(f"{key}: {values}")


userdata()
