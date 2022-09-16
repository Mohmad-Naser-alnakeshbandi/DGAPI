# DGAPI
## This a free Data API, to get random data such as:

<ul>
<li> First name </li>
<li> Second name </li>
<li> E-Mail </li>
<li> Age </li>
<li> Salary </li>
</ul>
 
<hr>

# How to use it?
<p>To get one data set just visit the following link: </p>
<br>
 <a href="http://mohamadnaseralnakshbandi.pythonanywhere.com/">http://mohamadnaseralnakshbandi.pythonanywhere.com/</a>
<br>
<p>The response is</p>
```` json
{
  "Age": 46,
  "EMail": "LeonardAlsop@gmail.com",
  "First_Name": "Leonard",
  "ID": "05jYhqf0pNkkEb9XShU0PWYD",
  "Salary": "3521€",
  "Second_Name": "Alsop"
}
````
<hr>
<p>To get more than one data set just visit the following link: </p>
<br>
 <a href="http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=X">http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=X</a>
<br>
<p>The response is, by replacing X with the number 5</p>
```` json
[
  {
    "Age": 63,
    "EMail": "IanDavidson@gmail.com",
    "First_Name": "Ian",
    "ID": "000FNxtP1pq7IXAY301fAkBl",
    "Salary": "2944€",
    "Second_Name": "Davidson"
  },
  {
    "Age": 26,
    "EMail": "CarlNewman@gmail.com",
    "First_Name": "Carl",
    "ID": "000LZLSi8V05IFhzBXUCTG9a",
    "Salary": "3603€",
    "Second_Name": "Newman"
  },
  {
    "Age": 59,
    "EMail": "DanDuncan@gmail.com",
    "First_Name": "Dan",
    "ID": "000qcg88Ms8622MNZZnYXuCV",
    "Salary": "4312€",
    "Second_Name": "Duncan"
  },
  {
    "Age": 32,
    "EMail": "ConnorSlater@gmail.com",
    "First_Name": "Connor",
    "ID": "000r3h8QETtrnZVuIJ21WLsu",
    "Salary": "2831€",
    "Second_Name": "Slater"
  },
  {
    "Age": 13,
    "EMail": "NathanLangdon@gmail.com",
    "First_Name": "Nathan",
    "ID": "000zH4mwXl0Uu6pq3tX8wdl9",
    "Salary": "2557€",
    "Second_Name": "Langdon"
  }
]
````