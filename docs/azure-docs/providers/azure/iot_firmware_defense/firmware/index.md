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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firmware</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_firmware_defense.firmware" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | Get firmware. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all of firmwares inside a workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to create a firmware. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to delete a firmware. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all of firmwares inside a workspace. |
| <CopyableCode code="generate_binary_hardening_details" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to get binary hardening details for a firmware. |
| <CopyableCode code="generate_binary_hardening_summary" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to list the binary hardening summary percentages for a firmware. |
| <CopyableCode code="generate_component_details" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to get component details for a firmware. |
| <CopyableCode code="generate_crypto_certificate_summary" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to provide a high level summary of the discovered cryptographic certificates reported for the firmware image. |
| <CopyableCode code="generate_crypto_key_summary" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to provide a high level summary of the discovered cryptographic keys reported for the firmware image. |
| <CopyableCode code="generate_cve_summary" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to provide a high level summary of the CVEs reported for the firmware image. |
| <CopyableCode code="generate_download_url" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to a url for file download. |
| <CopyableCode code="generate_filesystem_download_url" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to a url for tar file download. |
| <CopyableCode code="generate_summary" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to get a scan summary. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to update firmware. |
