import requests
import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st


def scrape_books() -> pd.DataFrame:
    """
    This function scrapes the book data from the given URL and returns a DataFrame.

    Parameters:
    No parameters are required for this function.

    Returns:
    A pandas DataFrame containing the scraped book data. The DataFrame has two columns: 'title' and 'price'.

    The 'title' column contains the title of the book, and the 'price' column contains the price of the book.
    """
    url = "http://books.toscrape.com/"
    try:
        url = requests.get(url)
        soup = BeautifulSoup(url.content, "html.parser")
        enlaces = soup.find('ul').find_all('a')

        # calificaciones = soup.find_all('p', class_='start-rating')

        books = []
        for item in soup.find_all('article', class_='product_pod'):
            title = item.h3.a['title']
            price = item.find('p', class_='price_color').text
            qualification_class = item.find('p', class_='star-rating')['class'][1]
            qualification = ['One', 'Two', 'Three', 'Four', 'Five'].index(qualification_class) + 1
            books.append({'title': title, 'price': price, 'stars': qualification})
        return pd.DataFrame(books)
    except Exception as e:
        print("Error al acceder a la pagina web {url} \n {e}")
        return pd.DataFrame()

    options = st.multiselect(
    "Filtre por precio y calificación que desee",
    ["price", "star", "title"],
    ["price", "star"],
)

    st.write("You selected:", options)


if __name__ == '__main__':
    books_df = scrape_books()
    books_df.to_csv('books.csv', index=False)
    print('Books saved to books.csv')

