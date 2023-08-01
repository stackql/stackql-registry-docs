---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - event_grid
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `type` | `string` | Type of the resource. |
| `properties` | `object` | Properties of the Channel. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Channels_Get` | `SELECT` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Get properties of a channel. |
| `Channels_ListByPartnerNamespace` | `SELECT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | List all the channels in a partner namespace. |
| `Channels_CreateOrUpdate` | `INSERT` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Synchronously creates or updates a new channel with the specified parameters. |
| `Channels_Delete` | `DELETE` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Delete an existing channel. |
| `Channels_GetFullUrl` | `EXEC` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Get the full endpoint URL of a partner destination channel. |
| `Channels_Update` | `EXEC` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Synchronously updates a channel with the specified parameters. |
