---
title: connection_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_pools
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
<tr><td><b>Name</b></td><td><code>connection_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.connection_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A unique name for the connection pool. Must be between 3 and 60 characters. |
| <CopyableCode code="connection" /> | `object` |  |
| <CopyableCode code="db" /> | `string` | The database for use with the connection pool. |
| <CopyableCode code="mode" /> | `string` | The PGBouncer transaction mode for the connection pool. The allowed values are session, transaction, and statement. |
| <CopyableCode code="private_connection" /> | `object` |  |
| <CopyableCode code="size" /> | `integer` | The desired size of the PGBouncer connection pool. The maximum allowed size is determined by the size of the cluster's primary node. 25 backend server connections are allowed for every 1GB of RAM. Three are reserved for maintenance. For example, a primary node with 1 GB of RAM allows for a maximum of 22 backend server connections while one with 4 GB would allow for 97. Note that these are shared across all connection pools in a cluster. |
| <CopyableCode code="user" /> | `string` | The name of the user for use with the connection pool. When excluded, all sessions connect to the database as the inbound user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_connectionPool" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, pool_name" /> | To show information about an existing connection pool for a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`.<br />The response will be a JSON object with a `pool` key. |
| <CopyableCode code="list_connectionPools" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`.<br />The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects. |
| <CopyableCode code="add_connectionPool" /> | `INSERT` | <CopyableCode code="database_cluster_uuid, data__db, data__mode, data__name, data__size" /> | For PostgreSQL database clusters, connection pools can be used to allow a<br />database to share its idle connections. The popular PostgreSQL connection<br />pooling utility PgBouncer is used to provide this service. [See here for more information](https://www.digitalocean.com/docs/databases/postgresql/how-to/manage-connection-pools/)<br />about how and why to use PgBouncer connection pooling including<br />details about the available transaction modes.<br /><br />To add a new connection pool to a PostgreSQL database cluster, send a POST<br />request to `/v2/databases/$DATABASE_ID/pools` specifying a name for the pool,<br />the user to connect with, the database to connect to, as well as its desired<br />size and transaction mode.<br /> |
| <CopyableCode code="delete_connectionPool" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, pool_name" /> | To delete a specific connection pool for a PostgreSQL database cluster, send<br />a DELETE request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /> |
| <CopyableCode code="_get_connectionPool" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, pool_name" /> | To show information about an existing connection pool for a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`.<br />The response will be a JSON object with a `pool` key. |
| <CopyableCode code="_list_connectionPools" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`.<br />The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects. |
| <CopyableCode code="update_connectionPool" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, pool_name, data__db, data__mode, data__size" /> | To update a connection pool for a PostgreSQL database cluster, send a PUT request to  `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. |
