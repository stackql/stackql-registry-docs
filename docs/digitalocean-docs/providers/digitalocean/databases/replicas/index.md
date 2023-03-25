---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
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
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.databases.replicas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference a database replica. |
| `name` | `string` | The name to give the read-only replicating |
| `private_connection` | `object` |  |
| `private_network_uuid` | `string` | A string specifying the UUID of the VPC to which the read-only replica will be assigned. If excluded, the replica will be assigned to your account's default VPC for the region. |
| `region` | `string` | A slug identifier for the region where the read-only replica will be located. If excluded, the replica will be placed in the same region as the cluster. |
| `connection` | `object` |  |
| `size` | `string` | A slug identifier representing the size of the node for the read-only replica. The size of the replica must be at least as large as the node size for the database cluster from which it is replicating. |
| `status` | `string` | A string representing the current status of the database cluster. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the database cluster was created. |
| `tags` | `array` | A flat array of tag names as strings to apply to the read-only replica after it is created. Tag names can either be existing or new tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_replica` | `SELECT` | `database_cluster_uuid, replica_name` | To show information about an existing database replica, send a GET request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />The response will be a JSON object with a `replica key`. This will be set to an object containing the standard database replica attributes. |
| `list_replicas` | `SELECT` | `database_cluster_uuid` | To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes. |
| `create_replica` | `INSERT` | `database_cluster_uuid, data__name, data__size` | To create a read-only replica for a PostgreSQL or MySQL database cluster, send a POST request to `/v2/databases/$DATABASE_ID/replicas` specifying the name it should be given, the size of the node to be used, and the region where it will be located.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />The response will be a JSON object with a key called `replica`. The value of this will be an object that contains the standard attributes associated with a database replica. The initial value of the read-only replica's `status` attribute will be `forking`. When the replica is ready to receive traffic, this will transition to `active`. |
| `_get_replica` | `EXEC` | `database_cluster_uuid, replica_name` | To show information about an existing database replica, send a GET request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />The response will be a JSON object with a `replica key`. This will be set to an object containing the standard database replica attributes. |
| `_list_replicas` | `EXEC` | `database_cluster_uuid` | To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes. |
| `destroy_replica` | `EXEC` | `database_cluster_uuid, replica_name` | To destroy a specific read-only replica, send a DELETE request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| `promote_replica` | `EXEC` | `database_cluster_uuid, replica_name` | To promote a specific read-only replica, send a PUT request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME/promote`.<br /><br />**Note**: Read-only replicas are not supported for Redis clusters.<br /><br />A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
