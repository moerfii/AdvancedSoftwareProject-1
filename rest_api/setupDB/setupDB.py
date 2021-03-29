from sqlalchemy import create_engine
import psycopg2 as pg
import pandas as pd
import io



USER="ase_user"
HOST="localhost"
PORT=5432
DB_NAME="ase"
PASSWORD="aseisgreat"
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")



def createTables():
    print("Creating tables")
    conn = pg.connect(f"user={USER} dbname={DB_NAME} password={PASSWORD}")
    cur = conn.cursor()
    #cur.execute("drop table review")
    #cur.execute("Drop table listing")
    cur.execute("""
                create table if not exists  listing (
                	id integer primary key,
                	name varchar(200),
                	host_id integer,
                	host_name Varchar(100),
                	neighbourhood_group varchar(30),
                	neighbourhood varchar(30),
                	latitude decimal,
                	longitude decimal,
                	room_type varchar(15),
                	price integer,
                	minimum_nights integer,
                	number_of_reviews integer,
                	last_review date,
                	reviews_per_month decimal,
                	calculated_host_listing_count integer,
                	availability_365 integer
                )
    """
    )
    
    cur.execute("""
                create table if not exists review (
                	listing_id integer references listing(id) on delete cascade,
                	review_id integer primary key,
                	date date,
                	reviewer_id integer,
                	reviewer_name varchar(100),
                	comments text
                )
                """
    )
    
    conn.commit()
    conn.close()

def addData(tableName, path):
    engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")
    df = pd.read_csv(path)
    if tableName=="listing":
        print(f"Replacing newline chars in {path} in column name")

        df=replaceNewline(df,'name')
        print("done")
    elif tableName=="review":
        print(f"deleting unnecessary chars in {path} in column reviewer_name")
        df = deleteUnnecessaryChars(df,"reviewer_name")
        print(f"Replacing newline chars in {path} in column comments")
        df = replaceNewline(df,'comments')
        #bad encoding
        df.at[162758,"comments"] = df.at[162758,'comments'].replace("—\\0",",")
        df.at[822878,"comments"] = df.at[822878,'comments'].replace("—\\0",",")

        #Emojis don't seem compatible with postgres -.-
        df.at[624461,"comments"] = df.at[624461,"comments"].replace(":-)","").replace(":-\\","")
        
        print("done")
    print("Start loading data into db")
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()


    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, tableName, null="") # null values become ''
    conn.commit()
    print(f"table {tableName} complete")

def replaceNewline(df,column):
    """
    transforns \n to \\n, \r to \\r and \t with nothing because sql has a problem with it
    """
    for i in range(len(df[column])):
        try:
            df.at[i,column] = df.at[i,column].replace("\n","\\n").replace("\r","\\r").replace("\t","")
        except AttributeError:
            pass
    
    return df

def deleteUnnecessaryChars(df,column):
    """
    transforns \n to \\n, \r to \\r and \t with nothing because sql has a problem with it
    """
    for i in range(len(df[column])):
        try:
            df.at[i,column] = df.at[i,column].replace("\n","").replace("\r","").replace("\t","").replace("(","").replace(")","")
        except AttributeError:
            pass
    
    return df

if __name__=="__main__":
    createTables()
    
    addData("listing", "data/AB_NYC_2019.csv")
    addData("review", "data/reviews.csv")










