# Databricks notebook source
print("hello world edit vscode")

# COMMAND ----------

!pip install httpx

# COMMAND ----------

import httpx

# COMMAND ----------

dbutils.widgets.text("name", "default_name", "Enter your name:")
