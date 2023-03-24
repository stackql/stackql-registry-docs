---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - databases
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.databases.databases</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `database_cluster_uuid, database_name` | To show information about an existing database cluster, send a GET request to<br />`/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.<br /><br />Note: Database management is not supported for Redis clusters.<br /><br />The response will be a JSON object with a `db` key. This will be set to an object<br />containing the standard database attributes.<br /> |
| `list` | `SELECT` | `database_cluster_uuid` | To list all of the databases in a clusters, send a GET request to<br />`/v2/databases/$DATABASE_ID/dbs`.<br /><br />The result will be a JSON object with a `dbs` key. This will be set to an array<br />of database objects, each of which will contain the standard database attributes.<br /><br />Note: Database management is not supported for Redis clusters.<br /> |
| `add` | `INSERT` | `database_cluster_uuid, data__name` | To add a new database to an existing cluster, send a POST request to<br />`/v2/databases/$DATABASE_ID/dbs`.<br /><br />Note: Database management is not supported for Redis clusters.<br /><br />The response will be a JSON object with a key called `db`. The value of this will be<br />an object that contains the standard attributes associated with a database.<br /> |
| `delete` | `DELETE` | `database_cluster_uuid, database_name` | To delete a specific database, send a DELETE request to<br />`/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /><br />Note: Database management is not supported for Redis clusters.<br /> |
| `_get` | `EXEC` | `database_cluster_uuid, database_name` | To show information about an existing database cluster, send a GET request to<br />`/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.<br /><br />Note: Database management is not supported for Redis clusters.<br /><br />The response will be a JSON object with a `db` key. This will be set to an object<br />containing the standard database attributes.<br /> |
| `_list` | `EXEC` | `database_cluster_uuid` | To list all of the databases in a clusters, send a GET request to<br />`/v2/databases/$DATABASE_ID/dbs`.<br /><br />The result will be a JSON object with a `dbs` key. This will be set to an array<br />of database objects, each of which will contain the standard database attributes.<br /><br />Note: Database management is not supported for Redis clusters.<br /> |
