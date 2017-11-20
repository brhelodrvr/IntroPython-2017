#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# html_render1.py


class Element():
    tag = 'html'
    indent = '  '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        ''' add another string to the content. '''
        self.content.append(content)

    def render(self, file_obj):
        try:
            all_content
        except UnboundLocalError:
            all_content = ''
        else:
            all_content += ('<' + self.tag + '>')

        for each in self.content:
            try:
                all_content += each
            except TypeError:
                each.render(file_obj)
        all_content += '</' + self.tag + '>'
#        except TypeError:
#            each.render(each, file_obj)

        self.write_to_file(file_obj, all_content)

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)


class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class HTML(Element):
    tag = 'html'
