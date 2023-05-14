---
title: postgresql_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - postgresql_instances
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
<tr><td><b>Name</b></td><td><code>postgresql_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.databases.postgresql_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique ID that can be used to identify and reference the Managed Database. |
| `ssl_connection` | `boolean` | Whether to require SSL credentials to establish a connection to the Managed Database.<br /><br />Use the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/&#123;instanceId&#125;/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command for access information.<br /> |
| `type` | `string` | The Linode Instance type used by the Managed Database for its nodes. |
| `updates` | `object` | Configuration settings for automated patch update maintenance for the Managed Database. |
| `replication_type` | `string` | The replication method used for the Managed Database.<br /><br />Defaults to `none` for a single cluster and `semi_synch` for a high availability cluster.<br /><br />Must be `none` for a single node cluster.<br /><br />Must be `asynch` or `semi_synch` for a high availability cluster.<br /> |
| `allow_list` | `array` | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.<br /><br />By default, this is an empty array (`[]`), which blocks all connections (both public and private) to the Managed Database.<br /><br />If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /> |
| `cluster_size` | `integer` | The number of Linode Instance nodes deployed to the Managed Database.<br /><br />Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.<br /> |
| `version` | `string` | The Managed Database engine version. |
| `replication_commit_type` | `string` | The synchronization level of the replicating server.<br /><br />Must be `local` or `off` for the `asynch` replication type.<br /><br />Must be `on`, `remote_write`, or `remote_apply` for the `semi_synch` replication type.<br /> |
| `encrypted` | `boolean` | Whether the Managed Databases is encrypted. |
| `engine` | `string` | The Managed Database engine type. |
| `created` | `string` | When this Managed Database was created. |
| `status` | `string` | The operating status of the Managed Database. |
| `label` | `string` | A unique, user-defined string referring to the Managed Database. |
| `region` | `string` | The [Region](/docs/api/regions/) ID for the Managed Database. |
| `hosts` | `object` | The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete. |
| `updated` | `string` | When this Managed Database was last updated. |
| `port` | `integer` | The access port for this Managed Database. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDatabasesPostgreSQLInstance` | `SELECT` | `instanceId` | Display information for a single, accessible Managed PostgreSQL Database.<br /> |
| `getDatabasesPostgreSQLInstances` | `SELECT` |  | Display all accessible Managed PostgreSQL Databases.<br /> |
| `deleteDatabasesPostgreSQLInstance` | `DELETE` | `instanceId` | Remove a Managed PostgreSQL Database from your Account.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active`, `failed`, or `degraded` status to perform this command.<br /><br />Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.<br /> |
| `_getDatabasesPostgreSQLInstance` | `EXEC` | `instanceId` | Display information for a single, accessible Managed PostgreSQL Database.<br /> |
| `_getDatabasesPostgreSQLInstances` | `EXEC` |  | Display all accessible Managed PostgreSQL Databases.<br /> |
| `postDatabasesPostgreSQLInstancePatch` | `EXEC` | `instanceId` | Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/&#123;instanceId&#125;](/docs/api/databases/#managed-postgresql-database-update)) command.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />**Note**<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.<br /> |
| `postDatabasesPostgreSQLInstances` | `EXEC` | `data__engine, data__label, data__region, data__type` | Provision a Managed PostgreSQL Database.<br /><br />Restricted Users must have the `add_databases` grant to use this command.<br /><br />New instances can take approximately 15 to 30 minutes to provision.<br /><br />The `allow_list` is used to control access to the Managed Database.<br /><br />* IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.<br /><br />* If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /><br />* Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.<br /><br />All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.<br /><br />All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.<br /><br />* To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/&#123;instanceId&#125;](/docs/api/databases/#managed-postgresql-database-update)) command.<br /> |
| `putDatabasesPostgreSQLInstance` | `EXEC` | `instanceId` | Update a Managed PostgreSQL Database.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />Updating addresses in the `allow_list` overwrites any existing addresses.<br /><br />* IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.<br /><br />* If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /><br />* Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.<br /><br />* **Note**: Updates to the `allow_list` may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.<br /><br />All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.<br /> |
