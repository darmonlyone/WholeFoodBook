from random import randint

from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from cookbook.forms import UserAliasForm
from cookbook.models import Recipe, AuthorUser, UserAlias, Category


class ProfileView(generic.ListView):
    template_name = 'profile.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_user'] = AuthorUser.objects.all()
        context['recipe_all'] = Recipe.objects.all()
        context['author_alias'] = UserAlias.objects.all()
        return context


class WelcomeView(generic.ListView):
    template_name = 'welcome.html'

    def get_queryset(self):
        return None


class MenuView(generic.ListView):
    template_name = 'menu.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_name = self.kwargs['recipe_name']
        recipe_all = Recipe.objects.all()
        if recipe_all.count() > 8:
            random_int = randint(0, recipe_all.all().count() - 9)
            context['recipe_suggest'] = recipe_all[random_int:random_int + 8]
        else:
            context['recipe_suggest'] = recipe_all
        context['recipe_enable'] = recipe_all.filter(recipe_name=recipe_name)
        context['author_user'] = AuthorUser.objects.all()
        context['recipe_all'] = Recipe.objects.all()
        return context


class LoginView(generic.ListView):
    template_name = 'login.html'

    def get_queryset(self):
        return None


class IndexView(generic.ListView):
    template_name = 'display.html'
    model = Recipe

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_all = Recipe.objects.all()
        if recipe_all.count() > 8:
            random_int = randint(0, recipe_all.all().count() - 9)
            context['recipe_suggest'] = recipe_all[random_int:random_int + 8]
        else:
            context['recipe_suggest'] = recipe_all
        context['recipe_all'] = recipe_all
        context['recipe_appetizer'] = recipe_all.filter(category_tags__food_category='appetizer')
        context['recipe_main'] = recipe_all.filter(category_tags__food_category='main dish')
        context['recipe_soup'] = recipe_all.filter(category_tags__food_category='soup and stew')
        context['recipe_dessert'] = recipe_all.filter(category_tags__food_category='dessert')
        context['recipe_drink'] = recipe_all.filter(category_tags__food_category='drink')
        context['recipe_salad'] = recipe_all.filter(category_tags__food_category='salad')
        return context


class AddRecipeView(generic.ListView):
    template_name = 'add_recipe.html'
    model = AuthorUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_user'] = AuthorUser.objects.all()
        context['author_alias'] = UserAlias.objects.all()
        context['recipe_all'] = Recipe.objects.all()
        return context


class SearchView(generic.ListView):
    template_name = 'searcher.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_search = self.kwargs['recipe_search']
        recipe_all = Recipe.objects.all()
        if recipe_all.count() > 8:
            random_int = randint(0, recipe_all.all().count() - 9)
            context['recipe_suggest'] = recipe_all[random_int:random_int + 8]
        else:
            context['recipe_suggest'] = recipe_all
        context['recipe_all'] = recipe_all
        context['recipe_recipe_search'] = recipe_all.filter(recipe_name__contains=recipe_search)
        context['recipe_chef_search'] = recipe_all.filter(recipe_chef__contains=recipe_search)
        context['recipe_category_search'] = recipe_all.filter(category_tags__food_category__contains=recipe_search)
        context['recipe_time_search'] = recipe_all.filter(time_tags__cooking_time__contains=recipe_search)
        context['recipe_equipment_search'] = recipe_all.filter(
            equipment_tags__equipment_required__contains=recipe_search)
        context['recipe_allergies_search'] = recipe_all.filter(
            allergies_tags__allergies_ingredient__contains=recipe_search)
        context['recipe_search'] = recipe_search
        return context


def search(request):
    searcher = request.POST.get('search_recipe', '')
    return HttpResponseRedirect(reverse("cookbook:search", args=[searcher]))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect(reverse("cookbook:index"))


def userAliasPost(request):
    if request.method == 'POST':
        form = UserAliasForm(request.POST)
        if not form.is_valid():
            user_name = request.POST.get('user_name', '')
            alias = request.POST.get('alias_name', '')
            older_alias = UserAlias.objects.filter(user_username__exact=user_name)
            older_alias.delete()
            new_alias_model = UserAlias(user_username=user_name, alias_name=alias)
            new_alias_model.save()
            return HttpResponseRedirect(reverse("cookbook:profile"))
        raise Http404


class DeleteRecipeView(generic.ListView):
    def post(self, request, *args, **kwargs):
        delete_recipe = request.POST.get('deleted_recipe', '')
        user_name = request.POST.get('user_name', '')
        delete_recipe_model = Recipe.objects.get(recipe_name__exact=delete_recipe)
        delete_recipe_model.delete()
        author_recipe = AuthorUser.objects.get(recipe_name__exact=delete_recipe, user_username__exact=user_name)
        author_recipe.delete()
        return HttpResponseRedirect(reverse("cookbook:profile"))


