import xlwt


def makeExcelFile(vacancies):
    header_font = xlwt.Font()
    header_font.name = 'Arial'
    header_font.colour_index = 0
    header_font.bold = True
    header_style = xlwt.XFStyle()
    header_style.font = header_font
    header_pattern = xlwt.Pattern()
    header_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    header_pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']
    header_style.pattern = header_pattern

    basic_font = xlwt.Font()
    basic_font.name = 'Arial'
    basic_font.colour_index = 0
    basic_font.bold = False
    basic_style = xlwt.XFStyle()
    basic_style.font = basic_font

    wb = xlwt.Workbook()
    ws = wb.add_sheet('1')

    ws.write(0, 0, 'Название вакансии', header_style)
    ws.write(0, 1, 'Работодатель', header_style)
    ws.write(0, 2, 'Ссылка на вакансию', header_style)
    ws.write(0, 3, 'Город вакансии', header_style)
    ws.write(0, 4, 'Зарплата', header_style)
    ws.write(0, 5, 'Дата объявления', header_style)

    for (vacancyIndex, vacancy) in enumerate(vacancies, start=1):
        ws.write(vacancyIndex, 0, vacancy['name'], basic_style)
        ws.write(vacancyIndex, 1, vacancy['employer'], basic_style)
        ws.write(vacancyIndex, 2, vacancy['url'], basic_style)
        ws.write(vacancyIndex, 3, vacancy['city'], basic_style)
        ws.write(vacancyIndex, 4, vacancy['salary'], basic_style)
        ws.write(vacancyIndex, 5, vacancy['date'], basic_style)

    wb.save('vacancies.xls')