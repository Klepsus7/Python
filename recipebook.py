class Recipe:
    def __init__(self, name, num_ingredients, ingredients, prep_time, cook_time, calories, instructions):
        self.name = name
        self.num_ingredients = num_ingredients
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.calories = calories 
        self.instructions = instructions
    # Describe each Recipe
    def __repr__(self):
        return f"This recipe is {self.name}, it needs {self.num_ingredients} ingredients totaling {self.calories} calories with a preparation time of {self.prep_time} minutes and a cooking time of {self.cook_time} minutes."
    # Total Recipe Making time
    def total_cook_time(self):
        total_time = self.cook_time + self.prep_time
        return (f"The total making time for this Recipe is {total_time}")
        
# Instructions and Ingredients of each recipe 
recipe_1_instructions = """
  \n1-Prep: Bring a large pot of salted water to a boil. Wash and drie produce. 
  Remove and discard any large stems from kale; roughly chop leaves.
  Peel and mince or grade garlic.
  Pat chicken dry with paper towels; season all over with salt, peper, and half the Tuscan Heat Spice (all for 4 servings).
  \n2-Cook Pasta: Once water is boiling, add spaghetti to pot. 
  Cook until al dente, 9-11 minutes. Reserve 1/2 cup pasta cooking water then drain.
  \n3-Cook Kale: While pasta cooks, heat a drizzle of olive oilin a large pan over medium-high heat. 
  Add kale and a splash of water. 
  Cook until kale is wilted and very tender, 5-7 minutes. Tip: if necessary cook kale in batches. 
  Stir in garlic and cook untill fragrant, 30 seconds. Season with salt and pepper. transfer to plate. 
  \n4-Cook Chiken: Heat another drizle of olive oil in pan used for kaleover medium-high heat. 
  Add chiken and cook, stirring occasionally, until browned and cooked through, 4-6 minutes.
  \n5-Make Sauce: Return kale to pan with chicken and reduce heat to medium low. 
  Add cream sauce. Stir in cream cheese and 1/4 cup reserved pasta cooking water. 
  Bring to a simmer and cook until sauce is combined and thickened, 2-3 minutes. 
  \n6-Finish & Serve: Add drained spaghetti and 1 TBSP butter (2 TBSP for 4 servings) to pan with sauce; toss to combine. 
  Season with salt and pepper. 
  If needed, stir in more reserved pasta cooking water a splash at a time until pasta is ccoated in creamy sauce. 
  Divide pasta between bowls, top with Parmesan and serve.
  """
recipe_1_ingredients = """
  2 person / 4 person\n
  Kale: 4oz/8oz
  Garlic: 1 Clove/2 Cloves 
  Chiken Breast Strips: 10oz/20oz
  Tuscan Heat Spice: 1 TBSP
  Spaghetti: 6oz/12oz
  Cream Sauce Base: 4oz/8oz
  Cream Cheese: 2TBSP/4TBSP
  Parmesan Cheese: 1/4Cup / 1/2Cup
  """

recipe_2_instructions = """
  \n1-Cook Time: In a small pot, combine rice, 1 1/4 cups water (2 1/4 cups for 4 servings), and a pinch of salt.
  Bring to a boil, then cover and reduce to a low simmer.
  Cook until rice is tender, 15-18 minutes.
  Keep covered off heat until ready to serve.
  \n2-Prep & Mix Mayo: While rice cooks, wash and dry all produce.
  Zest and quarter lime.
  Roughly chop cilantro.
  In a small bowl, combine mayonaise with chili sauce to taste.
  \n3-Cook Pork: Heat a drizzle of oil in a large pan over medium-high heat.
  Add pork and a big pinch of salt.
  Cook, breaking up meat into pieces, until browned, 3-4 minutes.
  \n4-Finish & Serve: Fluff rice with a fork; stir in lime zest and 1 TBSP butter (2 TBSP for 4 servings).
  Season with salt and pepper.
  Divide rice between bowls and top with pork mixture and any remaining sauce from pan.
  Drizzle with chili mayo. Sprinkle with crispy fried onions and cilantro.
  Serve with lime wedges on the side.
  """
recipe_2_ingredients = """
  2 person / 4 person\n
  Jasmine Rice: 3/4 Cup / 1 1/2 Cup
  Ground Pork: 10oz/20oz
  Mayonnaise: 2TBSP/4TBSP
  Sweet Thai Chili Sauce: 1oz/2oz
  Shredded Carrots: 4oz/8oz
  Sweet Soy Glaze: 4TBSP/8TBSP
  Sesame Dressing: 1.5oz/3oz
  Crispy Fried Onions: 1/2
  Cilantro: 1/4oz
  Lime: 1
  """

