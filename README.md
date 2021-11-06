# schengen-visa-scraper

### Background

I got my Schengen visa recently! However, the application process was a bit unpleasant. I plan to go to France in the early December, so my first choice was to apply from France. Because I could only make an appointment after I filled out the application form, and the application form asks where I plan to live, I needed to book a hotel and make an itinerary. But after I was forwarded to make an appointment, I only found out that the earliest available slot is in December, which wouldn't allow me to go on the trip on time. I tried another country, Netherland, with the same outcome (i.e., no early enough slots after a lot of paperwork).

This motivates me to develop this project, to help anybody who plans to apply for a Schengen visa in the near future to more efficiently decide which country to apply from. Wish you all the best with the Schengen visa application process!

### How to Use It?
To use it to find out the earliest available schengen visa appointment slots, you only need a laptop with Python installed and a stable internet connection. Here's what you need to do:
1. Download the project;
2. Run the script "scraper.py";
3. Find everything that has been scraped for you in the generated file "available_slots.csv."

### How I Built It?

I used the popular [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) library as HTML parser and the [Selenium](https://selenium-python.readthedocs.io/) library to automate browser. I also used [Dropbox](https://www.dropbox.com/) to cache the scraped data so only 1 request per day to the server is required. For more details, please take a look at the code.

Please note that inside this repository there is information about some dummy accounts I created to scrape the useful appointment slot data. **Please do NOT try to login with those accounts!** There is also an access token which gives read and write permission for a Dropbox I created for this project. **Please do NOT try to modify (i.e., uploading, changing, deleting, etc.) any files through this token!**

If you find any issues that prevent you from using this scraper, please let me know (by submitting a pull request)!