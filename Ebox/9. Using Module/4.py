def main():
    topics = input("Enter the String").strip().split()  # Read input and split into list of topics
    topic_count = {}
    
    # Count occurrences of each topic
    for topic in topics:
        if topic in topic_count:
            topic_count[topic] += 1
        else:
            topic_count[topic] = 1
    
    # Output the count of each topic
    for topic, count in sorted(topic_count.items()):  # Sort by topic name alphabetically
        print(topic.lower() + "-" + str(count))

if __name__ == '__main__':
    main()