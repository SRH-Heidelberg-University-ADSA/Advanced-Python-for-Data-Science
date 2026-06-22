# open the file
# iterate over each line
# function : filter word
# function : insert into db


def begin_coroutine(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        result.__next__()
        return result

    return inner_function


def data_pipeline_start(file, next_stage):
    while True:
        line = file.readline()
        if not line:
            break
        next_stage.send(line)


@begin_coroutine
def insert_db():
    while True:
        line = yield
        print(f"insert {line} in db")


@begin_coroutine
def filter_word(keyword, next_stage):
    while True:
        line = yield
        if keyword in line:
            # insert db
            next_stage.send(line)


file = open(
    "/Users/D068192/dev/codes/git/srh/Advanced-Python-for-Data-Science/Week2/Lecture/bible.txt"
)

data_pipeline_start(file, filter_word("God", insert_db()))
