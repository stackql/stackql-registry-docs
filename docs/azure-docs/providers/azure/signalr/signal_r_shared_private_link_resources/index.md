---
title: signal_r_shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_shared_private_link_resources
  - signalr
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
<tr><td><b>Name</b></td><td><code>signal_r_shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.signalr.signal_r_shared_private_link_resources</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId` | Get the specified shared private link resource |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List shared private link resources |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId` | Create or update a shared private link resource |
| `delete` | `DELETE` | `resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId` | Delete the specified shared private link resource |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List shared private link resources |
