CREATE OR REPLACE FUNCTION get_course_id_by_email(getid_email VARCHAR(30)) RETURNS bigint AS ' 
 SELECT id FROM user_students 
 WHERE getid_email LIKE email 
'LANGUAGE SQL; 
 
SELECT get_course_id_by_email('aman@mail.ru')





