---
title: gateway_hostname_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_hostname_configuration
  - api_management
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
<tr><td><b>Name</b></td><td><code>gateway_hostname_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway_hostname_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Gateway hostname configuration details. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GatewayHostnameConfiguration_Get` | `SELECT` | `gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Get details of a hostname configuration |
| `GatewayHostnameConfiguration_ListByService` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of hostname configurations for the specified gateway. |
| `GatewayHostnameConfiguration_CreateOrUpdate` | `INSERT` | `gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Creates of updates hostname configuration for a Gateway. |
| `GatewayHostnameConfiguration_Delete` | `DELETE` | `If-Match, gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified hostname configuration from the specified Gateway. |
| `GatewayHostnameConfiguration_GetEntityTag` | `EXEC` | `gatewayId, hcId, resourceGroupName, serviceName, subscriptionId` | Checks that hostname configuration entity specified by identifier exists for specified Gateway entity. |
