---
title: firmware
hide_title: false
hide_table_of_contents: false
keywords:
  - firmware
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
<tr><td><b>Name</b></td><td><code>firmware</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_firmware_defense.firmware</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | Get firmware. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists all of firmwares inside a workspace. |
| `create` | `INSERT` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to create a firmware. |
| `delete` | `DELETE` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to delete a firmware. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists all of firmwares inside a workspace. |
| `generate_binary_hardening_details` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to get binary hardening details for a firmware. |
| `generate_binary_hardening_summary` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to list the binary hardening summary percentages for a firmware. |
| `generate_component_details` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to get component details for a firmware. |
| `generate_crypto_certificate_summary` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to provide a high level summary of the discovered cryptographic certificates reported for the firmware image. |
| `generate_crypto_key_summary` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to provide a high level summary of the discovered cryptographic keys reported for the firmware image. |
| `generate_cve_summary` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to provide a high level summary of the CVEs reported for the firmware image. |
| `generate_download_url` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to a url for file download. |
| `generate_filesystem_download_url` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to a url for tar file download. |
| `generate_summary` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to get a scan summary. |
| `update` | `EXEC` | `firmwareId, resourceGroupName, subscriptionId, workspaceName` | The operation to update firmware. |
