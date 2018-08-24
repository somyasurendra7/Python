import click
import threading
import requests


def Handler(start, end, url, filename):

    # starting and ending of th file
    headers = {'Range': 'bytes=%d-%d' %(start, end)}

    # requesting the specific part
    r = requests.get(url, headers=headers, stream=True)

    with open(filename, "r+b") as fp:
        fp.seek(int(start))
        var=fp.tell()
        fp.write(r.content)

@click.command(help="Download of specified file with the specified command.")
@click.option('--number_of_threads', default=4, help="Number of Threads")
@click.option('--name', type=click.Path(), help="Name of the file with extension.")
@click.argument('url_of_file', type=click.Path())
@click.pass_context


def download_file(ctx, url_of_file, name, number_of_threads):
    r = requests.head(url_of_file)
    if name:
        file_name = name
    else:
        file_name = url_of_file.split('/')[-1]
    try:
        file_size = int(r.headers['content-length'])
    except:
        print("Invalid URL")
        return
    
    part = int(file_size) / number_of_threads
    fp = open(file_name, "wb")
    fp.write(b'\0' * file_size)
    fp.close()

    for i in range(number_of_threads):
        start = part * i
        end = start + part 

        t = threading.Thread(target= Handler, args=(start, end, url_of_file, file_name))
        t.daemon = True
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('Downloaded', file_name)


if __name__ == '__main__':
    download_file(obj={})







