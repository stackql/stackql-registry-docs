---
title: diagnostics_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics_packages
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostics_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.diagnostics_packages" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified diagnostics package. |
| <CopyableCode code="list_by_packet_core_control_plane" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Lists all the diagnostics packages under a packet core control plane. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Creates or updates a diagnostics package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified diagnostics package. |
