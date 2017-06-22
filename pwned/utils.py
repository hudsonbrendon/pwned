from colors import color


def cli(services):
    message = 'Your data in the following services' \
              'have already been leaked:\n'
    if services:
        print(color(message, fg='red'))
        for service in services:
            print(color(service, fg='red') + '\n')
    else:
        print(color('None of your data has yet been leaked ...', fg='red'))
