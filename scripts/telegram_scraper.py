from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv
from asyncio import gather

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')


# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    try:
        entity = await client.get_entity(channel_username)
        
        channel_title = entity.title  # Extract the channel's title
        async for message in client.iter_messages(entity, limit=10000):
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
                # Create a unique filename for the photo
                filename = f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                # Download the media to the specified directory if it's a photo
                await client.download_media(message.media, media_path)

            # Write the channel title along with other data
            writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])

        print(f"Scraped data from {channel_username}")
    except Exception as e:
        print(f"Failed to scrape data from {channel_username}: {e}")

#  scrape data from multiple channels concurrently
async def scrape_multiple_channels(client, channels, media_dir, csv_file):
    os.makedirs(media_dir, exist_ok=True)  # Create a directory for media files

    # Open the CSV file and prepare the writer
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # CSV header

        # Gather tasks for concurrent scraping
        tasks = [scrape_channel(client, channel, writer, media_dir) for channel in channels]
        await gather(*tasks)  # Run all tasks concurrently

#  initialize the Telegram client and start scraping
async def main():
    media_dir = 'photos'
    csv_file = 'telegram_data.csv'

    # List of Telegram channels to scrape
    channels = [
        '@DoctorsET',
        '@lobelia4cosmetics',
        '@yetenaweg',
        '@EAHCI',
        
    ]

    print(f"Starting to scrape data from {len(channels)} channels...")
    await scrape_multiple_channels(client, channels, media_dir, csv_file)
    print("Data scraping complete!")

# Initialize the Telegram client
client = TelegramClient('scraping_session', api_id, api_hash)


with client:
    client.loop.run_until_complete(main())
