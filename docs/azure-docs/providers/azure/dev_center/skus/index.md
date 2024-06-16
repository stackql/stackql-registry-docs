---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - dev_center
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
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU. Ex - P3. It is typically a letter+number code |
| <CopyableCode code="capabilities" /> | `array` | Collection of name/value pairs to describe the SKU capabilities. |
| <CopyableCode code="capacity" /> | `integer` | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. |
| <CopyableCode code="family" /> | `string` | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| <CopyableCode code="locations" /> | `array` | SKU supported locations. |
| <CopyableCode code="resourceType" /> | `string` | The name of the resource type |
| <CopyableCode code="size" /> | `string` | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code.  |
| <CopyableCode code="tier" /> | `string` | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_subscription" /> | `SELECT` |  |
