---
title: subscription_level
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_level
  - saas
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>subscription_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.saas.subscription_level</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource uri |
| `name` | `string` | The name of the resource |
| `properties` | `object` | saas properties |
| `tags` | `object` | the resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SaasSubscriptionLevel_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets information about the specified Subscription Level SaaS. |
| `SaasSubscriptionLevel_ListByAzureSubscription` | `SELECT` | `subscriptionId` | Gets information about all the Subscription Level SaaS in a certain Azure subscription. |
| `SaasSubscriptionLevel_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about all the Subscription Level SaaS in a certain resource group. |
| `SaasSubscriptionLevel_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates or updates a SaaS resource. |
| `SaasSubscriptionLevel_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the specified SaaS. |
| `SaasSubscriptionLevel_MoveResources` | `EXEC` | `resourceGroupName, subscriptionId` | Move a specified Subscription Level SaaS. |
| `SaasSubscriptionLevel_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a SaaS Subscription Level resource. |
| `SaasSubscriptionLevel_UpdateToUnsubscribed` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Unsubscribe from a specified Subscription Level SaaS. |
| `SaasSubscriptionLevel_ValidateMoveResources` | `EXEC` | `resourceGroupName, subscriptionId` | Validate whether a specified Subscription Level SaaS can be moved. |
| `SaasSubscriptionLevel_listAccessToken` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets the ISV access token for a specified Subscription Level SaaS. |
