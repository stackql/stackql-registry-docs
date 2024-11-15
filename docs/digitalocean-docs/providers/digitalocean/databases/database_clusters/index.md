---
title: database_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - database_clusters
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

Creates, updates, deletes, gets or lists a <code>database_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.database_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a database cluster. |
| <CopyableCode code="name" /> | `string` | A unique, human-readable name referring to a database cluster. |
| <CopyableCode code="connection" /> | `object` |  |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the database cluster was created. |
| <CopyableCode code="db_names" /> | `array` | An array of strings containing the names of databases created in the database cluster. |
| <CopyableCode code="engine" /> | `string` | A slug representing the database engine used for the cluster. The possible values are: "pg" for PostgreSQL, "mysql" for MySQL, "redis" for Redis, "mongodb" for MongoDB, "kafka" for Kafka, and "opensearch" for OpenSearch. |
| <CopyableCode code="maintenance_window" /> | `object` |  |
| <CopyableCode code="metrics_endpoints" /> | `array` | Public hostname and port of the cluster's metrics endpoint(s). Includes one record for the cluster's primary node and a second entry for the cluster's standby node(s). |
| <CopyableCode code="num_nodes" /> | `integer` | The number of nodes in the database cluster. |
| <CopyableCode code="private_connection" /> | `object` |  |
| <CopyableCode code="private_network_uuid" /> | `string` | A string specifying the UUID of the VPC to which the database cluster will be assigned. If excluded, the cluster when creating a new database cluster, it will be assigned to your account's default VPC for the region. |
| <CopyableCode code="project_id" /> | `string` | The ID of the project that the database cluster is assigned to. If excluded when creating a new database cluster, it will be assigned to your default project. |
| <CopyableCode code="region" /> | `string` | The slug identifier for the region where the database cluster is located. |
| <CopyableCode code="rules" /> | `array` |  |
| <CopyableCode code="semantic_version" /> | `string` | A string representing the semantic version of the database engine in use for the cluster. |
| <CopyableCode code="size" /> | `string` | The slug identifier representing the size of the nodes in the database cluster. |
| <CopyableCode code="standby_connection" /> | `object` |  |
| <CopyableCode code="standby_private_connection" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | A string representing the current status of the database cluster. |
| <CopyableCode code="storage_size_mib" /> | `integer` | Additional storage added to the cluster, in MiB. If null, no additional storage is added to the cluster, beyond what is provided as a base amount from the 'size' and any previously added additional storage. |
| <CopyableCode code="tags" /> | `array` | An array of tags that have been applied to the database cluster. |
| <CopyableCode code="ui_connection" /> | `object` |  |
| <CopyableCode code="users" /> | `array` |  |
| <CopyableCode code="version" /> | `string` | A string representing the version of the database engine in use for the cluster. |
| <CopyableCode code="version_end_of_availability" /> | `string` | A timestamp referring to the date when the particular version will no longer be available for creating new clusters. If null, the version does not have an end of availability timeline. |
| <CopyableCode code="version_end_of_life" /> | `string` | A timestamp referring to the date when the particular version will no longer be supported. If null, the version does not have an end of life timeline. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_cluster" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID`. The response will be a JSON object with a database key. This will be set to an object containing the standard database cluster attributes. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster. For multi-node clusters, the `standby_connection` and `standby_private_connection` objects contain the information needed to connect to the cluster's standby node(s). The embedded maintenance_window object will contain information about any scheduled maintenance for the database cluster. |
| <CopyableCode code="databases_list_clusters" /> | `SELECT` | <CopyableCode code="" /> | To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`. The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster. For multi-node clusters, the `standby_connection` and `standby_private_connection` objects will contain the information needed to connect to the cluster's standby node(s). The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster. |
| <CopyableCode code="databases_create_cluster" /> | `INSERT` | <CopyableCode code="data__engine, data__name, data__num_nodes, data__region, data__size" /> | To create a database cluster, send a POST request to `/v2/databases`. The response will be a JSON object with a key called `database`. The value of this will be an object that contains the standard attributes associated with a database cluster. The initial value of the database cluster's `status` attribute will be `creating`. When the cluster is ready to receive traffic, this will transition to `online`. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster. For multi-node clusters, the `standby_connection` and `standby_private_connection` objects will contain the information needed to connect to the cluster's standby node(s). DigitalOcean managed PostgreSQL and MySQL database clusters take automated daily backups. To create a new database cluster based on a backup of an existing cluster, send a POST request to `/v2/databases`. In addition to the standard database cluster attributes, the JSON body must include a key named `backup_restore` with the name of the original database cluster and the timestamp of the backup to be restored. Creating a database from a backup is the same as forking a database in the control panel. Note: Backups are not supported for Redis clusters. |
| <CopyableCode code="databases_destroy_cluster" /> | `DELETE` | <CopyableCode code="database_cluster_uuid" /> | To destroy a specific database, send a DELETE request to `/v2/databases/$DATABASE_ID`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="databases_install_update" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To start the installation of updates for a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/install_update`. A successful request will receive a 204 No Content status code with no body in response. |
| <CopyableCode code="databases_update_cluster_size" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__num_nodes, data__size" /> | To resize a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/resize`. The body of the request must specify both the size and num_nodes attributes. A successful request will receive a 202 Accepted status code with no body in response. Querying the database cluster will show that its status attribute will now be set to resizing. This will transition back to online when the resize operation has completed. |
| <CopyableCode code="databases_update_maintenance_window" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__day, data__hour" /> | To configure the window when automatic maintenance should be performed for a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/maintenance`. A successful request will receive a 204 No Content status code with no body in response. |
| <CopyableCode code="databases_update_major_version" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To upgrade the major version of a database, send a PUT request to `/v2/databases/$DATABASE_ID/upgrade`, specifying the target version. A successful request will receive a 204 No Content status code with no body in response. |
| <CopyableCode code="databases_update_region" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__region" /> | To migrate a database cluster to a new region, send a `PUT` request to `/v2/databases/$DATABASE_ID/migrate`. The body of the request must specify a `region` attribute. A successful request will receive a 202 Accepted status code with no body in response. Querying the database cluster will show that its `status` attribute will now be set to `migrating`. This will transition back to `online` when the migration has completed. |

