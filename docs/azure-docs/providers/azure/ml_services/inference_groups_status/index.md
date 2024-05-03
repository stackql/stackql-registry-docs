---
title: inference_groups_status
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_groups_status
  - ml_services
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
<tr><td><b>Name</b></td><td><code>inference_groups_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.inference_groups_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actualCapacityInfo" /> | `object` |  |
| <CopyableCode code="bonusExtraCapacity" /> | `integer` | Gets or sets capacity used from the pool's reserved capacity. |
| <CopyableCode code="endpointCount" /> | `integer` | Gets or sets the actual number of endpoints in the group. |
| <CopyableCode code="requestedCapacity" /> | `integer` | Gets or sets the request number of instances for the group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, poolName, resourceGroupName, subscriptionId, workspaceName" /> |
