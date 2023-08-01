---
title: mongodb_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - mongodb_instances
  - databases
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongodb_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.databases.mongodb_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique ID that can be used to identify and reference the Managed Database. |
| `version` | `string` | The Managed Database engine version. |
| `status` | `string` | The operating status of the Managed Database. |
| `engine` | `string` | The Managed Database engine type. |
| `allow_list` | `array` | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.<br /><br />By default, this is an empty array (`[]`), which blocks all connections (both public and private) to the Managed Database.<br /><br />If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /> |
| `port` | `integer` | The access port for this Managed Database. |
| `region` | `string` | The [Region](/docs/api/regions/) ID for the Managed Database. |
| `storage_engine` | `string` | The type of storage engine for this Database.<br /><br />**Note:** MMAPV1 is not available for MongoDB versions 4.0 and above.<br /> |
| `replica_set` | `string` | Label for configuring a MongoDB [replica set](https://www.mongodb.com/docs/manual/replication/). Choose the same label on multiple Databases to include them in the same replica set.<br /><br />If `null`, the Database is not included in any replica set.<br /> |
| `cluster_size` | `integer` | The number of Linode Instance nodes deployed to the Managed Database.<br /><br />Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.<br /> |
| `updated` | `string` | When this Managed Database was last updated. |
| `updates` | `object` | Configuration settings for automated patch update maintenance for the Managed Database. |
| `label` | `string` | A unique, user-defined string referring to the Managed Database. |
| `peers` | `array` | An array of peer addresses for this Database.<br /> |
| `encrypted` | `boolean` | Whether the Managed Databases is encrypted. |
| `type` | `string` | The Linode Instance type used by the Managed Database for its nodes. |
| `created` | `string` | When this Managed Database was created. |
| `ssl_connection` | `boolean` | Whether to require SSL credentials to establish a connection to the Managed Database.<br /><br />Use the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/&#123;instanceId&#125;/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command for access information.<br /> |
| `hosts` | `object` | The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete. |
| `compression_type` | `string` | The type of data compression for this Database.<br /><br />Snappy has a lower comparative compression ratio and resource consumption rate.<br /><br />Zlip has a higher comparative compression ratio and resource consumption rate.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDatabasesMongoDBInstance` | `SELECT` | `instanceId` | Display information for a single, accessible Managed MongoDB Database.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| `getDatabasesMongoDBInstances` | `SELECT` |  | Display all accessible Managed MongoDB Databases.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| `deleteDatabasesMongoDBInstance` | `DELETE` | `instanceId` | Remove a Managed MongoDB Database from your Account.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active`, `failed`, or `degraded` status to perform this command.<br /><br />Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| `_getDatabasesMongoDBInstance` | `EXEC` | `instanceId` | Display information for a single, accessible Managed MongoDB Database.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| `_getDatabasesMongoDBInstances` | `EXEC` |  | Display all accessible Managed MongoDB Databases.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| `postDatabasesMongoDBInstancePatch` | `EXEC` | `instanceId` | Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/&#123;instanceId&#125;](/docs/api/databases/#managed-mongodb-database-update)) command.<br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />**Note**:<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
| `putDatabasesMongoDBInstance` | `EXEC` | `instanceId` | Update a Managed MongoDB Database.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />Updating addresses in the `allow_list` overwrites any existing addresses.<br /><br />* IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.<br /><br />* If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /><br />* Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.<br /><br />* **Note**: Updates to the `allow_list` may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.<br /><br />All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.<br /><br />**Note**: New MongoDB Databases cannot currently be created.<br /> |
