---
title: inference_pools_status
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_pools_status
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
<tr><td><b>Name</b></td><td><code>inference_pools_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.inference_pools_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actualCapacity" /> | `integer` | Gets or sets the actual number of instances in the pool. |
| <CopyableCode code="groupCount" /> | `integer` | Gets or sets the actual number of groups in the pool. |
| <CopyableCode code="requestedCapacity" /> | `integer` | Gets or sets the requested number of instances for the pool. |
| <CopyableCode code="reservedCapacity" /> | `integer` | Gets or sets the number of instances in the pool reserved by the system. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inferencePoolName, resourceGroupName, subscriptionId, workspaceName" /> |
