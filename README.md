# DGAPI
<img src="/images/icon.png" alt="Icon for DGAPI">

## This a free Data API, to get  up to 50 000 random generated data such as:

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

<p align="center"><a href="http://mohamadnaseralnakshbandi.pythonanywhere.com/">http://mohamadnaseralnakshbandi.pythonanywhere.com/</a></p>

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

 <p align="center"><a href="http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=X">http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=X</a></p>

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
<hr>

# Make an API request in JS , Python and Java

<p> Use Javascript to get 3 Data set</p>

``` Javascript
const axios = require('axios');
axios
  .get('http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=3')
  .then(res => {
    console.log(res);
  })
  .catch(error => {
    console.error(error);
  });
````

<p> Use python to get 20 Data set</p>

```` Python
import requests
response = requests.get("http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=20")
print(response.text)
````
</hr>


<p> Use it with Java to get 1000 Data set</p>

```` Java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.*;
import java.util.ArrayList;

public class APIResquest {
    public static void main(String[] args) {
        APIResquest request = new APIResquest();
        request.SendRequst("http://mohamadnaseralnakshbandi.pythonanywhere.com/data/?number=1000");
    }
    ArrayList<String> responses = new ArrayList<String>();
    public  void SendRequst(String linkname) {
        try {
            URL url = new URL(linkname);
            HttpURLConnection httpURLConnection = (HttpURLConnection)url.openConnection();
            httpURLConnection.setRequestMethod("GET");
            String line ;
            InputStreamReader inputStreamReader = new InputStreamReader(httpURLConnection.getInputStream());
            BufferedReader reader = new BufferedReader(inputStreamReader);

            while ((line = reader.readLine()) != null) {
                responses.add(line + "\n");
            }
            reader.close();

        } catch (Exception e) {
            System.err.println(e.toString());
        }
        responses.forEach(response ->{
            System.out.println(response);
        });
    }
}
````
</hr>

# Make an API request using Talend open Studio

<p> Make the Talend Job</p>

<img src="/images/Talend.PNG" alt="Image for Talend Job">

<p> The configutation of TRest Component: </p>

<img src="/images/TRest.PNG" alt="Image for TRest">

<p> The configutation of TExtractJSONField Component:</p>

<img src="/images/TExtractJSONField.PNG" alt="Image for TExtractJSONField">

<p> The Result:</p>

<img src="/images/Console.PNG" alt="Image for Talend Job Resutlt">

</hr>

## Visit my Github: 
<a href="https://www.github.com/Mohmad-Naser-alnakeshbandi" target="_blank" rel="noreferrer">Mohamad Naser Alankeshbandi </a>