---
title: management_group_subscriptions_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_subscriptions_subscription
  - management_groups
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
<tr><td><b>Name</b></td><td><code>management_group_subscriptions_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.management_groups.management_group_subscriptions_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the subscription.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/subscriptions/0000000-0000-0000-0000-000000000001 |
| `name` | `string` | The stringified id of the subscription. For example, 00000000-0000-0000-0000-000000000000 |
| `properties` | `object` | The generic properties of subscription under a management group. |
| `type` | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups/subscriptions |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `groupId, subscriptionId` |
