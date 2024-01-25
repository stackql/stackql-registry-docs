---
title: migrate_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - migrate_projects
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
<tr><td><b>Name</b></td><td><code>migrate_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate_projects.migrate_projects</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `patch_migrate_project` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` | Update a migrate project with specified name. Supports partial updates, for example only tags can be provided. |
| `put_migrate_project` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `refresh_migrate_project_summary` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `register_tool` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
