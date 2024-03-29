---
title: jit_network_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_network_access_policies
  - security
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
<tr><td><b>Name</b></td><td><code>jit_network_access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.jit_network_access_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `kind` | `string` | Kind of the resource |
| `location` | `string` | Location where the resource is stored |
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `list` | `SELECT` | `api-version, subscriptionId` | Policies for protecting resources using Just-in-Time access control. |
| `list_by_region` | `SELECT` | `api-version, ascLocation, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `list_by_resource_group_and_region` | `SELECT` | `api-version, ascLocation, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `create_or_update` | `INSERT` | `api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__properties` | Create a policy for protecting resources using Just-in-Time access control |
| `delete` | `DELETE` | `api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId` | Delete a Just-in-Time access control policy. |
| `_list` | `EXEC` | `api-version, subscriptionId` | Policies for protecting resources using Just-in-Time access control. |
| `_list_by_region` | `EXEC` | `api-version, ascLocation, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `_list_by_resource_group_and_region` | `EXEC` | `api-version, ascLocation, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `initiate` | `EXEC` | `api-version, ascLocation, jitNetworkAccessPolicyInitiateType, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__virtualMachines` | Initiate a JIT access from a specific Just-in-Time policy configuration. |
