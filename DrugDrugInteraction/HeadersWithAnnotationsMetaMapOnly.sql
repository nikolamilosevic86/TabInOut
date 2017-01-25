SELECT idCell,specId,TableOrder,cell.Content,GROUP_CONCAT(AnnotationID SEPARATOR ', ') as concepts,GROUP_CONCAT(AnnotationDescription SEPARATOR ', ') as semanticTypes 
FROM cell 
left join cellroles on cell.idCell=cellroles.Cell_idCell 
left join arttable on arttable.idTable=cell.Table_idTable 
left join annotation on cell.idCell=annotation.Cell_idCell 
left join article on article.idArticle=arttable.Article_idArticle 
where CellRole_idCellRole=1 and section="34073-7" and AgentName="MetaMap" 
Group by idCell;