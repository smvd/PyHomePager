# PyHomePager
PyHomePager is a python script that can generate custom homepages based on theme templates.

## Using a template
Using a template is very simple.
First you want to coppy the template configuration to the root of the project.

`cp templates/{the theme you want to use}/config.ini .`

Now you can edit config.ini to style the template to your liking.
The config file has a nice upgrade over a normal `.ini` file, it supports variables.
You can define a variable as `-{variable name} = {value}` and then reference it in the rest of the config as `-{variable name}`.
Keep in mind the config file is parsed line by line so you need to make shure you define your variables above where you use them.
The accepted values are based on CSS so they also accept all possible css values for that property.

## Making a template
Making a template is a bit more complex then using one.
I recommend copying a existing template and edditing it unitl it does what you want.
The template consists of 2 files, one for the main template and one for each entry.
You can also add custom key value pairs to the templates configuration.
All you need to do is add `${the key you want to add}$` in the template and then add `{the key you want to add} = {the value}` in the configuration file.
Outside of that its just HTML, CSS and javascript, so do whatever you want with your template.
Also please make a PR if you have you really like so i can add it to the repo.
