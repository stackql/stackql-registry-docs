---
title: compute_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_policies
  - data_lake_analytics
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
<tr><td><b>Name</b></td><td><code>compute_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_analytics.compute_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The compute policy properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ComputePolicies_Get` | `SELECT` | `accountName, computePolicyName, resourceGroupName, subscriptionId` | Gets the specified Data Lake Analytics compute policy. |
| `ComputePolicies_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists the Data Lake Analytics compute policies within the specified Data Lake Analytics account. An account supports, at most, 50 policies |
| `ComputePolicies_CreateOrUpdate` | `INSERT` | `accountName, computePolicyName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the specified compute policy. During update, the compute policy with the specified name will be replaced with this new compute policy. An account supports, at most, 50 policies |
| `ComputePolicies_Delete` | `DELETE` | `accountName, computePolicyName, resourceGroupName, subscriptionId` | Deletes the specified compute policy from the specified Data Lake Analytics account |
| `ComputePolicies_Update` | `EXEC` | `accountName, computePolicyName, resourceGroupName, subscriptionId` | Updates the specified compute policy. |
