import csv

from mvindex.models import Movie

file_path = 'scripts/files/movielist2.csv'

def isNull(item):
    if(item == null):
        return "na"
    else:
        return item

def run():
    data_reader = csv.reader(open(file_path, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
    purge_all()
    import_movies()


def purge_all():
    print('purging all movies')
    all_movies = Movie.objects.all()
    all_movies.delete()

def import_movies():
    movie_count = 0
    data_reader = csv.reader(open(file_path, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
    for row in data_reader:
        print(row)
        movie_count += 1
        id = clean(row[0])
        title = clean(row[1])
        #date = clean(row[2])
        print(id)
        print(title)
        #print(date)
        movieinstance = Movie.objects.create(
            imdbid = id,
            title = title,
        )
    print('Movie instances created.')




def clean(field):
    	if field in ('<null>', 'null', 'None', '','n/a'):
		return ''
	else:
		return field.strip()