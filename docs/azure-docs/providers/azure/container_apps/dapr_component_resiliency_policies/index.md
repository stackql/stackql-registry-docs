---
title: dapr_component_resiliency_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - dapr_component_resiliency_policies
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
<tr><td><b>Name</b></td><td><code>dapr_component_resiliency_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.dapr_component_resiliency_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `componentName, environmentName, name, resourceGroupName, subscriptionId` |  |
| `list` | `SELECT` | `componentName, environmentName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `componentName, environmentName, name, resourceGroupName, subscriptionId` | Creates or updates a resiliency policy for a Dapr component. |
| `delete` | `DELETE` | `componentName, environmentName, name, resourceGroupName, subscriptionId` | Delete a resiliency policy for a Dapr component. |
| `_list` | `EXEC` | `componentName, environmentName, resourceGroupName, subscriptionId` |  |
