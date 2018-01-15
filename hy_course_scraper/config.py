
# TODO

SCRAPE_URL_PREFIX = 'https://courses.helsinki.fi/fi/search/results/field_imp_organisation'
SCRAPE_URL_SUFFIX = '&search=&academic_year=START%20-%20END'

SCRAPED_FIELDS = [
  'matemaattis-luonnontieteellinen-tiedekunta-942/field_imp_organisation/tietojenk%C3%A4sittelytieteen-kandiohjelma-1922',
  'matemaattis-luonnontieteellinen-tiedekunta-942/field_imp_organisation/tietojenk%C3%A4sittelytieteen-maisteriohjelma-1929',
  'matemaattis-luonnontieteellinen-tiedekunta-942/field_imp_organisation/datatieteen-maisteriohjelma-1931'
]

def get_current_year():
  
def generate_suffix():
  current_year = get_current_year()
  f = re.sub('^START', current_year[0], SCRAPE_URL_SUFFIX)
  return re.sub('^END', current_year[1], f)

def get_scraped_fields():
  suffix = generate_suffix()
  return [''.join(SCRAPE_URL_PREFIX, field, suffix) for field in SCRAPED_FIELDS]

