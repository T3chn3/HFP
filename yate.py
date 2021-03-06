#import of the Template function from the string class allowing string substution templates
from string import Template

#a function to set the content type of a response from server to client
#This function takes a single (optional) string as its argument and uses it to create a CGI “Content-type:” line, with “text/html” as the default.
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

#Opens the .html page and substitutes the title
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

#Opens the .html page and substitues the links
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

# This function returns the HTML for the start of a form and lets the caller specify the URL to send the form’s data to, as well as the method to use.
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

#This function returns the HTML markup, which terminates the form while allowing the caller to customize the text of the form’s “submit” button.  
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

#used to hold the values of the seleted item on the raido button, by name and the value
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

#builds a list of items                             
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

#Builds html header items H1,H2,H3...Hn, with level 2 as the defualt  
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

#can be used to start a new paragraph of text
def para(para_text):
    return('<p>' + para_text + '</p>') 
