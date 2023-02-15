# Test CSS with Selenium and Python

You can test your CSS (computed styles) and the user interactions, thanks to Selenium. This tool is good for *integration tests*. It is a example, for the people who were asking.

The main file here is `itest.py`.


## Virtual env

I show an example about virtual environment in Linux. If you use other OS, please see more details in this site:

[https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

### Create your virtual env

In the project directory, you can run:

```
python -m venv env
```

The directory named `env` will be created, being an isolated environment with its own dependencies.

### Start the virtual env

When you need to start the virtual environment, you use the next command:

```
source env/bin/activate
```

## The dependencies

Do it from your virtual env.

You can install the dependencies using this command:

```
pip install selenium webdriver-manager
```

You can find the usual file, `requirements.txt`, in root folder.


## The website

Your website don't need to be in any specific folder. It will be accessed from the server, for example, `http://localhost:3000/`. In my example, it's in the folder **fake_website**.

You need to serve the site, before starting. For example, `npm start` or `npm run dev`.


## Script to start the test

You should start the virtual env (if it's not started) and use this command:

```
python itest.py
```

### Other way

In the folder `fake_website`, you can use the next command (only in this example):

```
npm run itest
```

You can see the complete command in `fake_website/package.json`, under the section **scripts**. If you want use it in other projects, pay attention to paths.


## The webdriver

The webdriver is what allows your browser to become a code-driven puppet and Selenium would be the puppet master. I used Firefox Webdriver, but you can use another webdriver. You can find the tutorial for webdriver installation here:

[https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

And the codes for different browsers are here:

[https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/test_install_drivers.py#L15-L17](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/test_install_drivers.py#L15-L17)

Youd should install the browser if you don't have it: the webdriver is not a replacement.

