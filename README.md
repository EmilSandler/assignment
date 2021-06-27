## User Guide


### First step is to Register and Login, after successful login the server will return a JWT access token and a refresh token.



- Register:

![image](https://user-images.githubusercontent.com/25231082/123539258-77f01180-d741-11eb-891b-299edc9c514b.png)





- Login:

![image](https://user-images.githubusercontent.com/25231082/123539320-d1584080-d741-11eb-869c-377af903adff.png)





### Next step is to send a message to other user, just remember to send the 'access_token' in the Authorization Header.

![image](https://user-images.githubusercontent.com/25231082/123539469-9b678c00-d742-11eb-861f-645ff18787f6.png)





- Send Message:

![image](https://user-images.githubusercontent.com/25231082/123539489-b5a16a00-d742-11eb-9d3f-809e1ebe4b3c.png)





### Lets Login as the receiver and read the message.
### NOTICE - If you read a message the messge will mark as read even if you read all messages at once.

- User 5 Login:

![image](https://user-images.githubusercontent.com/25231082/123539601-36606600-d743-11eb-93fc-b053da31cc3f.png)




### Get Unread Messages:

![image](https://user-images.githubusercontent.com/25231082/123539623-5a23ac00-d743-11eb-82a5-29ea5dfd8b6d.png)




### Get Single Message (by message ID):

![image](https://user-images.githubusercontent.com/25231082/123539686-8ccda480-d743-11eb-9c9f-3b26727474c1.png)




### Get All Messages:

![image](https://user-images.githubusercontent.com/25231082/123539718-a969dc80-d743-11eb-8ff2-d832c6d5f370.png)




### Delete Message (need to send the message_id in the Body):

![image](https://user-images.githubusercontent.com/25231082/123539762-e635d380-d743-11eb-9161-eba307aa395b.png)




