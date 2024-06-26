### Representing Textual Genre in COLaF

Given the quantity and variety of documents that the COLaF project handles, it is necessary to organize 
the corpus by indicating the type of document being processed and its genre. To achieve this, a series of keywords is used,
derived from a controlled vocabulary described in this directory.

This vocabulary operates on several levels: Supergenre, genre, and keywords. 
Supergenre and genre are closed lists, whereas keywords allow the addition of new terms. 
These pieces of information must be combined to best define the document being processed. 

<i>Examples:</i>
| Example | Supergenres | Genres | Keywords|
|--|--|--|--|
|Poetry print | Fiction | Drama||
|Forum on the internet | Web| Social |Forum|
|Interview from a news broadcast transcript | Spoken, Nonfiction | Interview, Transcript, Press | |
| Movie script | Spoken |TV/movie script | Movie|
|Article from a computing web journal | Non Fiction, web | Press | computing |

Textual Genres are presented in the metadata part of the XML-TEI file (Teiheader).
Following the example below, each <term> corresponds to a keyword. 
The <type> attribute indicates the level of description of the term: supergenre, genre, or keyword. 
The term should be written out in full between the two tags.
```
<textClass>
 <keywords>
  <term type="supergenre" rend="nonfiction">Non Fiction</term>
  <term type="supergenre" rend="web">Web</term>
  <term type="genre"
   rend="nonfiction-press">Press</term>
  <term type="motclef"
   rend="nonfiction-press-technology-engineering">Technology computing engineering</term>
 </keywords>
</textClass>
```
