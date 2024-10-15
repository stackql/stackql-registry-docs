---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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

Creates, updates, deletes, gets or lists a <code>models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The description of the model. |
| <CopyableCode code="kind" /> | `string` | The kind (type) of cognitive service account. |
| <CopyableCode code="model" /> | `object` | Cognitive Services account Model. |
| <CopyableCode code="skuName" /> | `string` | The name of SKU. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List Models. |
| <CopyableCode code="calculate_capacity" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Model capacity calculator. |

## `SELECT` examples

List Models.


```sql
SELECT
description,
kind,
model,
skuName
FROM azure.cognitive_services.models
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```