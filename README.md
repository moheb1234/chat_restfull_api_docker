<h1>How To Run</h1>
<p>after cloning project or download open your terminal and 
change directory to project and run "docker-compose up" </p>
<h3>Notes:</h3>
<p>the docker must be installed in your system</p>
<p>it may take a while for the first time
to build image and crate containers</p>
<p>the postgres use port:5432 by default 
if the postgres sql is installed in your system you have to stop the service
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
        <td>registered username</td>
    </tr>
        <tr>
        <td>account/login/</td>
        <td>POST</td>
        <td>All</td>
        <td>access token and refresh token</td>
    </tr>
</table>

