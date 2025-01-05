
drop table ru.cosine
create table ru.cosine as
select a.*, b.afidtc as afdtc1, b.aval as aval1 from (select * from ru.adcd where (afidtc like '%DIOD%' and param = 'FISTRESN')  ) as a 
left join ( select * from ru.adcd where (afidtc like '%XPEL%') or (afidtc like '%DIOD%') and param= 'FISTRESN') as b
on a.subjid = b.subjid 
and a.fidtc = b.fidtc

--ALTER TABLE ru.russell RENAME TO ru;
