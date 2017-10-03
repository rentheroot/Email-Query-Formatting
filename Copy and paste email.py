lineNumber = 1
previous = 'no'
year = input('What year were the archives from: ')
#--Open File--#
with open('test_file.html', 'w') as the_file:

    #--Write web headers--#
    the_file.write('<!DOCTYPE html>\n')
    the_file.write('<html>\n')
    the_file.write('<head>')
    the_file.write('<meta charset="UTF-8">\n')
    the_file.write('<title>Skinner Family Association</title>\n')
    the_file.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
    the_file.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n')
    the_file.write("<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha.6/css/bootstrap.min.css'>\n")
    the_file.write("<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css'>\n")
    the_file.write('<link rel="stylesheet" href="css/style.css">\n')
    the_file.write("</head>\n")
    the_file.write('<body>\n')
    the_file.write('<!-- Add Navigation bar to this page -->\n')
    the_file.write('<script src="//code.jquery.com/jquery.min.js"></script>\n')
    the_file.write('<script>\n')
    the_file.write('$.get("navigation.html", function(data){\n')
    the_file.write('\t$("#nav-placeholder").replaceWith(data);\n')
    the_file.write('});\n')
    the_file.write('</script>\n')
    the_file.write('\t<div id="nav-placeholder"> </div>\n')
    the_file.write('<!-- End of Navigation bar -->\n')
    the_file.write('<!-- Start of Content -->\n')
    the_file.write('<h1 class = "text-center">'+ year + '</h1>\n')
    for line in open('unformatted.txt', 'r'):
        if 'Subject:' in line:
            if lineNumber == 1:
                the_file.write('<div class = email-query>')
                a,b = line.split(':')
                the_file.write('<p>Subject: ' + b + '</p>'+ '\n')
                lineNumber = lineNumber + 1
            else:
                the_file.write('</div>'+ '\n' + '<div class = "email-query">')
                a,b = line.split(':')
                the_file.write('<p>Subject: ' + b + '</p>'+ '\n')
            
        elif 'Date:' in line:
            a,b = line.split(':')
            the_file.write('<p>Date: ' + b + '</p>' + '\n')

        elif 'From:' in line:
            a,b = line.split(':')
            the_file.write('<p>From: ' + b + '</p>' + '\n' + '<p>')

        elif line == '\n':
            the_file.write('<p></p>' + '\n')
            previous = 'yes'
            

        else:
            the_file.write('<p>' + line + '</p>')


    the_file.write('</p>\n')
    the_file.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>\n")
    the_file.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha.6/js/bootstrap.min.js'></script>\n")
    the_file.write('</body>')
                
