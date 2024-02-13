search_queries = ["watch new movies", "coffee near me", "how to find the determinant",\
                "python", "data science jobs in UK", "courses for data science", "taxi",\
                "google", "yandex", "bing", "foreign exchange rates USD/BYN",\
                "Netflix movies watch online free",  "Statistics courses online from top universities"]

def words_query(queries_list: list):

    # Calculation of the number of words in each query: words_number
    words_number = []

    for query in queries_list:
        words_number.append(len(query.split()))

    # Calculation of the distribution of words in each query:
    for number in set(words_number):
        if number == 1:
            print(f"{number} слово: {round(words_number.count(number)/len(queries_list)*100)}%")
        elif 2 <= number <= 4:
            print(f"{number} слова: {round(words_number.count(number)/len(queries_list)*100)}%")
        else:
            print(f"{number} слов: {round(words_number.count(number)/len(queries_list)*100)}%")

words_query(search_queries)



""" The code above may be modified taking into account that articles and in some cases prepositions \
    may be not considered as fully valid words. So they can distort the found distribution.
    Below is a solution for deleting articles. Due to the described modification, the output is \
    different for "4 слова" и "5 слов" items. """ 

def words_query_modified(queries_list: list):

    # The list of deleting articles: articles
    articles = ["a", "an", "the"]
    
    # The list of splitted queries without articles: indiv_queries
    indiv_queries = []

    for query in queries_list:
        indiv_queries.append(query.split())
    
    for art in articles:
        for i in indiv_queries:
            if art in i:
                i.remove(art)

    # Calculation of the number of words in each query: words_number
    words_number = []

    for query in indiv_queries:
        words_number.append(len(query))

    for number in set(words_number):
        if number == 1:
            print(f"{number} слово: {round(words_number.count(number)/len(queries_list)*100)}%")
        elif 2 <= number <= 4:
            print(f"{number} слова: {round(words_number.count(number)/len(queries_list)*100)}%")
        else:
            print(f"{number} слов: {round(words_number.count(number)/len(queries_list)*100)}%")

words_query_modified(search_queries)