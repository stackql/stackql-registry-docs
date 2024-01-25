---
title: dapr_components
hide_title: false
hide_table_of_contents: false
keywords:
  - dapr_components
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
<tr><td><b>Name</b></td><td><code>dapr_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.dapr_components</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `componentName, environmentName, resourceGroupName, subscriptionId` |  |
| `list` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `componentName, environmentName, resourceGroupName, subscriptionId` | Creates or updates a Dapr Component in a Managed Environment. |
| `delete` | `DELETE` | `componentName, environmentName, resourceGroupName, subscriptionId` | Delete a Dapr Component from a Managed Environment. |
| `_list` | `EXEC` | `environmentName, resourceGroupName, subscriptionId` |  |
