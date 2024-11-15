---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - databases
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.pools" /></td></tr>
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
| <CopyableCode code="standby_connection" /> | `object` |  |
| <CopyableCode code="standby_private_connection" /> | `object` |  |
| <CopyableCode code="user" /> | `string` | The name of the user for use with the connection pool. When excluded, all sessions connect to the database as the inbound user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_connection_pool" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, pool_name" /> | To show information about an existing connection pool for a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. The response will be a JSON object with a `pool` key. |
| <CopyableCode code="databases_list_connection_pools" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`. The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects. |
| <CopyableCode code="databases_add_connection_pool" /> | `INSERT` | <CopyableCode code="database_cluster_uuid, data__db, data__mode, data__name, data__size" /> | For PostgreSQL database clusters, connection pools can be used to allow a database to share its idle connections. The popular PostgreSQL connection pooling utility PgBouncer is used to provide this service. [See here for more information](https://docs.digitalocean.com/products/databases/postgresql/how-to/manage-connection-pools/) about how and why to use PgBouncer connection pooling including details about the available transaction modes. To add a new connection pool to a PostgreSQL database cluster, send a POST request to `/v2/databases/$DATABASE_ID/pools` specifying a name for the pool, the user to connect with, the database to connect to, as well as its desired size and transaction mode. |
| <CopyableCode code="databases_delete_connection_pool" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, pool_name" /> | To delete a specific connection pool for a PostgreSQL database cluster, send a DELETE request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="databases_update_connection_pool" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, pool_name, data__db, data__mode, data__size" /> | To update a connection pool for a PostgreSQL database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. |

## `SELECT` examples

To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`. The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects.


```sql
SELECT
name,
connection,
db,
mode,
private_connection,
size,
standby_connection,
standby_private_connection,
user
FROM digitalocean.databases.pools
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pools</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.databases.pools (
data__name,
data__mode,
data__size,
data__db,
data__user,
database_cluster_uuid
)
SELECT 
'{{ name }}',
'{{ mode }}',
'{{ size }}',
'{{ db }}',
'{{ user }}',
'{{ database_cluster_uuid }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.databases.pools (
data__name,
data__mode,
data__size,
data__db,
database_cluster_uuid
)
SELECT 
'{{ name }}',
'{{ mode }}',
'{{ size }}',
'{{ db }}',
'{{ database_cluster_uuid }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: pools
  props:
    - name: database_cluster_uuid
      value: string
    - name: data__db
      value: string
    - name: data__mode
      value: string
    - name: data__name
      value: string
    - name: data__size
      value: string
    - name: name
      value: string
    - name: mode
      value: string
    - name: size
      value: integer
    - name: db
      value: string
    - name: user
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>pools</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.pools
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND pool_name = '{{ pool_name }}';
```
