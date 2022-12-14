---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.time_series_insights.access_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessPolicies_Get` | `SELECT` | `accessPolicyName, environmentName, resourceGroupName, subscriptionId` | Gets the access policy with the specified name in the specified environment. |
| `AccessPolicies_ListByEnvironment` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Lists all the available access policies associated with the environment. |
| `AccessPolicies_CreateOrUpdate` | `INSERT` | `accessPolicyName, environmentName, resourceGroupName, subscriptionId, data__properties` | Create or update an access policy in the specified environment. |
| `AccessPolicies_Delete` | `DELETE` | `accessPolicyName, environmentName, resourceGroupName, subscriptionId` | Deletes the access policy with the specified name in the specified subscription, resource group, and environment |
| `AccessPolicies_Update` | `EXEC` | `accessPolicyName, environmentName, resourceGroupName, subscriptionId` | Updates the access policy with the specified name in the specified subscription, resource group, and environment. |
