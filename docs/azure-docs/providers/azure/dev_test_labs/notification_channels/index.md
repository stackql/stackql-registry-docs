---
title: notification_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channels
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.notification_channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a schedule. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Get notification channel. |
| `list` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId` | List notification channels in a given lab. |
| `create_or_update` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, data__properties` | Create or replace an existing notification channel. |
| `delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId` | Delete notification channel. |
| `_list` | `EXEC` | `api-version, labName, resourceGroupName, subscriptionId` | List notification channels in a given lab. |
| `notify` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Send notification to provided channel. |
| `update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Allows modifying tags of notification channels. All other properties will be ignored. |
