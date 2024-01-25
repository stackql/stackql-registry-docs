---
title: firmware_generate_binary_hardening_list
hide_title: false
hide_table_of_contents: false
keywords:
  - firmware_generate_binary_hardening_list
  - iot_firmware_defense
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
<tr><td><b>Name</b></td><td><code>firmware_generate_binary_hardening_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_firmware_defense.firmware_generate_binary_hardening_list</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The uri to fetch the next page of asset. |
| `value` | `array` | The list of binary hardening results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` |
