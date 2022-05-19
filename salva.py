import pyttsx3 as p
from pyttsx3 import engine
from selenium import webdriver

import randfacts

salva=p.init()
voices=salva.getProperty("voices")
salva.setProperty("rate",120)
salva.setProperty("voice",voices[1].id)

salva.say(f"""
              Null is a special data type which can have only one value: NULL. The special NULL value is used to represent
empty variables in PHP. A variable of type NULL is a variable without any data.
Tip: If a variable is created without a value, it is automatically assigned a value of NULL.Variables can also be
emptied by setting the value to NULL
 
 PHP Resource
Resources are not the exact data type in PHP. Basically, these are used to store some function calls or
references to external PHP resources. For example - a database call. It is an external resource.
This is an advanced topic of PHP, so we will discuss it later in detail with examples.""") 
salva.runAndWait()
