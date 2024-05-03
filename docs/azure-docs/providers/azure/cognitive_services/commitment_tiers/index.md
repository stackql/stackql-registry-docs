---
title: commitment_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_tiers
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
<tr><td><b>Name</b></td><td><code>commitment_tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.commitment_tiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cost" /> | `object` | Cognitive Services account commitment cost. |
| <CopyableCode code="hostingModel" /> | `string` | Account hosting model. |
| <CopyableCode code="kind" /> | `string` | The kind (type) of cognitive service account. |
| <CopyableCode code="maxCount" /> | `integer` | Commitment period commitment max count. |
| <CopyableCode code="planType" /> | `string` | Commitment plan type. |
| <CopyableCode code="quota" /> | `object` | Cognitive Services account commitment quota. |
| <CopyableCode code="skuName" /> | `string` | The name of the SKU. Ex - P3. It is typically a letter+number code |
| <CopyableCode code="tier" /> | `string` | Commitment period commitment tier. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> |
