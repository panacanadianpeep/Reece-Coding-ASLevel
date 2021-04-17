CREATE TABLE Users (
	user_id varchar(7),
    Actions varchar(7),
	Date_Of_Action date
);

CREATE TABLE DesiredOutput (
	user_id varchar(7) REFERENCES Users(user_id),
    publish_rate int,
    cancel_rate int
);