recipe_3_instructions = """
  \n1-Prep: Bring a large pot of water to a boil.
  Wash and dry produce. Peel and mince garlic.
  Trim ends from zucchini.
  Using peeler, shave zucchini lenghtwise into thin ribbons, rotating as you go, until you get to the seedy core;
  discard core.
  \n2-Cook Pasta: Once water is boiling, add spaghetti to pot.
  Cook until al dente, 9-11 minutes.
  Reserve 1/2 cup pasta cooking water (1 cup for 4 servings), then drain.
  \n3-Cook Sausage: While pasta cooks, remove sausage from casing; discard casing.
  Heat a drizzle of olive oil in a large pan over medium-high heat.
  Add sausage and cook, breaking up meat into pieces, until brownes and cooked through, 4-6 minutes.
  Stir in garlic and Tuscan Heat Spice; cook until fragrant, 30 seconds.
  \n4-Simmer sauce: Add marinara to pan with sausage mixture, then reduce heat to medium.
  Simmer until flavors meld and sauce is slightly reduced, 3-4 minutes.
  \n5-Toss Pasta: Add spaghetti, 1/4 cup reserved pasta cooking water (1/2 cup for 4 servings),
  and 1 TBSP butter (2 TBSP for 4) to pan with sauce.
  Toss to throughly combine.
  Separate zucchini ribbons with your hands, then stir into pasta until slightly softened, 1-2 minutes.
  Taste and season with salt and peper.
  TIP: If needed, stir in more reserved pasta cooking water a splash at a time until spaghetti is thoroughly coated in sauce.
  \n6-Serve: Divide pasta between bowls; top with Parmesan and serve.
   """
recipe_3_ingredients = """
  2 person / 4 person\n
  Garlic: 1 clove/2 cloves
  Zucchini: 1
  Spaghetti: 6oz/12oz
  Italian Pork Sausage: 9oz/18oz                  
  Tuscan Heat Spice: 1TBSP/2TBSP
  Marinara Sauce: 14oz/28oz
  Parmesan Cheese: 1/4 Cup
  """

recipe_4_instructions = """
  \n1-Prep: Wash and dry all produce.
  Trim, peel, and cut carrot into small dice.
  Halve, peel and finely chop onion.
  Remove and discard any large stems from kale.
  Peel and thinly slice garlic.
  \n2-Cook Sausage: Heat a drizle of olive oil in a large pot over medium-high heat.
  Add sausage and cook, breaking up meat into pieces, until browned, 4-6 minutes (it'll finish cooking in the next step).
  \n3-Cook Veggies: Add a large drizzle of olive oil tp pot with sausage.
  Stir in carrot, onion, kale, and a big pinch of salt.
  Cook, stirring occasionally, until veggies are just softened and sausage is cooked through, 5-7 minutes.
  \n4-Simmer Soup: Add garlic and half the Italian Seasoning (all for 4 servings) to pot.
  Cook, stirring, until fragrant, 1 minute.
  Stir in stock concentrates and 3 1/2 cups warm water (6 cups for 4), scraping up any browned bits from bottom of pot.
  Add half the couscous (all for 4), then cover and bring to a boil.
  Once boiling, immediately reduce heat to a low.
  Simmer until couscous is al dente, 7-9 minutes.
  \n5-Make Garlic Toasts: Meanwhile, halve and toast ciabatta.
  Spread garlic herb butter onto cut sides, then slice each half on a diagonal to break triangles.
  \n6-Finish & Serve: Stir half the Parmesan into soup until melted.
  Season with plenty of salt and pepper.
  Divide soup between bowls and sprinkle with remaining Parmesan.
  Serve with garlic toasts on the side.
  """
recipe_4_ingredients = """

  2 person / 4 person\n
  Carrot: 3oz/6oz
  Yellow Onion: 1
  Kale: 4oz
  Garlic: 1 clove/2 cloves
  Italian Chiken Sausage Mix: 9oz/18oz
  Italian Seasoning: 1 TBSP
  Chicken Stock Concentrate: 2/4
  Israeli Couscous: 2.5oz
  Ciabata Bread: 1 / 2
  Garlic Herb Butter: 2TBSP/4TBSP
  Parmesan Cheese: 1/4 Cup / 1/2 Cup
  """

# Creating the Recipe objects below
recipe_1 = Recipe("Tuscan Trattoria Chiken & Kale Spaguetti", 8, recipe_1_ingredients, 5, 25, 850, recipe_1_instructions)
recipe_2 = Recipe("Sesame Soy Pork Bowl", 10, recipe_2_ingredients, 5, 20, 1070, recipe_2_instructions)
recipe_3 = Recipe("Pork Sausage Spaghetti Bolognese", 7, recipe_3_ingredients, 5, 25, 830, recipe_3_instructions)
recipe_4 = Recipe("Chicken Sausage, Couscous & Kale Soup", 11, recipe_4_ingredients, 10, 35, 760, recipe_4_instructions)

# Start of Program
welcome = ("""\nWelcome to the Recipe Book, we currently count with the following recipes:\n
    1 - Tuscan Trattoria Chiken & Kale Spaghetti. 
    2 - Sesame Soy Pork Bowl.
    3 - Pork Sausage Spaghetti Bolognese.
    4 - Chicken Sausage, Couscous & Kale Soup
      """)
# print(welcome)
while True:
    print(welcome)
    choice = input("What recipe would you like to make today? Type number and press Enter, to Exit type \"0\" and Enter: ")
    if choice == "1":
        print("\n", recipe_1.__repr__(), "\n", "\nIngredients:\n",recipe_1.ingredients, "\nInstructions:", recipe_1.instructions)
    elif choice == "2":
        print("\n", recipe_2.__repr__(), "\n", "\nIngredients:\n",recipe_2.ingredients, "\nInstructions:", recipe_2.instructions)
    elif choice == "3":
        print("\n", recipe_3.__repr__(), "\n", "\nIngredients:\n",recipe_3.ingredients, "\nInstructions:", recipe_3.instructions)
    elif choice == "4":
        print("\n", recipe_4.__repr__(), "\n", "\nIngredients:\n",recipe_4.ingredients, "\nInstructions:", recipe_4.instructions)
    elif choice == "0":
        break
    else:
        continue