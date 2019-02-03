import boto3
import mysql.connector
from botocore.exceptions import ClientError

#Using boto3 to send email
def processSendMail(course_name):
    mydb = mysql.connector.connect(
      host="localhost",
      user="",
      passwd="",
      database=""
    )

    mycursor = mydb.cursor()

    sql = "SELECT email FROM contacts WHERE course_name = %s"
    val = (course_name,)
    mycursor.execute(sql, val)

    result = mycursor.fetchall()


    for c in result:
        sendMail(str(c[0]),course_name)


def sendMail(address, course_name):
    SENDER = "Section Update <newsectionnotification@reckerwang.com>"
    RECIPIENT = address
    AWS_REGION = "us-east-1"
    SUBJECT = "Section Update for Course " + course_name


    BODY_TEXT = ("There is an update of sections for \r\n") + course_name
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Section Update</h1>
      <p>There is an update of sections for</p> """ + course_name + """
    </body>
    </html>
                """            
    # The character encoding for the email.
    CHARSET = "UTF-8"

    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong. 
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

#for testing 
processSendMail("CMSC420")


