---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - container_apps
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
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.source_controls</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContainerAppsSourceControls_Get` | `SELECT` | `containerAppName, resourceGroupName, sourceControlName, subscriptionId` |  |
| `ContainerAppsSourceControls_ListByContainerApp` | `SELECT` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `ContainerAppsSourceControls_CreateOrUpdate` | `INSERT` | `containerAppName, resourceGroupName, sourceControlName, subscriptionId` | Create or update the SourceControl for a Container App. |
| `ContainerAppsSourceControls_Delete` | `DELETE` | `containerAppName, resourceGroupName, sourceControlName, subscriptionId` | Delete a Container App SourceControl. |
