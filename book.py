def extract_info(book_list):
    result = []
    for book in book_list:
        title = book.find("a", {"class":"N=a:bta.title"}).string
        img_src = book.find("div", {"class":"thumb type_best"}).find("div", {"class": "thumb_type thumb_type2"}).find("a",{"class":"N=a:bta.thumb"}).find("img")["src"]
        link = book.find("div", {"class":"thumb type_best"}).find("div", {"class": "thumb_type thumb_type2"}).find("a", {"class":"N=a:bta.thumb"})["href"]
        author = book.find("dl").find("dd").find("a", {"class": "txt_name"}).text
        publisher = book.find("dl").find("dd").find("a", {"class": "N=a:bta.publisher"}).text
        book_info = {
            'title' : title,
            'img_src' : img_src,
            'link': link,
            'author': author,
            'publisher': publisher
        }
        result.append(book_info)
    return result