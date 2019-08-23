Question: How long did you spend on the coding test below? What would you add to your solution if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.

#Answer: I spent 120 hours on the coding test. IF I had more time I would ad front end tests and add more responsive features to the application, because the application is not currently responsive on all pages.


Question: What was the most useful feature that was added to the latest version of your chosen language? Please include a snippet of code that shows how you've used it.

#Answer: The breakpoint() Built-In feature in python 3.7

code snippet
PYTHONBREAKPOINT=0
 def update(self,  instance, validated_data):
        breakpoint()
        ranking = validated_data.get('ranking', instance.ramking)
        category = validated_data.get('category', instance.category)
        rankings_queryset = FavoriteThing.objects.order_by('ranking').filter(category=category)
        existing_ranking = rankings_queryset.filter(ranking=ranking)
        
 
in the above snippet I am trying to debugthe update function inorder to get what is returned in instance, I made use of the newly added built in breakpoint(), which is both a cleaner syntax and even customizable. As seen above, I set the pythonbreakpoint to 0 inorder to ignore the break point when I run it a second time after supposedly solving the bug.

Question: How would you track down a performance issue in production? Have you ever had to do this?

#Answer: 
I will do a performance monitoring. I will do this by identifying how long it takes to complete a request and how long it takes to render a page. An example of a tool used for django app production monitoring is DJANGO-HEALTH-CHECK, it runs perfomance checks on production using database, queue server, celery processes amongst other. I will also ensure i have unit tests and measure how long it takes to perform each unit test.

Yes I have.
