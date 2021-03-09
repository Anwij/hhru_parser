from hh import getVacancies
from excel import makeExcelFile


vacancy = input()
print(f'Поиск вакансий по запросу "{vacancy}"')
vacancies = getVacancies(vacancy)
vacanciesCount = len(vacancies)
print(f'Найдено {vacanciesCount} вакансий по запросу "{vacancy}"')
makeExcelFile(vacancies)
print('Создана Excel таблица vacancies.xls, проверьте папку со скриптом')