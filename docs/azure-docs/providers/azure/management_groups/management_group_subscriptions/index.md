---
title: management_group_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_subscriptions
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
<tr><td><b>Name</b></td><td><code>management_group_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.management_groups.management_group_subscriptions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementGroupSubscriptions_Create` | `INSERT` | `groupId, subscriptionId` | Associates existing subscription with the management group.<br /> |
| `ManagementGroupSubscriptions_Delete` | `DELETE` | `groupId, subscriptionId` | De-associates subscription from the management group.<br /> |
| `ManagementGroupSubscriptions_GetSubscription` | `EXEC` | `groupId, subscriptionId` | Retrieves details about given subscription which is associated with the management group.<br /> |
| `ManagementGroupSubscriptions_GetSubscriptionsUnderManagementGroup` | `EXEC` | `groupId` | Retrieves details about all subscriptions which are associated with the management group.<br /> |
