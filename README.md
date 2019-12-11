# test-repo
#production jira user license cleanup step to get user in csv file from DB
#ssh host-name
#$ cd /usr/local/ecomm/atlassian/data/mysql/jiraMYSQL/mysql-5.5.13-linux2.6-x86_64
#$ ./bin/mysql -u root -p --socket=/usr/local/ecomm/atlassian/data/mysql/jiraMYSQL/socket/mysql.sock --port=6666
#$connect jiradb;
#(run below script to get list of user in mention file, move it on local and set filter to filter user list which do not need to desabled then desablel user manually)
select user_name,u.email_address, u.display_name,u.updated_date,ua.attribute_value LAST_LOGIN_IN_MILLIS from cwd_user u, cwd_user_attributes ua where u.id = ua.user_id and ua.attribute_name ='login.lastLoginMillis' and CAST(ua.attribute_value AS UNSIGNED INTEGER) < (select max(CAST(attribute_value AS UNSIGNED INTEGER))-10518984000 from cwd_user_attributes where attribute_name ='login.lastLoginMillis') AND u.active = '1' INTO OUTFILE '/usr/local/ecomm/atlassian/data/mysql/jiraMYSQL/inactive_jira_users_dec06_2019.csv'FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
