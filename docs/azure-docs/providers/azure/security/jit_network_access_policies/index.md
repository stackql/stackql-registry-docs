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
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `kind` | `string` | Kind of the resource |
| `location` | `string` | Location where the resource is stored |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JitNetworkAccessPolicies_Get` | `SELECT` | `api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `JitNetworkAccessPolicies_List` | `SELECT` | `api-version, subscriptionId` | Policies for protecting resources using Just-in-Time access control. |
| `JitNetworkAccessPolicies_ListByRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `JitNetworkAccessPolicies_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `JitNetworkAccessPolicies_ListByResourceGroupAndRegion` | `SELECT` | `api-version, ascLocation, resourceGroupName, subscriptionId` | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| `JitNetworkAccessPolicies_CreateOrUpdate` | `INSERT` | `api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__properties` | Create a policy for protecting resources using Just-in-Time access control |
| `JitNetworkAccessPolicies_Delete` | `DELETE` | `api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId` | Delete a Just-in-Time access control policy. |
| `JitNetworkAccessPolicies_Initiate` | `EXEC` | `api-version, ascLocation, jitNetworkAccessPolicyInitiateType, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__virtualMachines` | Initiate a JIT access from a specific Just-in-Time policy configuration. |
