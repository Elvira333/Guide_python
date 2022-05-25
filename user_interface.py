import data
import logger as log

def surname_view():
    d = data.get_surname()
    log.add_surname(d)
    return d
def name_view():
    d = data.get_name()
    log.add_name(d)
    return d
def number_view():
    d = data.get_number()
    log.add_number(d)
    return d
def discription_view():
    d = data.get_description()
    log.add_description(d)
    return d