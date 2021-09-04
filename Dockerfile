FROM ghcr.io/maastrichtu-ids/code-server:latest

ENV PATH="$PATH:/home/coder/.yarn/bin"

RUN yarn global add @rmlio/yarrrml-parser

# Download latest RML mapper in /opt/rmlmapper.jar
RUN curl -s https://api.github.com/repos/RMLio/rmlmapper-java/releases/latest \
    | grep browser_download_url | grep .jar | cut -d '"' -f 4 \
    | wget -O /opt/rmlmapper.jar -qi -

# Downloac SHACL compact converter
RUN wget -O /opt/shaclconvert.jar https://gitlab.ontotext.com/yasen.marinov/shaclconvert/-/raw/master/built/shaclconvert.jar
# java -jar /opt/shaclconvert.jar resources/bio2kg-shapes.shaclc resources/bio2kg-shapes.shacl