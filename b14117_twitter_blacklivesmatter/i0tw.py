import twint
import schedule
import time


# you can change the name of each "job" after "def" if you'd like.
def jobone():
	print("Fetching Tweets")
	c = twint.Config()
    # choose username (optional)
    # c.Username = ""
    # choose search term (optional)
	searchstr = "(#blacklivesmatter) until:2020-05-30 since:2020-05-25)"
	#searchstr = "(#Goerge Floryd) until:2020-07-25 since:2020-05-25)"
	c.Search = searchstr
    #c.Search = ""
    # c.Search = "#eth"
    # choose beginning time (narrow results)
    #c.Since = "2021-01-01"
    # set limit on total tweets
	c.Limit = 2000
    # no idea, but makes the csv format properly
	c.Store_csv = True

    # change the name of the csv file
	c.Output = "black2.csv"
	#c.Output = "fd1.csv"
	twint.run.Search(c)



# run once when you start the program

jobone()


# run every minute(s), hour, day at, day of the week, day of the week and time. Use "#" to block out which ones you don't want to use.  Remove it to active. Also, replace "jobone" and "jobtwo" with your new function names (if applicable)

# schedule.every(1).minutes.do(jobone)
schedule.every().hour.do(jobone)



while True:
    schedule.run_pending()
    time.sleep(1)
