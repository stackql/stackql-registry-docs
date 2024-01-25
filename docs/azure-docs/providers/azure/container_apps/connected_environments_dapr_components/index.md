---
title: connected_environments_dapr_components
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_dapr_components
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
<tr><td><b>Name</b></td><td><code>connected_environments_dapr_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.connected_environments_dapr_components</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `componentName, connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `list` | `SELECT` | `connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `componentName, connectedEnvironmentName, resourceGroupName, subscriptionId` | Creates or updates a Dapr Component in a connected environment. |
| `delete` | `DELETE` | `componentName, connectedEnvironmentName, resourceGroupName, subscriptionId` | Delete a Dapr Component from a connected environment. |
| `_list` | `EXEC` | `connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
