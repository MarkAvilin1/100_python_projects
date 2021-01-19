import smtplib
import datetime as dt
import random

my_email = "avilinmark1@gmail.com"
password = "whiteking"

date = dt.datetime.now()
week_day = date.weekday()

if week_day == 2:
    with open("quotes.txt", encoding="utf8") as f:
        data = f.readlines()

        new_data = [i.split("– ")[0] for i in data]
        quote = random.choice(new_data)
        word = quote[1:-2]
        my_quotes = [i[1:-2] for i in new_data]

        with open("new_quotes.txt", "w") as data_file:
            data_file.write(str(my_quotes))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="avilin1@yahoo.com",
                            msg=f"subject: Hello\n\n{str(word)}")




