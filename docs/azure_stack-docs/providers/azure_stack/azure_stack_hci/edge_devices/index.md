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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.edge_devices" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="edgeDeviceName, resourceUri" /> | Get a EdgeDevice |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List EdgeDevice resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="edgeDeviceName, resourceUri" /> | Create a EdgeDevice |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="edgeDeviceName, resourceUri" /> | Delete a EdgeDevice |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceUri" /> | List EdgeDevice resources by parent |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="edgeDeviceName, resourceUri, data__edgeDeviceIds" /> | A long-running resource action. |
