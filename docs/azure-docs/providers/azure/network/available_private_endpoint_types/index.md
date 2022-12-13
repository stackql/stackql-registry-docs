---
title: available_private_endpoint_types
hide_title: false
hide_table_of_contents: false
keywords:
  - available_private_endpoint_types
  - network
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
<tr><td><b>Name</b></td><td><code>available_private_endpoint_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.available_private_endpoint_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique identifier of the AvailablePrivateEndpoint Type resource. |
| `name` | `string` | The name of the service and resource. |
| `displayName` | `string` | Display name of the resource. |
| `resourceName` | `string` | The name of the service and resource. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AvailablePrivateEndpointTypes_List` | `SELECT` | `location, subscriptionId` |
| `AvailablePrivateEndpointTypes_ListByResourceGroup` | `SELECT` | `location, resourceGroupName, subscriptionId` |
