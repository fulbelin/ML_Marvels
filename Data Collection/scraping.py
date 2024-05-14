import urllib.request
def fetch_latest_paper(topic):
    # Replace spaces in the topic with '+' to fit the query parameter requirements
    formatted_topic = topic.replace(' ', '+')
    # Construct the URL with dynamic search query based on the topic
    url = f'http://export.arxiv.org/api/query?search_query=all:{formatted_topic}&sortBy=submittedDate&sortOrder=descending&start=0&max_results=1'
    # Open the URL and read the data
    data = urllib.request.urlopen(url)
    # Decode the fetched XML data and print it
    print(data.read().decode('utf-8'))
# Example usage: Fetch the latest paper on a specific topic
fetch_latest_paper('quantum mechanics')