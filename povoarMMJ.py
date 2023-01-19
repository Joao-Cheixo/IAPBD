import mysql
import mysql.connector
from mysql.connector import Error
import pandas as pd 
import mysql.connector as SQLC
import re
import os
from os import listdir
from os.path import isfile, join
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature


def demonstra_ficheiros(path):
    # retorna todos os ficheiros genbank numa diretoria
    a = []
    files = [file for file in listdir(path) if isfile(join(path, file))]

    for name in files:
        a.extend(re.findall(r'\w+.gb', name))
    return a


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'") 


def povoar_locus(org):
    org = SeqIO.read(org,"genbank")
    id_l = org.name
    bp = len(org)
    sql_locus = f"INSERT INTO locus (bp, id_l) VALUES('{bp}','{id_l}')"
    print(sql_locus)
    Cursor.execute(sql_locus)
    DataBase.commit()


def len_sequencia(org):
    org = SeqIO.read(org, "genbank")
    len_seq = len(org)
    sql_sequencia = f"INSERT INTO sequencia (len_seq) VALUES ('{len_seq}')"
    print(sql_sequencia)
    Cursor.execute(sql_sequencia)
    DataBase.commit()


def features(org):

    tamanho = len(org.features)
    org = SeqIO.read(org, "genbank")
    CDS = [] 
    for i in range(len(org.features)):
        if org.features[i].type=='CDS':
            CDS.append(i)
    for k in CDS:
        print(org.features[k].location)
        print(len(CDS))
    gene = [] 
    for j in range(len(org.features)):
        if org.features[j].type=='gene':
            gene.append(j)
    for a in gene:
        print(org.features[a].location)
        print(len(gene))

    mobile_element = [] 
    for f in range(len(org.features)):
        if org.features[f].type=='mobile_element':
            mobile_element.append(f)
    for b in mobile_element:
        print(org.features[b].location)
        print(len(mobile_element))
        
    fsource = [] 
    for m in range(len(org.features)):
        if org.features[m].type=='source':
            fsource.append(m)
    for a in fsource:
        print(org.features[a].location)
        print(len(fsource))

    repeat = [] 
    for m in range(len(org.features)):
        if org.features[m].type=='repeat_region':
            repeat.append(m)
    for a in repeat:
        print(org.features[a].location)
        print(len(repeat))
        
    misc = [] 
    for m in range(len(org.features)):
        if org.features[m].type=='misc_feature':
            misc.append(m)
    for a in misc:
        print(org.features[a].location)
        print(len(misc))
    
    sql_features = f"INSERT INTO features (tamanho, CDS, gene, mobile_element, misc, repeat_region, fsource) VALUES ('{tamanho}','{';'.join(str(c) for c in CDS)}','{';'.join(str(g) for g in gene)}','{';'.join(str(me) for me in mobile_element)}','{';'.join(str(mi) for mi in misc)}','{';'.join(str(r) for r in repeat)}','{';'.join(str(fs) for fs in fsource)}')"
    print(sql_features)
    Cursor.execute(sql_features)
    DataBase.commit()


def titulo_journal(ficheiro):
    
    fonte = open(ficheiro,'r')
    org = fonte.read()
    fonte.close()
    t = '' 
    titulo = re.findall(r'TITLE\s+.*?(?=JOURNAL)', org, re.DOTALL)
    if titulo:
        for title in titulo:
            m = re.match( r'TITLE\s+(.+)', title, re.DOTALL )
            t = t + re.sub(r'\s+', ' ', m.group(1) ) 
    print(t)


def insere_jornal (org):
    fonte = open(org,'r')
    org = fonte.read()
    fonte.close()
    j = ''
    jou = re.findall(r'JOURNAL\s+.*?(?=PUBMED|REFERENCE|FEATURES|COMMENT)', org, re.DOTALL)
    if jou:
        for journal in jou:
            m = re.match( r'JOURNAL\s+(.+)', journal, re.DOTALL )
            j = j + re.sub(r'\s+', ' ', m.group(1) ) 
    print(j)

    sql_reference = f"INSERT INTO reference (title, journal) VALUES ('{t}','{j}')"
    print(sql_reference)
    Cursor.execute(sql_reference)
    DataBase.commit()


