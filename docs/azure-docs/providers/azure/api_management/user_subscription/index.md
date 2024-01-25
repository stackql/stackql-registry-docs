---
title: user_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - user_subscription
  - api_management
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
<tr><td><b>Name</b></td><td><code>user_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.user_subscription</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, sid, subscriptionId, userId` | Gets the specified Subscription entity associated with a particular user. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, userId` | Lists the collection of subscriptions of the specified user. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, userId` | Lists the collection of subscriptions of the specified user. |
