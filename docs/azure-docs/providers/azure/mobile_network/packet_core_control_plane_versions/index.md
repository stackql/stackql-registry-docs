---
title: packet_core_control_plane_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_control_plane_versions
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>packet_core_control_plane_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.packet_core_control_plane_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `versionName` | Gets information about the specified packet core control plane version. |
| `list` | `SELECT` |  | Lists all supported packet core control planes versions. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all supported packet core control planes versions. |
| `_list` | `EXEC` |  | Lists all supported packet core control planes versions. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all supported packet core control planes versions. |
| `get_by_subscription` | `EXEC` | `subscriptionId, versionName` | Gets information about the specified packet core control plane version. |
