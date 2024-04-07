
import pandas
import datetime as dt
import smtplib
import random

data = pandas.read_csv("birthdays.csv")
revised_data = data.to_dict(orient='records')
print(revised_data)

for i in revised_data:
    contact_index = revised_data.index(i)
    # print(location)
    letter_number = random.randint(1, 3)
    print(letter_number)

    date_time = dt.datetime.now()
    day = date_time.day
    month = date_time.month

    if month == revised_data[contact_index]["month"] and day == revised_data[contact_index]['day']:
        with open(f"letter_templates/letter_{letter_number}.txt", mode='r') as file:
            content = file.read()
            name_update = content.replace("[NAME]", revised_data[contact_index]["name"])
        with open(f"letter_templates/letter_{letter_number}.txt", mode='w') as file:
            new_content = file.write(name_update)
        #The below code also needs to be mentioned otherwise the txt file won't be read
        with open(f"letter_templates/letter_{letter_number}.txt", mode='r') as file:
            send_content = file.read()

        EMAIL = "****@******.com"
        PASSWORD = "************"

        with smtplib.SMTP("smtp.******.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=revised_data[contact_index]["email"],
                msg=f"Subject:Birthday Wish\n\n{send_content}"
            )

        # Replacing the name in the letters with the placeholder [NAME]
        with open(f"letter_templates/letter_{letter_number}.txt", mode='r') as file:
            content = file.read()
            default_name = content.replace(revised_data[contact_index]["name"], "[NAME]")
        with open(f"letter_templates/letter_{letter_number}.txt", mode='w') as file:
            default_content = file.write(default_name)
