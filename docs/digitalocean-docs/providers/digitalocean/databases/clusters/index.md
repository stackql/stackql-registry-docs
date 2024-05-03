---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a database cluster. |
| <CopyableCode code="name" /> | `string` | A unique, human-readable name referring to a database cluster. |
| <CopyableCode code="connection" /> | `object` |  |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the database cluster was created. |
| <CopyableCode code="db_names" /> | `array` | An array of strings containing the names of databases created in the database cluster. |
| <CopyableCode code="engine" /> | `string` | A slug representing the database engine used for the cluster. The possible values are: "pg" for PostgreSQL, "mysql" for MySQL, "redis" for Redis, and "mongodb" for MongoDB. |
| <CopyableCode code="maintenance_window" /> | `object` |  |
| <CopyableCode code="num_nodes" /> | `integer` | The number of nodes in the database cluster. |
| <CopyableCode code="private_connection" /> | `object` |  |
| <CopyableCode code="private_network_uuid" /> | `string` | A string specifying the UUID of the VPC to which the database cluster will be assigned. If excluded, the cluster when creating a new database cluster, it will be assigned to your account's default VPC for the region. |
| <CopyableCode code="project_id" /> | `string` | The ID of the project that the database cluster is assigned to. If excluded when creating a new database cluster, it will be assigned to your default project. |
| <CopyableCode code="region" /> | `string` | The slug identifier for the region where the database cluster is located. |
| <CopyableCode code="rules" /> | `array` |  |
| <CopyableCode code="size" /> | `string` | The slug identifier representing the size of the nodes in the database cluster. |
| <CopyableCode code="status" /> | `string` | A string representing the current status of the database cluster. |
| <CopyableCode code="tags" /> | `array` | An array of tags that have been applied to the database cluster. |
| <CopyableCode code="users" /> | `array` |  |
| <CopyableCode code="version" /> | `string` | A string representing the version of the database engine in use for the cluster. |
| <CopyableCode code="version_end_of_availability" /> | `string` | A timestamp referring to the date when the particular version will no longer be available for creating new clusters. If null, the version does not have an end of availability timeline. |
| <CopyableCode code="version_end_of_life" /> | `string` | A timestamp referring to the date when the particular version will no longer be supported. If null, the version does not have an end of life timeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cluster" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID`.<br />The response will be a JSON object with a database key. This will be set to an object containing the standard database cluster attributes.<br />The embedded connection and private_connection objects will contain the information needed to access the database cluster.<br />The embedded maintenance_window object will contain information about any scheduled maintenance for the database cluster. |
| <CopyableCode code="list_clusters" /> | `SELECT` |  | To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`.<br />The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes.<br />The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster:<br />The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster. |
| <CopyableCode code="create_cluster" /> | `INSERT` |  | To create a database cluster, send a POST request to `/v2/databases`.<br />The response will be a JSON object with a key called `database`. The value of this will be an object that contains the standard attributes associated with a database cluster. The initial value of the database cluster's `status` attribute will be `creating`. When the cluster is ready to receive traffic, this will transition to `online`.<br />The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster.<br />DigitalOcean managed PostgreSQL and MySQL database clusters take automated daily backups. To create a new database cluster based on a backup of an existing cluster, send a POST request to `/v2/databases`. In addition to the standard database cluster attributes, the JSON body must include a key named `backup_restore` with the name of the original database cluster and the timestamp of the backup to be restored. Creating a database from a backup is the same as forking a database in the control panel.<br />Note: Backups are not supported for Redis clusters. |
| <CopyableCode code="_get_cluster" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID`.<br />The response will be a JSON object with a database key. This will be set to an object containing the standard database cluster attributes.<br />The embedded connection and private_connection objects will contain the information needed to access the database cluster.<br />The embedded maintenance_window object will contain information about any scheduled maintenance for the database cluster. |
| <CopyableCode code="_list_clusters" /> | `EXEC` |  | To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`.<br />The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes.<br />The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster:<br />The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster. |
| <CopyableCode code="destroy_cluster" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To destroy a specific database, send a DELETE request to `/v2/databases/$DATABASE_ID`.<br />A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="get_evictionPolicy" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To retrieve the configured eviction policy for an existing Redis cluster, send a GET request to `/v2/databases/$DATABASE_ID/eviction_policy`.<br />The response will be a JSON object with an `eviction_policy` key. This will be set to a string representing the eviction policy. |
| <CopyableCode code="update_clusterSize" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__num_nodes, data__size" /> | To resize a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/resize`. The body of the request must specify both the size and num_nodes attributes.<br />A successful request will receive a 202 Accepted status code with no body in response. Querying the database cluster will show that its status attribute will now be set to resizing. This will transition back to online when the resize operation has completed. |
| <CopyableCode code="update_evictionPolicy" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__eviction_policy" /> | To configure an eviction policy for an existing Redis cluster, send a PUT request to `/v2/databases/$DATABASE_ID/eviction_policy` specifying the desired policy. |
| <CopyableCode code="update_maintenanceWindow" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__day, data__hour" /> | To configure the window when automatic maintenance should be performed for a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/maintenance`.<br />A successful request will receive a 204 No Content status code with no body in response. |
