---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
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
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate_projects.machines</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Machines_EnumerateMachines` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |
| `Machines_GetMachine` | `EXEC` | `api-version, machineName, migrateProjectName, resourceGroupName, subscriptionId` |
