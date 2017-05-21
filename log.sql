DROP VIEW IF EXISTS toparticles CASCADE;
DROP VIEW IF EXISTS topauthors CASCADE;
DROP VIEW IF EXISTS alldayerrors CASCADE;
DROP VIEW IF EXISTS statistics CASCADE;

\c news;

--This view is used to fetch the top articles of the newspaper:
create view toparticles as select articles.title,count(log.path) from log,articles where path like '/article%' and log.path = concat('/article/',articles.slug) group by articles.title,articles.author order by count(path) desc;

--This view is used to fetch the top authors of the newspaper:
create view topauthors as select authors.name,count(articles.author) from log,articles,authors where path like '/article%' and log.path = concat('/article/',articles.slug) and articles.author = authors.id group by articles.author,authors.name order by count(path) desc;

--this view is used to fetch the errors:
create view alldayerrors as select date, count(status) from statistics where status != '200 OK' group by date union all select date,count(status) from statistics group by date;

--This view includes the status and particular date from the timestamp column time
create view statistics as select status,date(time) from log;