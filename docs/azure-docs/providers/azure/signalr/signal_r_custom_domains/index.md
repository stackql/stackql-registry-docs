---
title: signal_r_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_custom_domains
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
<tr><td><b>Name</b></td><td><code>signal_r_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.signalr.signal_r_custom_domains</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, resourceName, subscriptionId` | Get a custom domain. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List all custom domains. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update a custom domain. |
| `delete` | `DELETE` | `name, resourceGroupName, resourceName, subscriptionId` | Delete a custom domain. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List all custom domains. |