def filiacao_autores(org):
    fonte = open(org,'r')
    org = fonte.read()
    fonte.close()
    filiacao = ''
    f = re.findall(r'AUTHORS\s+.*?(?=TITLE)', org, re.DOTALL)
    if f:
        for auth in f:
            m = re.match( r'AUTHORS\s+(.+)', auth, re.DOTALL )
            filiacao = filiacao + re.sub(r'\s+', ' ', m.group(1))
    print(filiacao)

    sql_autor = f"INSERT INTO autor (filiacao) VALUES ('{filiacao}')"
    print(sql_autor)
    Cursor.execute(sql_autor)
    DataBase.commit()


def annotations(org):
    org = SeqIO.read(org, "genbank")
    len_annotations = len(org.annotations) 
    source = org.annotations["source"]
    letter_annotations = org.letter_annotations
    organism = org.annotations["organism"] 
    taxonomy = org.annotations["taxonomy"] 
    mol_type = org.annotations['molecule_type']
    accessions = org.annotations['accessions'] 
    keywords = org.annotations.keys() 
    sql_annotations = f"INSERT INTO annotations (keywords, accessions, mol_type, organism, letter_annotations, source, taxonomy, len_annotations) VALUES ('{';'.join(keywords)}', '{';'.join(accessions)}','{mol_type}','{organism}','{letter_annotations}', '{source}','{'; '.join(taxonomy)}', '{len_annotations}')"
    print(sql_annotations)
    Cursor.execute(sql_annotations)
    DataBase.commit()  


def nome_org(org):
    fonte = open(org,'r')
    org = fonte.read()
    fonte.close()

    link_NCBI = ''
    link = re.search(r'ACCESSION\s+[^\s]+', org)
    if link:
        m = re.match(r'ACCESSION\s+([^\s]+)', link[0] )
        if m:
            id = m.group(1)
            link_NCBI = link_NCBI + "https://www.ncbi.nlm.nih.gov/nuccore/{}".format( id ) 
    else:
        print( "Padrão não encontrado" )

    fonte = open(org,'r')
    org = SeqIO.read(org, "genbank")

    id = org.id

    descricao = org.description
    
    flag = False
    nome = ""
    for linha in fonte:   
        if re.search(r"^SOURCE", linha):
            s = re.match(r"SOURCE\s+(.+)", linha)
            if s:
                nome = s.group(1)
        if re.search(r"//", linha):
            flag = False  
    fonte.close()
    return print(nome)


def url(item):
    urls = []
    url = "https://pubmed.ncbi.nlm.nih.gov//?term={}".format(item)
    urls.append(url)
    return urls


def validar(item):
    return re.match(r'[\d|a-z|A-Z]+(_?[\d|a-z|A-Z]+)*', item)


def valida_url_pubmed(item):
    query = item
    try:
        if not validar(query):
            raise Exception
        else:
            print(url(query))

    except Exception:
        print(f'ERROR This is what you inserted:"{query}"')

    link_pubmed = url(query)
    sql_bacterias = f"INSERT INTO bacterias (id, link_NCBI, descricao, nome, link_pubmed) VALUES ('{id}','{link_NCBI}','{descricao}','{nome}','{';'.join(link_pubmed)}')"
    print(sql_bacterias)
    Cursor.execute(sql_bacterias)
    DataBase.commit()


def multipla_auto_populacao():
    path = input("Coloque o caminho completo para a pasta que contem os ficheiro genbank:")
    lista_fich=[]
    lista_fich=demonstra_ficheiros(path)
    host_name =input("Nome de host")
    user_name = input("Nome do usuario")
    user_password = input("Password do usuario")
    db_name = input("Nome da database")
    connection = create_db_connection(host_name,user_name,user_password,db_name)
    desejo= input("Prima 1 se deseja efetuar um comando para a database ")
    if desejo=="1":
        query = input("Comando para db:")
        execute_query(connection,query)

    for file in lista_fich:
        povoar_locus(file)
        len_sequencia(file)
        features(file)
        titulo_journal(file)
        insere_jornal(file)
        filiacao_autores(file)
        annotations(file)
        nome = nome_org(file)
        valida_url_pubmed(nome)
    
    return 0

""" 
Para utilizacao deste modulo , faz se import do mesmo e antes da invocacao de qualquer funcao 
especifique o nome do modulo. 

Exemplos:

import povoarMMJ 

povoarMMJ.features(exemplo)
povoarMMJ.multipla_auto_populacao()

"""