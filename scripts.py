def fix_marks(child_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except ObjectDoesNotExist:
        print("Нет ученика с таким именем и фамилией")
    except MultipleObjectsReturned:
        print("Найдено несколько учеников с введенными данными.")
    bad_marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    return


def delete_chastisements(child_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except ObjectDoesNotExist:
        print("Нет ученика с таким именем и фамилией")
    except MultipleObjectsReturned:
        print("Найдено несколько учеников с введенными данными.")
    chastisements = Chastisement.objects.filter(schoolkid=child)
    for chastisement in chastisements:
        chastisement.delete()
    return


def create_commendation(child_name, subject_title):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
        subjects = Lesson.objects.filter(
            year_of_study=child.year_of_study,
            group_letter=child.group_letter,
            subject__title=subject_title)
        commendation = random.choice(commendations)
        subject = subjects[random.randint(0, len(subjects))]
        Commendation.objects.create(
            schoolkid=child,
            subject=subject.subject,
            teacher=subject.teacher,
            text=commendation,
            created=subject.date)
    except ObjectDoesNotExist:
        print("Нет ученика или предмета с таким именем.")
    except MultipleObjectsReturned:
        print("Найдено несколько учеников с введенными данными.")
    return
