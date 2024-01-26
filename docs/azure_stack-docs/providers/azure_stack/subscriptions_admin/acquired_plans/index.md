---
title: acquired_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - acquired_plans
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>acquired_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.acquired_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier in the tenant subscription context. |
| `acquisitionId` | `string` | Acquisition identifier. |
| `acquisitionTime` | `string` | Acquisition time. |
| `externalReferenceId` | `string` | External reference identifier. |
| `planId` | `string` | Plan identifier in the tenant subscription context. |
| `provisioningState` | `string` | Provisioning state for subscriptions service resources, for example, resource provider registration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `planAcquisitionId, subscriptionId, targetSubscriptionId` | Gets the specified plan acquired by a subscription consuming the offer. |
| `list` | `SELECT` | `subscriptionId, targetSubscriptionId` | Get a collection of all acquired plans that subscription has access to. |
| `create` | `INSERT` | `planAcquisitionId, subscriptionId, targetSubscriptionId` | Creates an acquired plan. |
| `delete` | `DELETE` | `planAcquisitionId, subscriptionId, targetSubscriptionId` | Deletes an acquired plan. |
| `_list` | `EXEC` | `subscriptionId, targetSubscriptionId` | Get a collection of all acquired plans that subscription has access to. |
