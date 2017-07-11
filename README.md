# TabInOut (Table Information Out) - Framework for information extraction from tables

TabInOut is a framework for information extraction from tables and a GUI tool for generating information extraction rules from the tables in literature. The tool is dependent on [TableDisentangler](https://github.com/nikolamilosevic86/TableAnnotator) and actually presents the second step in the extraction pipeline. Firstly, tables are processed, disentangled and annotated using Tabledisentangler tool. TabInOut uses database created by TableAnnotator, uses all the functional and structural annotation performed by TableDisentangler in order to extract information from the tables. It also creates additional table in the mySQL database where it stores the extracted information.

We are currently working on a paper that will present the methodology of TabInOut, however, it is based on case study and a hybrid approach already presented at BIOSTEC and BelBi conference. You can see and read relevant papers we published bellow. 

The project is part of my PhD project funded by EPRSC and AstraZeneca.

The main application (Wizard) is located under Wizard folder. You can run it by starting TkGUIFirstScreen.py file. Alternatively you can start TableInOut wizard by running TableInOutStarter.sh from the main directory.


## Relevant publications:
* Milosevic,N; Gregson, C; Hernandez, R; Nenadic, G. (2016, June). [Disentangling the Structure of Tables in Scientific Literature](http://link.springer.com/chapter/10.1007%2F978-3-319-41754-7_14). In Natural Language Processing and Information Systems: 21st International Conference on Applications of Natural Language to Information Systems, NLDB 2016, Salford, UK, June 22-24, 2016, Proceedings (Vol. 9612, p. 162). Springer.
* Milosevic, N., Gregson, C., Hernandez, R., & Nenadic, G. (2016). [Extracting patient data from tables in clinical literature: Case study on extraction of BMI, weight and number of patients.](http://www.scitepress.org/DigitalLibrary/PublicationsDetail.aspx?ID=/O16myWhsP4=&t=1). In Proceedings of the 9th International Joint Conference on Biomedical Engineering Systems and Technologies ISBN 978-989-758-170-0, pages 223-228. DOI: 10.5220/0005660102230228
* Milosevic, N., Gregson, C., Hernandez, R., & Nenadic, G. [Hybrid methodology for information extraction from tables in the biomedical literature](https://www.academia.edu/26499404/Hybrid_methodology_for_information_extraction_from_tables_in_the_biomedical_literature). In Proceedings of the Belgrade Bioinformatics Conference (BelBi2016) 
* Milosevic, N. (2016). [Marvin: Semantic annotation using multiple knowledge sources.](http://arxiv.org/abs/1602.00515) arXiv preprint arXiv:1602.00515.


