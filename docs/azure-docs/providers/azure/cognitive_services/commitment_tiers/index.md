---
title: commitment_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_tiers
  - cognitive_services
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>commitment_tiers</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List Commitment Tiers. |

## `SELECT` examples

List Commitment Tiers.


```sql
SELECT
cost,
hostingModel,
kind,
maxCount,
planType,
quota,
skuName,
tier
FROM azure.cognitive_services.commitment_tiers
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```