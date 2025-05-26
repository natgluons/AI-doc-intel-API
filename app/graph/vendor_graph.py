from neo4j import GraphDatabase
from app.core.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def add_vendor_node(name):
    with driver.session() as session:
        session.run("MERGE (v:Vendor {name: $name})", name=name)
