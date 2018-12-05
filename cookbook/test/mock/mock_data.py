from cookbook.models import *
from django.core.files.uploadedfile import SimpleUploadedFile


def clear_new_line(line):
    return line.replace("\n", "").replace("\r", "")


def set_data():
    read = ReadData()
    image = SimpleUploadedFile(name='dot.jpg', content=open('cookbook/static/image/dot.jpg', 'rb').read())
    for time in read.time_tags:
        CookTime.objects.create(cooking_time=time)
    for equipment in read.equipment_tags:
        Equipment.objects.create(equipment_required=equipment)
    for allergies in read.allergies_tags:
        Allergies.objects.create(allergies_ingredient=allergies)
    for category in read.category_tags:
        Category.objects.create(food_category=category)
    for author in read.author_user:
        AuthorUser.objects.create(user_username=author[0], recipe_name=author[1])
    for alias in read.user_alias:
        UserAlias.objects.create(user_username=alias[0], alias_name=alias[1])
    for recipe in read.recipe_list:
        Recipe.objects.create(recipe_chef=recipe[0], recipe_name=recipe[1], recipe_info=recipe[2],
                              recipe_time=recipe[3], recipe_equipment=recipe[4], recipe_fat=recipe[5],
                              recipe_ingredient=recipe[6], recipe_method=recipe[7], recipe_image_1=image)


class ReadData:
    time_tags = []
    equipment_tags = []
    category_tags = []
    allergies_tags = []
    recipe_list = []
    author_user = []
    user_alias = []

    def __init__(self):
        self.read_time_require()
        self.read_allergies_require()
        self.read_category_require()
        self.read_equipment_require()
        self.read_recipe()

    def read_time_require(self):
        time_path = "cookbook/test/mock/data/time_preb_require.txt"
        time_read = open(time_path, "r")
        for i in time_read.readlines():
            self.time_tags.append(clear_new_line(i))
        time_read.close()
        return self.time_tags

    def read_equipment_require(self):
        equipment_path = "cookbook/test/mock/data/equipment_require.txt"
        equipment_read = open(equipment_path, "r")
        for i in equipment_read.readlines():
            self.equipment_tags.append(clear_new_line(i))
        equipment_read.close()
        return self.equipment_tags

    def read_allergies_require(self):
        allergies_path = "cookbook/test/mock/data/allergies_require.txt"
        allergies_read = open(allergies_path, "r")
        for i in allergies_read.readlines():
            self.allergies_tags.append(clear_new_line(i))
        allergies_read.close()
        return self.allergies_tags

    def read_category_require(self):
        category_path = "cookbook/test/mock/data/category_require.txt"
        category_read = open(category_path, "r")
        for i in category_read.readlines():
            self.category_tags.append(clear_new_line(i))
        category_read.close()
        return self.category_tags

    def read_recipe(self):
        recipe_path = "cookbook/test/mock/data/recipes.txt"
        recipe_read = open(recipe_path, "r", encoding='utf8', errors='ignore')
        recipe_mock = recipe_read.readlines()
        for recipe_data in recipe_mock:
            recipe_mock_split = recipe_data.split("$$")
            self.user_alias.append([clear_new_line(recipe_mock_split[0]), clear_new_line(recipe_mock_split[1])])
            self.author_user.append([clear_new_line(recipe_mock_split[0]), clear_new_line(recipe_mock_split[2])])
            self.recipe_list.append(
                [clear_new_line(recipe_mock_split[1]), clear_new_line(recipe_mock_split[2]),
                 clear_new_line(recipe_mock_split[3]), clear_new_line(recipe_mock_split[4]),
                 clear_new_line(recipe_mock_split[5]), clear_new_line(recipe_mock_split[6]),
                 clear_new_line(recipe_mock_split[7]), clear_new_line(recipe_mock_split[8])])
            recipe_read.close()
