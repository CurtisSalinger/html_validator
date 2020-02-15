#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    """
    lst = []
    for tag in _extract_tags(html):
        char = html[i]
        if char in "<" :
            lst.append(char)
        else:
            if lst == []:
                balanced = False
            else:
                top = lst.pop()
                if not 
    if balanced and lst==[]:
        return True
    else:
        return False
    """
    """
    balanced = true

    tags = _extract_tags(html)
    while (len(tags) % 2 == 0):
        if tags[0][1:] not in tags[-1][2:]:
            print("tags when false = ")
            return false
        else:
            tags = tags[2:-1]
            print("else line = ", tags)
        for i in range(len( tags)):
            if tags[i] != tags[-i+1]:
                balanced = false
    return balanced
    """




    balanced = True
    if len(tags) == 0 or len(tags) % 2 == 1:
        return False
    for i in range(len( tags)): 
        if tags[i] != tags[-i+1]:
            balanced = False
    return balanced





    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.
    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    while len(html) != 0:
        left = html.find('<')
        right = html.find('>')
        if left == -1 or right == -1:
            break
        tags.append(html[left:(right + 1)])
        html = html[(right + 1):]
        
    return tags


