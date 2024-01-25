---
title: notification_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_hubs
  - notification_hubs
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
<tr><td><b>Name</b></td><td><code>notification_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.notification_hubs.notification_hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | NotificationHub properties. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__location` |
| `delete` | `DELETE` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` |
| `check_notification_hub_availability` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, data__name` |
| `debug_send` | `EXEC` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__policyKey` |
| `update` | `EXEC` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` |
