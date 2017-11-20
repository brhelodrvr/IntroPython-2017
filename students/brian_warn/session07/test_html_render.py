#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

# import html_render1
from html_render1 import Element, Body, Para, HTML

def test_new_element():
    ''' test that this can initialize '''
    el_object = Element()
    el_object2 = Element('content')


def test_add_content():
    ''' testing internal structure to see what's going on. '''
    el_object = Element('content')
    el_object = Element()
    assert el_object.content == []


def test_adding_empty_string():
    el_object = Element('')
    assert el_object.content == ['']


def test_append_string():
    el_object = Element('spam')
    el_object.append(', wonderful spam')
    assert el_object.content == ['spam', ', wonderful spam']


def test_class_tag_exists():
    assert Element.tag == 'html'
    el_object = Element('spam, spam')
    assert el_object.tag == 'html'


def test_indent_exists():
    assert Element.indent == '  '


def test_render():
    my_stuff = 'spam'
    el_object = Element(my_stuff)
    more_stuff = 'eggs, eggs'
    el_object.append(more_stuff)

    with open('file_test1', 'w') as out_file:
        el_object.render(out_file)
    with open('file_test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_body_tag():
    assert Body.tag == 'body'


def test_p_tag():
    assert Para.tag == 'p'


def test_html_tag():
    assert HTML.tag == 'html'


def test_render_body():
    my_stuff = 'spam'
    el_object = Body(my_stuff)
    more_stuff = 'eggs, eggs'
    el_object.append(more_stuff)

    with open('file_test1', 'w') as out_file:
        el_object.render(out_file)
    with open('file_test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<body>')
    assert contents.endswith('</body>')
    assert my_stuff in contents
    assert more_stuff in contents


def test_render_non_strings():

    el_object = Element(Body('a string for testing'))
    # need to solve this with recursion
    with open('file_test1', 'w') as out_file:
        el_object.render(out_file)  # <-- fails here
    with open('file_test1', 'r') as in_file:
        contents = in_file.read()

