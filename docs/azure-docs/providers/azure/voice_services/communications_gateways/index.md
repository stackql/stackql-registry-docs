---
title: communications_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - communications_gateways
  - voice_services
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
<tr><td><b>Name</b></td><td><code>communications_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.voice_services.communications_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Details of the CommunicationsGateway resource. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `communicationsGatewayName, resourceGroupName, subscriptionId` | Get a CommunicationsGateway |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List CommunicationsGateway resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List CommunicationsGateway resources by subscription ID |
| `create_or_update` | `INSERT` | `communicationsGatewayName, resourceGroupName, subscriptionId` | Create a CommunicationsGateway |
| `delete` | `DELETE` | `communicationsGatewayName, resourceGroupName, subscriptionId` | Delete a CommunicationsGateway |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List CommunicationsGateway resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List CommunicationsGateway resources by subscription ID |
| `update` | `EXEC` | `communicationsGatewayName, resourceGroupName, subscriptionId` | Update a CommunicationsGateway |
