## SQL

For the following two data requests, **build** and **show** SQL queries and **explain your reasoning**. A person unfamiliar with the data request should be able to understand the query. If you find a query cannot be done, **explain** how you come to the conclusion.

**Explain how you validate your intermediate and final results.**

1. We want to list the names and gold medal count of all athletes with three or more gold medals over all games, starting with the ones with the most gold medals.
2. For each region, we want to show the region average of the second tallest athlete of each country over all games.

<aside>
👉 **The dataset is contained in this SQLite database file:**

[wunderflats_case_study.db](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8a971388-b482-421d-858d-9887a9e0c54b/wunderflats_test.db)

**You don’t need to provide the query result.**

</aside>

## Python

💬 *The following piece of code is currently running in Production, but it does fail from time to time for unknown reasons. It is scheduled via cronjob on a virtual machine. Eventually, you will have to hand it over to a colleague…*

❓What would you change about the code and its context given the time and resources? Feel free to go wild, but at least one solution has to show Python code written by you.
****

🔮 **As a result, we would like to see your Python code as you would commit it to a VCS.**
In addition, we want to know your **assumptions** and your **thoughts** on **what’s good and bad** about the original situation.

🤓 **Explain the considerations, compromises, and new context of your solution(s).**

```python
import google.cloud.bigquery as bq

fh = open('myfile.csv')
fc = fh.read()

data = [l.split(",") for l in fc.split('\n')]

data = [{data[0][k]: v for k, v in enumerate(l)} for l in data[1:]]

c = bq.Client()
t = c.get_table("myproject.mydataset.mytable")
e = c.insert_rows(t, data)
```