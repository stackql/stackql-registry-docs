---
title: sk_us
hide_title: false
hide_table_of_contents: false
keywords:
  - sk_us
  - engagement_fabric
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
<tr><td><b>Name</b></td><td><code>sk_us</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.engagement_fabric.sk_us" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU |
| <CopyableCode code="locationInfo" /> | `array` | Locations and zones |
| <CopyableCode code="locations" /> | `array` | The set of locations that the SKU is available |
| <CopyableCode code="resourceType" /> | `string` | The fully qualified resource type |
| <CopyableCode code="restrictions" /> | `array` | The restrictions because of which SKU cannot be used |
| <CopyableCode code="tier" /> | `string` | The price tier of the SKU |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
