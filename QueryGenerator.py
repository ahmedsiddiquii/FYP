import json
from config import *
class QueryGenerator:
    def __init__(self):
        with open("data_list.txt","r") as f:
            self.data = json.loads(f.read())
        self.database_name=""
        self.entities = []
        self.sub_entities = {}
        self.main_entities = {}
    def define_db_name(self):
        for i in self.data:
            self.database_name=i
            break
        print("db name",self.database_name)
        return self.database_name
    def define_entities(self):
        for entity in self.data[self.database_name]:
            for i in entity:
                self.entities.append(i)
                break
        return self.entities
    def define_sub_entities(self):

        for i,entity in enumerate(self.entities):
            self.sub_entities[entity] = []
            for j in self.data[self.database_name][i][entity]:
                self.sub_entities[entity].append(j)
        return self.sub_entities
    def write_sub_entity_query(self):
        queries=[]
        for i,entity in enumerate(self.sub_entities):
            # print(entity)
            self.main_entities[entity] = {}
            for sub_entity in self.sub_entities[entity]:

                query  = "CREATE TABLE "+sub_entity+ " ("
                sub_entity_data = self.data[self.database_name][i][entity][sub_entity]
                count=0
                for attribute in sub_entity_data:
                    # attribute = attribute.casefold().replace(" ", "_")
                    attribute_data = sub_entity_data[attribute]
                    if attribute_data["checkable"] == False:
                        query+=attribute.casefold().replace(" ", "_")+" "+attribute_data['data_type']+","
                    else:
                        if attribute_data['checked'] == True:
                            query += attribute.casefold().replace(" ", "_") + " " + attribute_data['data_type'] + ","
                    count+=1

                query+="PRIMARY KEY (id)"
                query+=")"
                query = query.replace(",)",")")
                if count!=0:
                    queries.append(query)
                    self.main_entities[entity][sub_entity + "_id"] =  {"data_type":"int","constraint":"fk"}
                else:
                    self.main_entities[entity][sub_entity] = {"data_type": "varchar(255)", "constraint": ""}
        return queries
    def write_main_entity_query(self):
        queries = []
        for entity in self.main_entities:
            fk = []
            query = "CREATE TABLE " + entity + " ("
            for attribute in self.main_entities[entity]:
                attribute_data =  self.main_entities[entity][attribute]
                query += attribute.casefold().replace(" ", "_") + " " + attribute_data['data_type'] + ","
                if attribute_data['constraint'] == "fk":
                    fk.append(attribute.casefold().replace(" ", "_"))
            for fks in fk:
                table = fks.replace("_id","")
                query+=f"FOREIGN KEY ({fks}) REFERENCES {table}(id),"
            query+=")"
            query=query.replace(",)",")")
            queries.append(query)
        return queries
    def generate_sub_tables(self, username,password,host,port,dbname):
        queries= self.write_sub_entity_query()
        print(len(queries))
        conn = mysqlconnect(username,password,host,port,dbname)
        cursor=conn.cursor()
        for query in queries:
            try:
                cursor.execute(query)
                conn.commit()
            except Exception as e:
                print(query)
                print(e)
                print("\n")
                pass
    def generate_main_tables(self, username,password,host,port,dbname):
        queries= self.write_main_entity_query()
        print(len(queries))
        conn = mysqlconnect(username,password,host,port,dbname)
        cursor=conn.cursor()
        for query in queries:
            try:
                cursor.execute(query)
                conn.commit()
            except Exception as e:
                print(query)
                print(e)
                print("\n")
                pass

# obj=QueryGenerator()
# print(obj.define_db_name())
# print(obj.define_entities())
# print(obj.define_sub_entities())
# obj.generate_sub_tables("root","12345678","localhost","3306","fyp3")
# obj.generate_main_tables("root","12345678","localhost","3306","fyp3")
# obj.write_sub_entity_query()
# obj.write_main_entity_query()
# print(obj.main_entities)