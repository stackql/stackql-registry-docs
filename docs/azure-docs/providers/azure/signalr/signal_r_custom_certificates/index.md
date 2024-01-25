---
title: signal_r_custom_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_custom_certificates
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
<tr><td><b>Name</b></td><td><code>signal_r_custom_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.signalr.signal_r_custom_certificates</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateName, resourceGroupName, resourceName, subscriptionId` | Get a custom certificate. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List all custom certificates. |
| `create_or_update` | `INSERT` | `certificateName, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update a custom certificate. |
| `delete` | `DELETE` | `certificateName, resourceGroupName, resourceName, subscriptionId` | Delete a custom certificate. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List all custom certificates. |
