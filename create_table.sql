

CREATE TABLE payments(
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES user_course(id),
	amaount INTEGER,
	pay_date DATE NULL

);


