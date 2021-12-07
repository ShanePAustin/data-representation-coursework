from BookDao import bookDao

book1 = {
    'ISBN' : 1234567,
    'title' : 'Some fantasy book',
    'author' : 'jk',
    'price' : 12,

}

book2 = {
    'ISBN' : 12345678,
    'title' : 'had a little lamb',
    'author' : 'mary',
    'price' : 999,

}

#returnValue = bookDao.create(book)
returnValue = bookDao.getAll()
print(returnValue)
returnValue = bookDao.findById(book2['ISBN'])
print('find By ID')
print(returnValue)
returnValue = bookDao.update(book2)
print(returnValue)
returnValue = bookDao.findById(book2['ISBN'])
print(returnValue)
returnValue = bookDao.delete(book2['ISBN'])
print(returnValue)
returnValue = bookDao.getAll()
print(returnValue)