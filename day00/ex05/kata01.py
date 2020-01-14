if __name__ == '__main__':
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
    for key, val in languages.items():
       print("{} was created by {}".format(key, val))
