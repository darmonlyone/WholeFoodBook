from django.db import model


class CookTime(models.Model):
    cooking_time = models.CharField(max_length=30)

    def __str__(self):
        return self.cooking_time


class Equipment(models.Model):
    equipment_required = models.CharField(max_length=30)

    def __str__(self):
        return self.equipment_required


class Allergies(models.Model):
    allergies_ingredient = models.CharField(max_length=30)

    def __str__(self):
        return self.allergies_ingredient


class Category(models.Model):
    food_category = models.CharField(max_length=30)

    def __str__(self):
        return self.food_category


class Recipe(models.Model):
    object = RandomManager()
    recipe_chef = models.CharField(max_length=100)
    recipe_name = models.CharField(max_length=100)
    recipe_info = models.TextField()
    recipe_time = models.IntegerField(null=True)
    recipe_equipment = models.CharField(max_length=150)
    recipe_fat = models.IntegerField(null=True)
    recipe_ingredient = models.TextField()
    recipe_method = models.TextField()
    recipe_image_1 = models.ImageField(upload_to='recipe_image/', blank=True)
    recipe_image_2 = models.ImageField(upload_to='recipe_image/', blank=True)
    recipe_image_3 = models.ImageField(upload_to='recipe_image/', blank=True)
    recipe_image_4 = models.ImageField(upload_to='recipe_image/', blank=True)
    category_tags = models.ManyToManyField(Category, related_name="categories")
    time_tags = models.ManyToManyField(CookTime, related_name='cook_times', blank=True)
    equipment_tags = models.ManyToManyField(Equipment, related_name='equipments', blank=True)
    allergies_tags = models.ManyToManyField(Allergies, related_name='allergiess', blank=True)

    def __str__(self):
        return f"Chef: {self.recipe_chef}, Food: {self.recipe_name}"

    def get_recipe_image_1(self):
        return self.recipe_image_1

    def get_recipe_image_2(self):
        return self.recipe_image_2

    def get_recipe_image_3(self):
        return self.recipe_image_3

    def get_recipe_image_4(self):
        return self.recipe_image_4

    def get_all_recipe_image(self):
        all_image = [self.recipe_image_2, self.recipe_image_3, self.recipe_image_4]
        useful_image = []
        for i in all_image:
            if i != '':
                useful_image.append(i)
        return useful_image

    def get_recipe_chef(self):
        return self.recipe_chef

    def get_recipe_name(self):
        return self.recipe_name

    def get_recipe_info(self):
        return self.recipe_info

    def get_recipe_time(self):
        return self.recipe_time

    def get_recipe_equipment(self):
        return self.recipe_equipment.upper()

    def get_recipe_fat(self):
        return self.recipe_fat

    def get_recipe_ingredient(self):
        ingredients = self.recipe_ingredient.split("||")
        ingredient = []
        for i in ingredients:
            splitter = i.split(":")
            ingredient.append(Ingredient(splitter[0], splitter[1]))
        return ingredient

    def get_recipe_method(self):
        return self.recipe_method

    def get_recipe_method_list(self):
        return self.recipe_method.split("||")


class Ingredient:

    def __init__(self, amount, detail):
        self.amount = amount
        self.detail = detail

    def get_detail(self):
        return self.detail

    def get_amount(self):
        return self.amount
