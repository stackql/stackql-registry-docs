---
title: changes
hide_title: false
hide_table_of_contents: false
keywords:
  - changes
  - resources
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
<tr><td><b>Name</b></td><td><code>changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.changes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID |
| `name` | `string` | Resource name |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `extendedLocation` | `object` | Resource extended location. |
| `location` | `string` | Resource location |
| `properties` | `object` | The properties of a change |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Changes_Get` | `SELECT` | `changeResourceId, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Obtains the specified change resource for the target resource |
| `Changes_List` | `SELECT` | `resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Obtains a list of change resources from the past 14 days for the target resource |
