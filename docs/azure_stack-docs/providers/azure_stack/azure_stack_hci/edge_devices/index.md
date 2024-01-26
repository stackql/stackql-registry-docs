---
title: edge_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_devices
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>edge_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.edge_devices</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `edgeDeviceName, resourceUri` | Get a EdgeDevice |
| `list` | `SELECT` | `resourceUri` | List EdgeDevice resources by parent |
| `create_or_update` | `INSERT` | `edgeDeviceName, resourceUri` | Create a EdgeDevice |
| `delete` | `DELETE` | `edgeDeviceName, resourceUri` | Delete a EdgeDevice |
| `_list` | `EXEC` | `resourceUri` | List EdgeDevice resources by parent |
| `validate` | `EXEC` | `edgeDeviceName, resourceUri, data__edgeDeviceIds` | A long-running resource action. |
