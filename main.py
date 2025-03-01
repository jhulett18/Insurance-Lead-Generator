
#Absolute import:
#folder.module:

# from leadFinderlive.functions import *
# from nameFinderlive.entityFunctions import *
# from scisFinderlive.scisfunctions import *

from leadFinderlive.leadFinder import leadFinder
from nameFinderlive.entityFinder import entityFinder
from scisFinderlive.SCISfinder import scisFinder


def main():

    # readJSON()
    
    leadFinder()
    
    entityFinder()
    
    scisFinder()

if __name__ == '__main__':
    main()
