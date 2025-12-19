def is_teacher_or_admin(user):
    return user.is_superuser or user.groups.filter(name='teacher').exists()
