---
title: resource_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>resource_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.resource_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of SKU. |
| <CopyableCode code="kind" /> | `string` | The Kind of resources that are supported in this SKU. |
| <CopyableCode code="locations" /> | `array` | The set of locations that the SKU is available. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the SKU applies to. |
| <CopyableCode code="restrictions" /> | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| <CopyableCode code="tier" /> | `string` | Specifies the tier of Cognitive Services account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
