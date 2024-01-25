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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `containerAppName, resourceGroupName, sourceControlName, subscriptionId` |  |
| `list_by_container_app` | `SELECT` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `containerAppName, resourceGroupName, sourceControlName, subscriptionId` | Create or update the SourceControl for a Container App. |
| `delete` | `DELETE` | `containerAppName, resourceGroupName, sourceControlName, subscriptionId` | Delete a Container App SourceControl. |
| `_list_by_container_app` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` |  |
