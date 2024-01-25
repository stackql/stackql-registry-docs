---
title: steps
hide_title: false
hide_table_of_contents: false
keywords:
  - steps
  - deployment_manager
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
<tr><td><b>Name</b></td><td><code>steps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_manager.steps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a step resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, stepName, subscriptionId` |  |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `resourceGroupName, stepName, subscriptionId, data__properties` | Synchronously creates a new step or updates an existing step. |
| `delete` | `DELETE` | `resourceGroupName, stepName, subscriptionId` |  |
