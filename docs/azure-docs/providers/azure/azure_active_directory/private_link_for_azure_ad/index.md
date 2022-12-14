---
title: private_link_for_azure_ad
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_for_azure_ad
  - azure_active_directory
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
<tr><td><b>Name</b></td><td><code>private_link_for_azure_ad</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_active_directory.private_link_for_azure_ad</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `tags` | `object` | Resource tags. |
| `subscriptionId` | `string` | Subscription Identifier |
| `allTenants` | `boolean` | Flag indicating whether all tenants are allowed |
| `resourceGroup` | `string` | Name of the resource group |
| `ownerTenantId` | `string` | Guid of the owner tenant |
| `resourceName` | `string` | Name of the private link policy resource |
| `tenants` | `array` | The list of tenantIds. |
| `type` | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `privateLinkForAzureAd_Get` | `SELECT` | `policyName, resourceGroupName, subscriptionId` | Gets a private link policy with a given name. |
| `privateLinkForAzureAd_List` | `SELECT` | `resourceGroupName, subscriptionId` | Operation to return the list of Private Link Policies For AzureAD scoped to the resourceGroup. |
| `privateLinkForAzureAd_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all  Private Link Policies For AzureAD in the given subscription. |
| `privateLinkForAzureAd_Create` | `INSERT` | `policyName, resourceGroupName, subscriptionId` | Creates a private link policy. |
| `privateLinkForAzureAd_Delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId` | Deletes a private link policy. When operation completes, status code 200 returned without content. |
| `privateLinkForAzureAd_Update` | `EXEC` | `policyName, resourceGroupName, subscriptionId` | Updates private link policy tags with specified values. |
