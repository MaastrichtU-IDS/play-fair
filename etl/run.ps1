

yarrrml-parser -i mapping-ludeme.yarrr.yml -o data/mapping-ludeme.rml.ttl

java -jar rmlmapper.jar -m data/mapping-ludeme.rml.ttl -o data/output-rdf.ttl -s turtle