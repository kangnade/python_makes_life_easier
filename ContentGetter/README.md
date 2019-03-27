# Project Title

This project allows user to store information via Python program. Using cmd to run "runContentGetter.py" and it allows the user to add,
get, or delete keys and items that are encrypted in a json file.

## Getting Started



### Prerequisites

You need Python and Required libraries to run it.

```
cryptography, json, pathlib, etc.
```

### Installing

No installation. Please manually download the file and give it a try.

```
N/A
```

And repeat

```
N/A
```

End with an example of getting some data out of the system or using it for a little demo

## Cmd running sample

'''
C:\Users\username\Desktop\randomprojects\ContentGetter>python runContentGetter.py

    Welcome, you are using the ContentGetter. Though ContentGetter
    uses Python Cryptography to encrypt your saved information, please
    do not use it to store important passwords on sites such as Bank
    , Amazon, Facebook, or Instagram where Hackers could be a potential
    threat.

    It's fine to use it to store information with your CV, if you are
    copying and pasting all the time to fill out only application, this
    could make your life easier!

`Press Y/y to continue; press any key to quit`
`Are you going to use the ContentGetter?> y`
Please enter file path (up to folder level); q to quit:> C:/Users/username/Desktop/randomprojects
Please enter the file name (e.g. xyz.json): keys.json
Would you like to (add), (get), (del) content?> (Press any key to quit):> add
Please enter the account name:> youtube
Please enter the content:> youtubepassword
Would you like to (add), (get), (del) content?> (Press any key to quit):> add
Please enter the account name:> facebook
Please enter the content:> facebookpassword
Would you like to (add), (get), (del) content?> (Press any key to quit):> add
Please enter the account name:> twitter
Please enter the content:> twitterpassword
Would you like to (add), (get), (del) content?> (Press any key to quit):> add
Please enter the account name:> instagram
Please enter the content:> inspassword
Would you like to (add), (get), (del) content?> (Press any key to quit):> get
Please enter the account name:> twitter
Information copied, please paste on your browser.
Would you like to (add), (get), (del) content?> (Press any key to quit):> del
Please enter the account name:> facebook
C:\Users\username\Desktop\randomprojects\keys.json
Would you like to (add), (get), (del) content?> (Press any key to quit):> get
Please enter the account name:> facebook
There is no such KEY in the file
Would you like to (add), (get), (del) content?> (Press any key to quit):>
'''

## Deployment

Add additional notes about how to deploy this on a live system


## Authors

* **Nade Kang** - *Initial work* - [nadekang](https://github.com/kangnade)

See also the list of [contributors](https://github.com/kangnade/python_makes_life_easier/graphs/contributors) who participated in this project.
