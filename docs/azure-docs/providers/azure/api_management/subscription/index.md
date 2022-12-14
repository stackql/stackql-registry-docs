---
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
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
<tr><td><b>Name</b></td><td><code>subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Subscription details. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subscription_Get` | `SELECT` | `resourceGroupName, serviceName, sid, subscriptionId` | Gets the specified Subscription entity. |
| `Subscription_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all subscriptions of the API Management service instance. |
| `Subscription_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, sid, subscriptionId` | Creates or updates the subscription of specified user to the specified product. |
| `Subscription_Delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, sid, subscriptionId` | Deletes the specified subscription. |
| `Subscription_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Gets the entity state (Etag) version of the apimanagement subscription specified by its identifier. |
| `Subscription_ListSecrets` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Gets the specified Subscription keys. |
| `Subscription_RegeneratePrimaryKey` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Regenerates primary key of existing subscription of the API Management service instance. |
| `Subscription_RegenerateSecondaryKey` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Regenerates secondary key of existing subscription of the API Management service instance. |
| `Subscription_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, sid, subscriptionId` | Updates the details of a subscription specified by its identifier. |
