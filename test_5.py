search_queries = ["watch new movies", "coffee near me", "how to find the determinant",\
                "python", "data science jobs in UK", "courses for data science", "taxi",\
                "google", "yandex", "bing", "foreign exchange rates USD/BYN",\
                "Netflix movies watch online free",  "Statistics courses online from top universities"]

def words_query(query: list):

    words_number = []

    for query in query:
        words_number.append(len(query.split()))

    for number in set(words_number):
        if number == 1:
            print(f"{number} слово: {round(words_number.count(number)/len(search_queries)*100)}%")
        elif 2 <= number <= 4:
            print(f"{number} слова: {round(words_number.count(number)/len(search_queries)*100)}%")
        else:
            print(f"{number} слов: {round(words_number.count(number)/len(search_queries)*100)}%")

words_query(search_queries)


