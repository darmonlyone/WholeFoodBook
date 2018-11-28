from django.shortcuts import render
from random import randint
from django.views import generic
from cookbook.models import Recipe


class ProfileView(generic.ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        return None


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
        return context


class LoginView(generic.ListView):
    template_name = 'login.html'

    def get_queryset(self):
        return None


class IndexView(generic.ListView):
    template_name = 'display.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_all = Recipe.objects.all()
        if recipe_all.count() > 8:
            random_int = randint(0, recipe_all.all().count() - 9)
            context['recipe_suggest'] = recipe_all[random_int:random_int + 8]
        else:
            context['recipe_suggest'] = recipe_all
        context['recipe_show'] = recipe_all
        return context

class AddRecipeView(generic.ListView):
    template_name = 'add_recipe.html'
    
    def get_queryset(self):
        return None

# def test(request):
#     entry_list = list(Recipe.objects.all())
#     for i in entry_list:
#         print(i.get_recipe_name())

# def fake_put_db(request):
#
# r = Recipe(recipe_chef="Wan", recipe_name="Chicken Breast",
#            recipe_info="Pumpkin Pie? Pudding shots? Obviously the two belong together! Fireball adds some more cinnamon flavor to the shots but you can sub with all vodka if you prefer. ",
#            recipe_time=80,
#            recipe_type="Grill",
#            recipe_fat=450,
#            recipe_ingredient="2 x 400g:packets Lilydale Breast Strips||8:kipfler potatoes, washed, cut into 1cm thick rounds||1:tablespoon olive oil||100g:cup macadamia nuts||1/2:garlic clove, chopped||1:tablespoon water||1:baby beans, ends trimmed, blanched",
#            recipe_method="Preheat oven to 200°C or 180°C fan. Line two baking trays with baking paper. Lay Lilydale breast strips on one of the prepared trays and bake according to packet instructions||Place potatoes onto the other prepared tray in a single layer. Drizzle with oil and season well. Bake for 25-30 minutes, until golden and tender||Meanwhile, make pesto. Place watercress, macadamias and garlic in a small food processor. Pulse until chopped. Add extra virgin olive oil, lemon juice and water. Process until a paste forms. Transfer hot potatoes to a bowl, add half of the pesto and stir to coat")
# r.save()

# heroku pg:psql
# \d
# SELECT * FROM cookbook_recipe;
# Recipe.objects.get(id=1).delete()
