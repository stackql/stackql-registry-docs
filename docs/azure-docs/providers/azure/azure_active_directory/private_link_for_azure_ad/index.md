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
| `allTenants` | `boolean` | Flag indicating whether all tenants are allowed |
| `ownerTenantId` | `string` | Guid of the owner tenant |
| `resourceGroup` | `string` | Name of the resource group |
| `resourceName` | `string` | Name of the private link policy resource |
| `subscriptionId` | `string` | Subscription Identifier |
| `tags` | `object` | Resource tags. |
| `tenants` | `array` | The list of tenantIds. |
| `type` | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyName, resourceGroupName, subscriptionId` | Gets a private link policy with a given name. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Operation to return the list of Private Link Policies For AzureAD scoped to the resourceGroup. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all  Private Link Policies For AzureAD in the given subscription. |
| `create` | `INSERT` | `policyName, resourceGroupName, subscriptionId` | Creates a private link policy. |
| `delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId` | Deletes a private link policy. When operation completes, status code 200 returned without content. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Operation to return the list of Private Link Policies For AzureAD scoped to the resourceGroup. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all  Private Link Policies For AzureAD in the given subscription. |
| `update` | `EXEC` | `policyName, resourceGroupName, subscriptionId` | Updates private link policy tags with specified values. |
