import os


from neo4j import GraphDatabase, basic_auth


# password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("testamr", "neo4j"))

session = driver.session()

# session.run("CREATE (a:Person {name:'Name', title:'Title'})")

create_str = "CREATE (a:Person {name:{name}, title:{title}})"

# delete_str = "MATCH (a:Person {name: {name}} ) DELETE a"

with session.begin_transaction() as tx:
    for u in [{"uname":"amr","utitle":"admin"},{"uname":"kul","utitle":"user"}]:
        tx.run(create_str,{"name":u["uname"],"title":u["utitle"]})
        # tx.run(delete_str,{"name":u["uname"]})
    tx.success = True

session.close()

sessionnew = driver.session()

result = sessionnew.run("MATCH (a:Person) RETURN a.name AS name, a.title AS title")

for record in result:
    print("%s %s" % (record["title"], record["name"]))

sessionnew.close()



# heroku create london-underground-prod
# Creating ⬢ london-underground-prod... done
# https://london-underground-prod.herokuapp.com/ | https://git.heroku.com/london-underground-prod.git

# heroku create london-underground-stage
# Creating ⬢ london-underground-stage... done
# https://london-underground-stage.herokuapp.com/ | https://git.heroku.com/london-underground-stage.git
