---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - web_pub_sub
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
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pub_sub.hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a hub. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebPubSubHubs_Get` | `SELECT` | `hubName, resourceGroupName, resourceName, subscriptionId` | Get a hub setting. |
| `WebPubSubHubs_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List hub settings. |
| `WebPubSubHubs_CreateOrUpdate` | `INSERT` | `hubName, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update a hub setting. |
| `WebPubSubHubs_Delete` | `DELETE` | `hubName, resourceGroupName, resourceName, subscriptionId` | Delete a hub setting. |
