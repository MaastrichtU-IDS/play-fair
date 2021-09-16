
yarrrml_mappings=$1

if [ -z "$yarrrml_mappings" ]
then
    echo "Provide the path to a YARRRML file"
    exit
fi
mkdir -p data
mkdir -p output

rml_mappings=data/$(echo $yarrrml_mappings | sed "s/\.yarrr\.yml/.rml.ttl/g" )
rdf_output=output/$(echo $yarrrml_mappings | sed "s/\.yarrr\.yml/-output.ttl/g" )

yarrrml-parser -i $yarrrml_mappings -o $rml_mappings

java -jar /opt/rmlmapper.jar -m $rml_mappings -o $rdf_output