---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of a database user. |
| <CopyableCode code="mysql_settings" /> | `object` |  |
| <CopyableCode code="password" /> | `string` | A randomly generated password for the database user. |
| <CopyableCode code="role" /> | `string` | A string representing the database user's role. The value will be either<br />"primary" or "normal".<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_user" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, username" /> | To show information about an existing database user, send a GET request to<br />`/v2/databases/$DATABASE_ID/users/$USERNAME`.<br /><br />Note: User management is not supported for Redis clusters.<br /><br />The response will be a JSON object with a `user` key. This will be set to an object<br />containing the standard database user attributes.<br /><br />For MySQL clusters, additional options will be contained in the mysql_settings<br />object.<br /> |
| <CopyableCode code="list_users" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the users for your database cluster, send a GET request to<br />`/v2/databases/$DATABASE_ID/users`.<br /><br />Note: User management is not supported for Redis clusters.<br /><br />The result will be a JSON object with a `users` key. This will be set to an array<br />of database user objects, each of which will contain the standard database user attributes.<br /><br />For MySQL clusters, additional options will be contained in the mysql_settings object.<br /> |
| <CopyableCode code="add_user" /> | `INSERT` | <CopyableCode code="database_cluster_uuid, data__name" /> | To add a new database user, send a POST request to `/v2/databases/$DATABASE_ID/users`<br />with the desired username.<br /><br />Note: User management is not supported for Redis clusters.<br /><br />When adding a user to a MySQL cluster, additional options can be configured in the<br />`mysql_settings` object.<br /><br />The response will be a JSON object with a key called `user`. The value of this will be an<br />object that contains the standard attributes associated with a database user including<br />its randomly generated password.<br /> |
| <CopyableCode code="delete_user" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, username" /> | To remove a specific database user, send a DELETE request to<br />`/v2/databases/$DATABASE_ID/users/$USERNAME`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /><br />Note: User management is not supported for Redis clusters.<br /> |
| <CopyableCode code="_get_user" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, username" /> | To show information about an existing database user, send a GET request to<br />`/v2/databases/$DATABASE_ID/users/$USERNAME`.<br /><br />Note: User management is not supported for Redis clusters.<br /><br />The response will be a JSON object with a `user` key. This will be set to an object<br />containing the standard database user attributes.<br /><br />For MySQL clusters, additional options will be contained in the mysql_settings<br />object.<br /> |
| <CopyableCode code="_list_users" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To list all of the users for your database cluster, send a GET request to<br />`/v2/databases/$DATABASE_ID/users`.<br /><br />Note: User management is not supported for Redis clusters.<br /><br />The result will be a JSON object with a `users` key. This will be set to an array<br />of database user objects, each of which will contain the standard database user attributes.<br /><br />For MySQL clusters, additional options will be contained in the mysql_settings object.<br /> |
| <CopyableCode code="reset_auth" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, username" /> | To reset the password for a database user, send a POST request to<br />`/v2/databases/$DATABASE_ID/users/$USERNAME/reset_auth`.<br /><br />For `mysql` databases, the authentication method can be specifying by<br />including a key in the JSON body called `mysql_settings` with the `auth_plugin`<br />value specified.<br /><br />The response will be a JSON object with a `user` key. This will be set to an<br />object containing the standard database user attributes.<br /> |
