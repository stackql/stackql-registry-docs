---
title: sql_migration_services_migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_migration_services_migrations
  - data_migration
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
<tr><td><b>Name</b></td><td><code>sql_migration_services_migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.sql_migration_services_migrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `properties` | `object` | Database Migration Resource properties. |
| `systemData` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, sqlMigrationServiceName, subscriptionId` |
