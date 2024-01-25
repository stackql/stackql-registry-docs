---
title: migrate_project
hide_title: false
hide_table_of_contents: false
keywords:
  - migrate_project
  - migrate_projects
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
<tr><td><b>Name</b></td><td><code>migrate_project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate_projects.migrate_project</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the relative URL to get this migrate project. |
| `name` | `string` | Gets the name of the migrate project. |
| `eTag` | `string` | Gets or sets the eTag for concurrency control. |
| `location` | `string` | Gets or sets the Azure location in which migrate project is created. |
| `properties` | `object` | Class for migrate project properties. |
| `tags` | `object` | Gets or sets the tags. |
| `type` | `string` | Handled by resource provider. Type = Microsoft.Migrate/MigrateProject. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `delete` | `DELETE` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` | Delete the migrate project. Deleting non-existent project is a no-operation. |
