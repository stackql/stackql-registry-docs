---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
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

Creates, updates, deletes, gets or lists a <code>replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.replicas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a database replica. |
| <CopyableCode code="name" /> | `string` | The name to give the read-only replicating |
| <CopyableCode code="connection" /> | `object` |  |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the database cluster was created. |
| <CopyableCode code="private_connection" /> | `object` |  |
| <CopyableCode code="private_network_uuid" /> | `string` | A string specifying the UUID of the VPC to which the read-only replica will be assigned. If excluded, the replica will be assigned to your account's default VPC for the region. |
| <CopyableCode code="region" /> | `string` | A slug identifier for the region where the read-only replica will be located. If excluded, the replica will be placed in the same region as the cluster. |
| <CopyableCode code="size" /> | `string` | A slug identifier representing the size of the node for the read-only replica. The size of the replica must be at least as large as the node size for the database cluster from which it is replicating. |
| <CopyableCode code="status" /> | `string` | A string representing the current status of the database cluster. |
| <CopyableCode code="storage_size_mib" /> | `integer` | Additional storage added to the cluster, in MiB. If null, no additional storage is added to the cluster, beyond what is provided as a base amount from the 'size' and any previously added additional storage. |
| <CopyableCode code="tags" /> | `array` | A flat array of tag names as strings to apply to the read-only replica after it is created. Tag names can either be existing or new tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_replica" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, replica_name" /> | To show information about an existing database replica, send a GET request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`. **Note**: Read-only replicas are not supported for Redis clusters. The response will be a JSON object with a `replica key`. This will be set to an object containing the standard database replica attributes. |
| <CopyableCode code="databases_list_replicas" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`. **Note**: Read-only replicas are not supported for Redis clusters. The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes. |
| <CopyableCode code="databases_create_replica" /> | `INSERT` | <CopyableCode code="database_cluster_uuid, data__name" /> | To create a read-only replica for a PostgreSQL or MySQL database cluster, send a POST request to `/v2/databases/$DATABASE_ID/replicas` specifying the name it should be given, the size of the node to be used, and the region where it will be located. **Note**: Read-only replicas are not supported for Redis clusters. The response will be a JSON object with a key called `replica`. The value of this will be an object that contains the standard attributes associated with a database replica. The initial value of the read-only replica's `status` attribute will be `forking`. When the replica is ready to receive traffic, this will transition to `active`. |
| <CopyableCode code="databases_destroy_replica" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, replica_name" /> | To destroy a specific read-only replica, send a DELETE request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`. **Note**: Read-only replicas are not supported for Redis clusters. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="databases_promote_replica" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, replica_name" /> | To promote a specific read-only replica, send a PUT request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME/promote`. **Note**: Read-only replicas are not supported for Redis clusters. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |

## `SELECT` examples

To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`. **Note**: Read-only replicas are not supported for Redis clusters. The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes.


```sql
SELECT
id,
name,
connection,
created_at,
private_connection,
private_network_uuid,
region,
size,
status,
storage_size_mib,
tags
FROM digitalocean.databases.replicas
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replicas</code> resource.

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
INSERT INTO digitalocean.databases.replicas (
database_cluster_uuid,
data__name
)
SELECT 
'{{ database_cluster_uuid }}',
'{{ name }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: replicas
  props:
    - name: database_cluster_uuid
      value: string
    - name: data__name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>replicas</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.replicas
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND replica_name = '{{ replica_name }}';
```
