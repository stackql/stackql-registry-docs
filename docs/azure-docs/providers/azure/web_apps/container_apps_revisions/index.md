---
title: container_apps_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_revisions
  - web_apps
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
<tr><td><b>Name</b></td><td><code>container_apps_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.container_apps_revisions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ContainerAppsRevisions_ActivateRevision` | `EXEC` | `containerAppName, name, resourceGroupName, subscriptionId` |
| `ContainerAppsRevisions_DeactivateRevision` | `EXEC` | `containerAppName, name, resourceGroupName, subscriptionId` |
| `ContainerAppsRevisions_GetRevision` | `EXEC` | `containerAppName, name, resourceGroupName, subscriptionId` |
| `ContainerAppsRevisions_ListRevisions` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` |
| `ContainerAppsRevisions_RestartRevision` | `EXEC` | `containerAppName, name, resourceGroupName, subscriptionId` |
