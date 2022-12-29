<h1>How To Run</h1>
<p>after cloning project or download open your terminal and 
change directory to project and run "docker-compose up" </p>
<h3>Notes:</h3>
<p>the docker must be installed in your system</p>
<p>it may take a while for the first time
to build image and crate containers</p>
<p>the postgres use port:5432 by default 
if the postgres is installed in your system you have to stop the service
or change postgres container port in docker-compose file</p>
<h1>Api</h1>
<table>
    <tr>
        <th>Endpoint</th>
        <th>HttpMethod</th>
        <th>Authorizations</th>
        <th>Result</th>
    </tr>
    <tr>
        <td>account/register/</td>
        <td>POST</td>
        <td>All</td>
        <td>register a user</td>
    </tr>
    <tr>
        <tr>
        <td>account/login/</td>
        <td>POST</td>
        <td>All</td>
        <td>access token and refresh token</td>
    </tr>
    <tr>
        <tr>
        <td>account/refresh-token/</td>
        <td>POST</td>
        <td>All</td>
        <td>new access token </td>
    </tr>
    <tr>
        <tr>
        <td>account/change-password/</td>
        <td>PUT</td>
        <td>Authenticated user</td>
        <td>change password</td>
    </tr>
    <tr>
        <tr>
        <td>message/send/?receiver=</td>
        <td>GET</td>
        <td>Authenticated user</td>
        <td>list all message that user sent for receiver username
            (list all sent message if receiver was none or empty)</td>
    </tr>
    <tr>
        <tr>
        <td>message/send/</td>
        <td>POST</td>
        <td>Authenticated user</td>
        <td>sending message </td>
    </tr>
    <tr>
        <tr>
        <td>message/received/?sender=</td>
        <td>GET</td>
        <td>Authenticated user</td>
        <td>list all received messages by sender username
            (list all received message if sender was none or empty)</td>
    </tr>
    <tr>
        <tr>
        <td>message/:pk</td>
        <td>GET</td>
        <td>sender or receiver user</td>
        <td>retrieve a message </td>
    </tr>
    <tr>
        <tr>
        <td>message/:pk</td>
        <td>PUT</td>
        <td>sender user</td>
        <td>update a message </td>
    </tr>
    <tr>
        <tr>
        <td>message/:pk</td>
        <td>DELETE</td>
        <td>sender user</td>
        <td>delete a message </td>
    </tr>



</table>

