import requests


def getVacancies(vacancy):
    rawVacancies = []
    attempt = 0
    for page in range(20):
        while attempt < 10:
            try:
                response = requests.get(f'https://api.hh.ru/vacancies?per_page=100&page={page}&text={vacancy}').json()
                rawVacancies += response['items']
                break
            except:
                attempt += 1
    vacanciesCount = len(rawVacancies)

    vacancies = []
    for rawVacancy in rawVacancies:
        if rawVacancy['salary']:
            salary_from = rawVacancy['salary']['from']
            salary_to = rawVacancy['salary']['to']
            salary_currency = rawVacancy['salary']['currency']

            if salary_from and salary_to:
                salary = f'{salary_from} - {salary_to} {salary_currency}'
            elif salary_from and not salary_to:
                salary = f'{salary_from} {salary_currency}'
            elif not salary_from and not salary_to:
                salary = '-'
        else:
            salary = '-'

        year, month, day = rawVacancy['published_at'].split('-')
        day = day[:2]

        if rawVacancy['address']:
            city = rawVacancy['address']['city']
        else:
            city = '-'

        vacancies.append({
            'name': rawVacancy['name'],
            'employer': rawVacancy['employer']['name'],
            'url': rawVacancy['alternate_url'],
            'city': city,
            'salary': salary,
            'date': f'{year}.{month}.{day}'
        })

    return vacancies