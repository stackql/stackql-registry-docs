---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - traffic_manager
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.traffic_manager.endpoints</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointName, endpointType, profileName, resourceGroupName, subscriptionId` | Gets a Traffic Manager endpoint. |
| `create_or_update` | `INSERT` | `endpointName, endpointType, profileName, resourceGroupName, subscriptionId` | Create or update a Traffic Manager endpoint. |
| `delete` | `DELETE` | `endpointName, endpointType, profileName, resourceGroupName, subscriptionId` | Deletes a Traffic Manager endpoint. |
| `update` | `EXEC` | `endpointName, endpointType, profileName, resourceGroupName, subscriptionId` | Update a Traffic Manager endpoint. |
