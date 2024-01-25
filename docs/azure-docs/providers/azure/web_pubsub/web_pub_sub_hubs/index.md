---
title: web_pub_sub_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_hubs
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pubsub.web_pub_sub_hubs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, resourceGroupName, resourceName, subscriptionId` | Get a hub setting. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List hub settings. |
| `create_or_update` | `INSERT` | `hubName, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update a hub setting. |
| `delete` | `DELETE` | `hubName, resourceGroupName, resourceName, subscriptionId` | Delete a hub setting. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List hub settings. |
