from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F

def teste_um():
    spark = SparkSession.builder.appName('firstSeesion')\
        .config("spark.master","local") \
        .config("spark.executor.memory","1gb") \
        .config("spark.shuffle.sql.partitions", 1) \
        .getOrCreate()


    #df = spark.read.json("C:\scripts\EMA_definition.json")
    # # Define custom schema
    # schema = StructType([
    #       StructField("name",StringType()),
    #       StructField("questions",FloatType()),
    #       StructField("options",StringType()),
    #       StructField("question_id",StringType()),
    #       StructField("question_text",StringType()),
    # ])

    # df_with_schema = spark.read.schema(schema) \
    #     .json("C:\scripts\Trabalhofinal\EMA_definition.json")
    # df_with_schema.printSchema()
    # df_with_schema.show() 

    df = spark.read.option("multiline","true").json("C:\scripts\EMA_definition.json")


    #dicionario = df.toJSON()
    #dicionario = df.toPandas()
    #dicionario = df[1].getItem('questions')
    #x = df['questions']
   
    df.show()

    input('ok')
    #print(dicionario)
    #print(x)
def teste_dois():
    spark = SparkSession.builder\
    .master("local")\
    .appName("Teste")\
    .config("spark.jars.packages", "com.crealytics:spark-excel_2.11:0.12.2")\
    .getOrCreate()

    df = spark.read.format("com.crealytics.spark.excel")\
    .option("useHeader", "true")\
    .option("inferSchema", "true")\
    .option("dataAddress", "Details")\
    .load("c:\scripts\Medals.xlsx")

    input('o...')
    return df

df = teste_dois()

df.show(5)

def parte_tres():
    

    spark = SparkSession.builder.appName('Sessao')\
        .config("spark.master", "local") \
        .config("spark.executor.memory", "1gb") \
        .config("spark.shuffle.sql.partitions", 1) \
        .getOrCreate()

    path = 'C:/scripts/paralympics_tokyo.json'
    df_json = spark.read.option("multiline","true").json(path)
    # df_json.show(10)
    # df_json.printSchema()
    # df_json.select('sex').count() #não retorna nada, converti para Pandas:
    #converter para Dataframe do pandas
    pandasDf = df_json.toPandas()
    print(f'A tabela possui {pandasDf.shape[0]} linhas e {pandasDf.shape[1]} colunas!\n')


    path = 'C:/scripts/Paralympics_tokyo_21.csv'
    df_csv = spark.read.load(path, format = 'csv', sep = ',', inferschema = 'true', header = 'true')
    # df_csv.show()
    # df_csv.printSchema()
    df_csv.select('rank').count()

    #=================================NÚMERO DE LINHAS DIFERENTES ENTRE O CSV E O JSON, JOIN INPOSSÍVEL==========================

    print(pandasDf['rank'].value_counts()) #927 valores únicos, muitos arrays

    # df_json = df.drop('name')
    # df_csv = df_csv.select('medal', 'name', 'rank')

    # df_json.show()
    # df_csv.show()

    # df_join = df_json.join(df_csv,df_json['rank'] ==  df_csv['rank'])
    # df_join.show(20)

    # df_join = df_join.toDF(*['Age', 'Nacionalidade', 'Sexo', 'Esporte', 'Seleção', 'Medalha', 'Nome'])
    # df_join.printSchema()

    # def colunaTipo(dataframe, nomes, novoTipo):
    #     for nome in nomes:
    #         dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    #     return dataframe

    # colunaI = ['Age']

    # df_join = colunaTipo(df_join, colunaI, IntegerType())

    # df_join.show(10)
    # df_join.printSchema()

    # df_join = df_join.groupby('E')
    # Validar os dados
    # import pyspark.sql.functions as F
    # df = df.withColumn("data_type", F.lit(df.schema["Frequency"].dataType))
    # df = df.withcolumn('typ_freq',F.when(F.col("data_type") != dic["Frequency"], False).otherwise('true')