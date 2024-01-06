<h1>Convert HTML AWR report to Excel file for Visualization using Python Language</h1>

<h2>Output of execution of this repo code would look like this.
<h3>Before executing the code, <span style="color: blue;">example Oracle AWR report looks like these</span></h3>


![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/awr1.jpg?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/awr2.jpg?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/awr3.png?raw=true)

<h3>Aftere executing the code, example Oracle AWR repor look like thse</h3>

![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/intro.jpg?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/orderbyelapsed.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/sgaadvisory.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/orderbyio.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/orderbygets.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/orderbyPreads.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/orderbycpu.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/ioprofile.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/fore.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/addmpie.png?raw=true)
![alt text](https://github.com/chakratechgeek/oracleHTMLVisualization/blob/main/images/addmbar.png?raw=true)

<h2>Interested??? Continue reading to make use of these codes</h2>
<h3>Why we need this tool?</h3>
<ul>
  <li>~95% of Oracle database's Performance and Tuning (PT) DBA's primary role is to review AWR reports.</li>
  <li>~50% of time, in live monitoring, we rely on ASH and AWR reports.</li>
  <li>Easy to convey to your clients during root cause analysis and critical performance issues.</li>
  <li>AWR reports are huge in size and ~99%, DBA has to read numbers in the reports and infer the analysis based on it. Most of the information in the AWR report are not really needed for analysis; due to its size and reading numbers in the report, these are things can happen</li>
  <ul>
    <li>specialized DBA skillset is needed</li>
    <li>Lots of chances for human errors or oversight</li>
    <li>Skilled DBA has to spend lots of time.</li>
  </ul>
</ul>

<p>This tool is developed using Python language. This tool prompts for entering AWR report to be analyzed and visualized. These are steps to follow to make use of this tool and it has to be developed further adding all important sections of the AWR report to excel sheet,
Let's start!!!</p>

<h2>Prerequisites: </h2>
<ul>
  <li>Basic programming knowledge on Python language.</li>
  <li>Basic understanding of OOPS concepts.</li>
  <li>Basic understanding of pandas library</li>
</ul>

<h2> Step 1:</h2>
<p>Use this link to download and install Python 3.7.6 version on Windows 10, 64bit OS. https://www.python.org/downloads/</p>

<h2> Step 2:</h2>
<p>Install these libraries. I used 'pip' command to install. </p>
<p>Example: Follow this to install pandas library.</p>

```
start program --> command prompt -->
python -m pip install pandas
python -m pip install matplotlib
python -m pip install BeautifulSoup
python -m pip install pandas 
python -m pip install xlsxwriter
python -m pip install openpyxl
```
<h2>Step 3:</h2>
<p>Copy and save these Python class codes into their respective files in a directory in local machine on which you want to execute.</p>

```
File 1: main.py
File 2: env.py
File 3: addmevent.py
File 4: ioprofile.py
File 5: sqlstats.py
File 6: sgatarget.py

```

<h1>Now, output.xlsx file will be generated on the location where you have executed the python script. 

Enjoy!!!!!
</h1>
