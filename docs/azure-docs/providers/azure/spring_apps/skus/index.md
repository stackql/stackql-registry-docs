---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - spring_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets the name of SKU. |
| <CopyableCode code="capacity" /> | `object` | The SKU capacity |
| <CopyableCode code="locationInfo" /> | `array` | Gets a list of locations and availability zones in those locations where the SKU is available. |
| <CopyableCode code="locations" /> | `array` | Gets the set of locations that the SKU is available. |
| <CopyableCode code="resourceType" /> | `string` | Gets the type of resource the SKU applies to. |
| <CopyableCode code="restrictions" /> | `array` | Gets the restrictions because of which SKU cannot be used. This is<br />empty if there are no restrictions. |
| <CopyableCode code="tier" /> | `string` | Gets the tier of SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
