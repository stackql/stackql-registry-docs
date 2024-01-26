---
title: upgrade_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - upgrade_notifications
  - redis
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>upgrade_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redis.upgrade_notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of upgrade notification. |
| `timestamp` | `string` | Timestamp when upgrade notification occurred. |
| `upsellNotification` | `object` | Details about this upgrade notification |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `history, name, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `history, name, resourceGroupName, subscriptionId` |
