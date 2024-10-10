import os
import requests
from threading import Thread
from queue import Queue


# Function to download an image from a URL
def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {save_path}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")


# Worker function to process items in the queue
def worker(queue):
    while not queue.empty():
        url, save_path = queue.get()
        download_image(url, save_path)
        queue.task_done()


# Main function to set up the queue and threads
def main(urls, save_dir, num_threads=4):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    queue = Queue()
    for url in urls:
        filename = os.path.basename(url)
        save_path = os.path.join(save_dir, filename)
        queue.put((url, save_path))

    threads = []
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(queue,))
        thread.start()
        threads.append(thread)

    queue.join()  # Wait for all tasks to be processed

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # List of image URLs to download
    image_urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
        # Add more URLs as needed
    ]

    # Directory to save downloaded images
    save_directory = "data"

    # Number of threads to use
    num_threads = 32
    main(image_urls, save_directory, num_threads)