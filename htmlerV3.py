# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:44:22 2020

@author: flap
"""
#import re
#import sys
from datetime import date
today = date.today()

raw_csv_file = '.\\new_articles.tsv'

fichier_sortie = '.\\web\\html' + today.strftime("%d%m%Y") + '.html'

style = 1

def main():
    
    liste_articles = open (raw_csv_file, "r", encoding='utf-8')
    
    fichier_html = open (fichier_sortie, "w", encoding='utf-8')
    
    articles = liste_articles.readlines()
    
   # print(articles)
    
    def intro(date,nb_articles):
    
        introduction = "<!DOCTYPE html>\n<html><head><title>Lexique BCTQ</title></head><body>"
        introduction += "\nDate {} <br />  Nombre d'articles: {}\n".format(date, nb_articles)    
        introduction +=  "<br /><br />"
        return introduction
    
    def css(style):
       
        span = """<style>
                span.vedette  {
                    font-size: 130%;
                        }
                span.catgram {
                    font-size: 110%;
                        }
        
                div.renvois {
                    padding-left: 50px;
                           }
                
                div.renvois_anglais {
                    padding-left: 50px;
                           }
                
                span.FL_key {
                    font-variant: small-caps;

                        }
                span.FL_value {
                    }
                
                span.vedette_anglais  {
                    font-size: 120%;
                    font-style: italic;
                        }
                span.termes_anglais  {
                    font-size: 120%;
                    font-style: italic;
                        }
                 
                p.definition {
                    font-size: 110%;
                        }
                
                p.notes {
                    }
                
                table {
                    background-color: rgb(244, 244, 244);
                    width:800px;
                    }

                td {
                    //padding-left: 50px;
                    vertical-align: top;
                    text-align: left;
                    width:50%;
                    }
                
                </style>"""
        
        return span
   
    def outro():
        outroduction = "</body></html>"
    
        return outroduction    
    def format_renvois(type_de_renvoi, renvois):
            
        liste_renvois = ""
            
        if renvois:    
            print (renvois)
            liste_renvois += "<tr><td><span class='FL_key'><strong>" + type_de_renvoi + "</strong></span></td>"                   
            liste_renvois += "<td><span class='FL_value'><strong>" + renvois + "</strong></span></td></tr>\n"
                       
        return liste_renvois

                
    def format_article(article):
        
        rubriques = article.split("\t")
        
        categorie = rubriques[1]
        vedette_anglais = rubriques[0]
        vedette = rubriques[2]
        catgram = rubriques[3]
        definition = rubriques[4]
        #notes = rubriques[5]
        abrege = format_renvois("abrégé", rubriques[5])
        synonymes = format_renvois("synonyme(s)", rubriques[6])
        veilli = format_renvois("veilli", rubriques[7])
        critique = format_renvois("critiqué", rubriques[8])
        classe = format_renvois("classe", rubriques[9])
        etape_de = format_renvois("étape de", rubriques[10])
        regroupement = format_renvois("regroupement", rubriques[11])
        constituant_de = format_renvois("constituant de", rubriques[12])
        types = format_renvois("types", rubriques[13])
        constituants = format_renvois("constituants", rubriques[14])
        par_oppos_a = format_renvois("par oppos. à", rubriques[15])
        mot_voisin = format_renvois("mot voisin", rubriques[16])
        metiers = format_renvois("métier(s)", rubriques[17])
        termes_anglais = rubriques[18]
        
        

        article_html = "\n\n\n<br /><hr><small> CATEGORIE: " + categorie + "</small>"
        article_html += "\n<br /><br /><span class='vedette'><i>" + vedette_anglais + "</i></span>"
        article_html += "<br /><strong><span class='vedette'>" + vedette + "</span></strong>\n"
        article_html +="<span class='catgram'>, " + catgram + "</span><br />\n"
        #article_html +="<strong><span class='vedette_anglais'>" + vedette_anglais + "</span></strong><br />\n"
        article_html +="<p class='definition'>" + definition + "</span></p>\n"         
        #article_html +="<p class='notes'>" + notes + "</p>\n"
        
        article_html +="\n<table>"
        if abrege:
            article_html +="\n<div class='renvois'>" + abrege + "</div>\n"
        #article_html +="<div class='renvois_anglais'>" + syn_anglais + "</div>\n"
        if synonymes:
            article_html +="\n<div class='renvois'>" + synonymes + "</div>\n"
        if veilli:
            article_html +="\n<div class='renvois'>" + veilli + "</div>\n"
        if critique:
            article_html +="\n<div class='renvois'>" + critique + "</div>\n"
        if classe:
            article_html +="\n<div class='renvois'>" + classe + "</div>\n"
        if etape_de:
            article_html +="\n<div class='renvois'>" + etape_de + "</div>\n"
        if regroupement:
            article_html +="\n<div class='renvois'>" + regroupement + "</div>\n"
        if constituant_de:
            article_html +="\n<div class='renvois'>" + constituant_de + "</div>\n"
        if types:
            article_html +="\n<div class='renvois'>" + types + "</div>\n"
        if constituants:
            article_html +="\n<div class='renvois'>" + constituants + "</div>\n"
        if par_oppos_a:
            article_html +="\n<div class='renvois'>" + par_oppos_a + "</div>\n"
        if mot_voisin:
            article_html +="\n<div class='renvois'>" + mot_voisin + "</div>\n"
        if metiers:
            article_html +="\n<div class='renvois'>" + metiers + "</div>\n"
        article_html +="</table>"

        article_html +="\n\n<br /><span><strong>Anglais:</strong></span>"
        article_html +="\n<br /><span class='termes_anglais'>" + termes_anglais + "</span>"

          
        return article_html
   
    fichier_html.write(intro(today,len(articles)))
    #print(intro(today,len(articles)))
    
    fichier_html.write(css(1))
    #print(css(1))
    
    #print(articles[0])
    
    for article in articles:
        fichier_html.write(format_article(article))
        #print(format_article(article))
    
    
    fichier_html.write(outro())
    #print(outro())
    
main()