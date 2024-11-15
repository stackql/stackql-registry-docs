---
title: dbs
hide_title: false
hide_table_of_contents: false
keywords:
  - dbs
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

Creates, updates, deletes, gets or lists a <code>dbs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.dbs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the database. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, database_name" /> | To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID/dbs/$DB_NAME`. Note: Database management is not supported for Redis clusters. The response will be a JSON object with a `db` key. This will be set to an object containing the standard database attributes. |
| <CopyableCode code="databases_list" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the databases in a clusters, send a GET request to `/v2/databases/$DATABASE_ID/dbs`. The result will be a JSON object with a `dbs` key. This will be set to an array of database objects, each of which will contain the standard database attributes. Note: Database management is not supported for Redis clusters. |
| <CopyableCode code="databases_add" /> | `INSERT` | <CopyableCode code="database_cluster_uuid, data__name" /> | To add a new database to an existing cluster, send a POST request to `/v2/databases/$DATABASE_ID/dbs`. Note: Database management is not supported for Redis clusters. The response will be a JSON object with a key called `db`. The value of this will be an object that contains the standard attributes associated with a database. |
| <CopyableCode code="databases_delete" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, database_name" /> | To delete a specific database, send a DELETE request to `/v2/databases/$DATABASE_ID/dbs/$DB_NAME`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. Note: Database management is not supported for Redis clusters. |

## `SELECT` examples

To list all of the databases in a clusters, send a GET request to `/v2/databases/$DATABASE_ID/dbs`. The result will be a JSON object with a `dbs` key. This will be set to an array of database objects, each of which will contain the standard database attributes. Note: Database management is not supported for Redis clusters.


```sql
SELECT
name
FROM digitalocean.databases.dbs
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dbs</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.databases.dbs (
data__name,
database_cluster_uuid
)
SELECT 
'{{ name }}',
'{{ database_cluster_uuid }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: dbs
  props:
    - name: database_cluster_uuid
      value: string
    - name: data__name
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dbs</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.dbs
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND database_name = '{{ database_name }}';
```
