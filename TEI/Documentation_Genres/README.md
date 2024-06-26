### Representing Textual Genre in COLaF

Given the quantity and variety of documents that the COLaF project handles, it is necessary to organize 
the corpus by indicating the type of document being processed and its genre. To achieve this, a series of keywords is used,
derived from a controlled vocabulary described in this directory.

#### Description
This vocabulary operates on several levels: Supergenre, genre, and keywords. 
Supergenre and genre are closed lists, whereas keywords allow the addition of new terms. 
These pieces of information must be combined to best define the document being processed. 

| SuperGenres | Genres |
| --|  --|
|Fiction| Prose, Poetry, Drama, Bible|
| Non fiction| Press, Academic, Administrative, Legal, reference, Interractive, LearningMaterials, Instructional |
| Web | Blog, Social, Wiki |
| Spoken | Interview, Transcript of video/audio, TV/movie script, Other, Lyrics|

The Keywords can specify the types of document (for NonFiction, Interractive: Letters, email, comments... for examples), the domain of the document (For academic or press, if it's about art, science, medecine...., For fiction if it's science-fiction, etc...). 

It is mandatory to use at least one supergenre and one genre to describe the document. Keywords are not obligatory but it is best to make use for them. A non exhaustive list of keywords is given here, so if another keyword, not in the list, can describe better the document, it can be use.

#### Examples
| Example | Supergenres | Genres | Keywords|
|--|--|--|--|
|Poetry print | Fiction | Poetry||
|Forum on the internet | Web| Social |Forum|
|Interview from a news broadcast transcript | Spoken, Nonfiction | Interview, Transcript, Press | Type: National, Domain: Politics, News |
| Movie script | Spoken |TV/movie script | Type: Movie, Domain: Science-fiction|
|Article from a computing web journal | Non Fiction, web | Press | Domain: computing |

#### Documentation
The Hierarchie file contains a list of the SuperGenre and Genre used by COLaF and the Keywords file a non exhaustive list of keywords. Each of these elements have a identifier created to use in the XML-file. Usually, Supergenre, genre and keywords have been created to have obvious association such as Non Fiction/Press, Fiction/drama, etc... and this association is shown in the structure of each identifier.


The Alignement file present the work done to create this controled vocabulary by studying the other genres description vocabularies that exist. It associate, for each keywords in more than 5 controled vocabularies, the keyword used in COLAF genres vocabulary.

#### Representation of Textual Genres in the XML
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

#### Development of the COLaF Textual Genre vocabulary
If you're using our vocabulary to describe your document and you need new keywords (or even genres!), please create an issue on this repository so we can talk about it with you and maybe add your term in the vocabulary. 

