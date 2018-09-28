from random import choice


def random_comment(hashtag):
    choices = [
        f'Yeah {hashtag} rocks!',
        'Nice!',
        f'#{hashtag} !',
        'yup',
        'so true'
    ]
    return choice(choices)