class EditRecipeView(generic.ListView):
    template_name = 'add_recipe.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_name = self.kwargs['recipe_name']
        context['recipe'] = Recipe.objects.get(recipe_name__exact=recipe_name)
        context['author_user'] = AuthorUser.objects.all()
        context['author_alias'] = UserAlias.objects.all()
        context['recipe_all'] = Recipe.objects.all()
        context['edit'] = 'edit'
        return context


def update_recipe(request):
    if request.method == 'POST':
        old_recipe = request.POST.get('old_recipe', '')
        recipe_name = request.POST.get('name_input', '')
        recipe_info = request.POST.get('info_input', '')
        recipe_chef = request.POST.get('chef_input', '')
        username = request.POST.get('username_input', '')
        recipe_time = int(request.POST.get('time_input', ''))
        recipe_equipment = request.POST.get('equipment_input', '')
        recipe_fat = int(request.POST.get('fat_input', ''))

        measurement_list = request.POST.getlist('text_measurement')
        ingredient_list = request.POST.getlist('text_ingredient')

        recipe_ingredient = ""
        for i in range(len(measurement_list) - 1):
            recipe_ingredient += measurement_list[i] + ":" + ingredient_list[i]
            recipe_ingredient += "||"
        recipe_ingredient += measurement_list[len(measurement_list) - 1] + ":" + ingredient_list[
            len(ingredient_list) - 1]

        recipe_method = "||".join(request.POST.getlist("text_direction"))

        recipe = Recipe(recipe_name=recipe_name, recipe_chef=recipe_chef, recipe_info=recipe_info,
                        recipe_time=recipe_time, recipe_equipment=recipe_equipment, recipe_fat=recipe_fat,
                        recipe_ingredient=recipe_ingredient, recipe_method=recipe_method)

        recipe_image_1 = request.FILES.get('image1', '')
        recipe_image_2 = request.FILES.get('image2', '')
        recipe_image_3 = request.FILES.get('image3', '')
        recipe_image_4 = request.FILES.get('image4', '')

        if recipe_image_1:
            recipe.recipe_image_1 = recipe_image_1
        if recipe_image_2:
            recipe.recipe_image_2 = recipe_image_2
        if recipe_image_3:
            recipe.recipe_image_3 = recipe_image_3
        if recipe_image_4:
            recipe.recipe_image_4 = recipe_image_4

        if old_recipe:
            delete_recipe = Recipe.objects.get(recipe_name__exact=old_recipe)
            if delete_recipe:
                delete_recipe.delete()

            delete_author = AuthorUser.objects.get(recipe_name__exact=old_recipe, user_username__exact=username)
            if delete_author:
                delete_author.delete()

        recipe.save()

        author = AuthorUser(user_username=username, recipe_name=recipe_name)
        author.save()

        category_list = request.POST.getlist('check_category')
        for category in category_list:
            recipe.category_tags.add(category)

        time_list = request.POST.getlist('check_time')
        for time in time_list:
            recipe.time_tags.add(time)

        equipment_list = request.POST.getlist('check_equipment')
        for equipment in equipment_list:
            recipe.equipment_tags.add(equipment)

        allergies_list = request.POST.getlist('check_allergies')
        for allergies in allergies_list:
            recipe.allergies_tags.add(allergies)

        return HttpResponseRedirect(reverse("cookbook:profile"))
    raise Http404

# def test(request):
#     entry_list = list(Recipe.objects.all())
#     for i in entry_list:
#         print(i.get_recipe_name())

# def fake_put_db(request):
#
# r = Recipe(recipe_chef="Wan", recipe_name="Chicken Breast", recipe_info="Pumpkin Pie? Pudding shots? Obviously the
# two belong together! Fireball adds some more cinnamon flavor to the shots but you can sub with all vodka if you
# prefer. ", recipe_time=80, recipe_type="Grill", recipe_fat=450, recipe_ingredient="2 x 400g:packets Lilydale Breast
#  Strips||8:kipfler potatoes, washed, cut into 1cm thick rounds||1:tablespoon olive oil||100g:cup macadamia
# nuts||1/2:garlic clove, chopped||1:tablespoon water||1:baby beans, ends trimmed, blanched", recipe_method="Preheat
# oven to 200°C or 180°C fan. Line two baking trays with baking paper. Lay Lilydale breast strips on one of the
# prepared trays and bake according to packet instructions||Place potatoes onto the other prepared tray in a single
# layer. Drizzle with oil and season well. Bake for 25-30 minutes, until golden and tender||Meanwhile, make pesto.
# Place watercress, macadamias and garlic in a small food processor. Pulse until chopped. Add extra virgin olive oil,
#  lemon juice and water. Process until a paste forms. Transfer hot potatoes to a bowl, add half of the pesto and
# stir to coat")
# r.save()

# heroku pg:psql
# \d
# SELECT * FROM cookbook_recipe;
# Recipe.objects.get(id=1).delete()