## `SELECT` examples

To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`. The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster. For multi-node clusters, the `standby_connection` and `standby_private_connection` objects will contain the information needed to connect to the cluster's standby node(s). The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster.


```sql
SELECT
id,
name,
connection,
created_at,
db_names,
engine,
maintenance_window,
metrics_endpoints,
num_nodes,
private_connection,
private_network_uuid,
project_id,
region,
rules,
semantic_version,
size,
standby_connection,
standby_private_connection,
status,
storage_size_mib,
tags,
ui_connection,
users,
version,
version_end_of_availability,
version_end_of_life
FROM digitalocean.databases.database_clusters
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_clusters</code> resource.

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
INSERT INTO digitalocean.databases.database_clusters (
data__backup_restore,
data__engine,
data__name,
data__num_nodes,
data__region,
data__size
)
SELECT 
'{{ backup_restore }}',
'{{ engine }}',
'{{ name }}',
'{{ num_nodes }}',
'{{ region }}',
'{{ size }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.databases.database_clusters (
data__name,
data__engine,
data__num_nodes,
data__size,
data__region
)
SELECT 
'{{ name }}',
'{{ engine }}',
'{{ num_nodes }}',
'{{ size }}',
'{{ region }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: database_clusters
  props:
    - name: data__engine
      value: string
    - name: data__name
      value: string
    - name: data__num_nodes
      value: string
    - name: data__region
      value: string
    - name: data__size
      value: string
    - name: backup_restore
      props:
        - name: database_name
          value: string
        - name: backup_created_at
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>database_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.database_clusters
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
