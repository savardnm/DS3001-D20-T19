# DS3001-D20-T19

##The Need and Benefits##

Popular media streaming services tend to recommend titles and genres to users that they already rated highly, however, this system is limited in what is recommended. Our system aims to address this by taking in user data about the books they have read and enjoyed, and then using this data to find the polar opposite of their current suggestions. This could be useful for people trying to branch out from their traditional books and try some new experiences. It can also be used to find suggestions that are dissimilar to what they tend to read in terms of genres and themes allowing the user to expand their repertoire.

##The Dataset##

For our dataset, we are using data from Goodbooks on books, their tags, and their ratings, found at https://www.kaggle.com/zygmunt/goodbooks-10k. This dataset provides separate data sets separated by book and by user. Data sorted by book allows us to fund overarching data about certain titles such as average ratings, common tags, and metadata. Data sorted by users will allow us to compare and contrast the input user data with existing user data.
We can also use the GoodReads API to get input user data. This service is used by people who read books to keep track of what they read and what they enjoyed. It holds user-specific data about their ratings and prefered genres. We are not sure if we are going to incorporate this data into the final project, but it could be worth exploring to connect the user with their existing account. 

##How to run##

To run this program, you need to pull the repository and run the GUI.py file through a python development environment such as Spyder.

Once the GUI is open, follow the instructions at the top of the screen to receive you recommendations.
