---
title: scale_units
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units
  - fabric_admin
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
<tr><td><b>Name</b></td><td><code>scale_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.scale_units" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Properties of a scale unit. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Returns the requested scale unit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all scale units at a location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Add a new scale unit. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all scale units at a location. |
| <CopyableCode code="scale_out" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Scales out a scale unit. |
| <CopyableCode code="set_gpu_partition_size" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnit, subscriptionId" /> | Set GPU partition size. |
