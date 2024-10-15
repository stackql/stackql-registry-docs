---
title: model_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - model_capacities
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

Creates, updates, deletes, gets or lists a <code>model_capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.model_capacities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The location of the Model Sku Capacity. |
| <CopyableCode code="properties" /> | `object` | Cognitive Services account ModelSkuCapacity. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="modelFormat, modelName, modelVersion, subscriptionId" /> | List ModelCapacities. |

## `SELECT` examples

List ModelCapacities.


```sql
SELECT
location,
properties
FROM azure.cognitive_services.model_capacities
WHERE modelFormat = '{{ modelFormat }}'
AND modelName = '{{ modelName }}'
AND modelVersion = '{{ modelVersion }}'
AND subscriptionId = '{{ subscriptionId }}';
```