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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_core_control_plane_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_core_control_plane_versions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="versionName" /> | Gets information about the specified packet core control plane version. |
| <CopyableCode code="list" /> | `SELECT` |  | Lists all supported packet core control planes versions. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all supported packet core control planes versions. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists all supported packet core control planes versions. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all supported packet core control planes versions. |
| <CopyableCode code="get_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId, versionName" /> | Gets information about the specified packet core control plane version. |
