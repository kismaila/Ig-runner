import time
from instabot import Bot
import random

# Set up your bot credentials (replace with your real Instagram login credentials)
username = 'kenyanismaila69'  # Your Instagram username
password = 'W1692seven'  # Your Instagram password

# Define the bot's follow behavior
def run_bot():
    # Initialize the bot
    bot = Bot()
    bot.login(username=username, password=password)

    # List of target pages (hashtags or users)
    target_pages = ['yapfilms', 'aamu_honest_program', 'aamu_athletes', 'aamu1875', 'hbcu_buzz']
    
    # List of DM messages
    dm_messages = [
        "You from Huntsville?",
        "Yo, you look familiar, you go to AAMU?"
    ]
    
    # Follow and DM users from the target pages
    for page in target_pages:
        # Find users from the target pages
        users = bot.get_users_from_tag(page)
        
        for user in users:
            # Follow the user
            bot.follow(user)
            
            # Send a DM
            message = random.choice(dm_messages)
            bot.send_message(message, [user])
            
            # Like their latest post
            bot.like_user(user)
            
            time.sleep(random.randint(5, 10))  # Wait a few seconds before the next action

    print("Bot has finished following and DMing users.")
    
if __name__ == "__main__":
    run_bot()