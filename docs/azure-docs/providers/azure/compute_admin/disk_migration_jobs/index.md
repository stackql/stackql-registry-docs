---
title: disk_migration_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_migration_jobs
  - compute_admin
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_migration_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute_admin.disk_migration_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Disk migration job properties. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiskMigrationJobs_Get` | `SELECT` | `location, migrationId, subscriptionId` | Returns the requested disk migration job. |
| `DiskMigrationJobs_List` | `SELECT` | `location, subscriptionId` | Returns a list of disk migration jobs. |
| `DiskMigrationJobs_Create` | `INSERT` | `location, migrationId, subscriptionId` | Create a disk migration job. |
| `DiskMigrationJobs_Cancel` | `EXEC` | `location, migrationId, subscriptionId` | Cancel a disk migration job. |
