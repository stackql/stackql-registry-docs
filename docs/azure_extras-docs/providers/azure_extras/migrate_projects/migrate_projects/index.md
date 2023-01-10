---
title: migrate_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - migrate_projects
  - migrate_projects
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>migrate_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate_projects.migrate_projects</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MigrateProjects_DeleteMigrateProject` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` | Delete the migrate project. Deleting non-existent project is a no-operation. |
| `MigrateProjects_GetMigrateProject` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `MigrateProjects_PatchMigrateProject` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` | Update a migrate project with specified name. Supports partial updates, for example only tags can be provided. |
| `MigrateProjects_PutMigrateProject` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `MigrateProjects_RefreshMigrateProjectSummary` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `MigrateProjects_RegisterTool` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
