---
title: mysql_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - mysql_instances
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
<tr><td><b>Name</b></td><td><code>mysql_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.databases.mysql_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique ID that can be used to identify and reference the Managed Database. |
| `updates` | `object` | Configuration settings for automated patch update maintenance for the Managed Database. |
| `allow_list` | `array` | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.<br /><br />By default, this is an empty array (`[]`), which blocks all connections (both public and private) to the Managed Database.<br /><br />If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /> |
| `created` | `string` | When this Managed Database was created. |
| `encrypted` | `boolean` | Whether the Managed Databases is encrypted. |
| `status` | `string` | The operating status of the Managed Database. |
| `replication_type` | `string` | The replication method used for the Managed Database.<br /><br />Defaults to `none` for a single cluster and `semi_synch` for a high availability cluster.<br /><br />Must be `none` for a single node cluster.<br /><br />Must be `asynch` or `semi_synch` for a high availability cluster.<br /> |
| `version` | `string` | The Managed Database engine version. |
| `ssl_connection` | `boolean` | Whether to require SSL credentials to establish a connection to the Managed Database.<br /><br />Use the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/&#123;instanceId&#125;/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command for access information.<br /> |
| `cluster_size` | `integer` | The number of Linode Instance nodes deployed to the Managed Database.<br /><br />Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.<br /> |
| `type` | `string` | The Linode Instance type used by the Managed Database for its nodes. |
| `engine` | `string` | The Managed Database engine type. |
| `region` | `string` | The [Region](/docs/api/regions/) ID for the Managed Database. |
| `port` | `integer` | The access port for this Managed Database. |
| `label` | `string` | A unique, user-defined string referring to the Managed Database. |
| `hosts` | `object` | The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete. |
| `updated` | `string` | When this Managed Database was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDatabasesMySQLInstance` | `SELECT` | `instanceId` | Display information for a single, accessible Managed MySQL Database.<br /> |
| `getDatabasesMySQLInstances` | `SELECT` |  | Display all accessible Managed MySQL Databases.<br /> |
| `deleteDatabasesMySQLInstance` | `DELETE` | `instanceId` | Remove a Managed MySQL Database from your Account.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active`, `failed`, or `degraded` status to perform this command.<br /><br />Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.<br /> |
| `_getDatabasesMySQLInstance` | `EXEC` | `instanceId` | Display information for a single, accessible Managed MySQL Database.<br /> |
| `_getDatabasesMySQLInstances` | `EXEC` |  | Display all accessible Managed MySQL Databases.<br /> |
| `postDatabasesMySQLInstancePatch` | `EXEC` | `instanceId` | Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/&#123;instanceId&#125;](/docs/api/databases/#managed-mysql-database-update)) command.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />**Note**<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.<br /> |
| `postDatabasesMySQLInstances` | `EXEC` | `data__engine, data__label, data__region, data__type` | Provision a Managed MySQL Database.<br /><br />Restricted Users must have the `add_databases` grant to use this command.<br /><br />New instances can take approximately 15 to 30 minutes to provision.<br /><br />The `allow_list` is used to control access to the Managed Database.<br /><br />* IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.<br /><br />* If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /><br />* Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.<br /><br />All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.<br /><br />All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.<br /><br />* To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/&#123;instanceId&#125;](/docs/api/databases/#managed-mysql-database-update)) command.<br /> |
| `putDatabasesMySQLInstance` | `EXEC` | `instanceId` | Update a Managed MySQL Database.<br /><br />Requires `read_write` access to the Database.<br /><br />The Database must have an `active` status to perform this command.<br /><br />Updating addresses in the `allow_list` overwrites any existing addresses.<br /><br />* IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.<br /><br />* If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /><br />* Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.<br /><br />* **Note**: Updates to the `allow_list` may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.<br /><br />All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.<br /><br />* If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.<br /><br />* **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.<br /> |
