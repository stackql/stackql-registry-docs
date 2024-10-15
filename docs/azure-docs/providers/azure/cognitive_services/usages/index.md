---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="currentValue" /> | `number` | Current value for this metric. |
| <CopyableCode code="limit" /> | `number` | Maximum value for this metric. |
| <CopyableCode code="nextResetTime" /> | `string` | Next reset time for current quota. |
| <CopyableCode code="quotaPeriod" /> | `string` | The quota period used to summarize the usage values. |
| <CopyableCode code="status" /> | `string` | Cognitive Services account quota usage status. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get usages for the requested subscription |

## `SELECT` examples

Get usages for the requested subscription


```sql
SELECT
name,
currentValue,
limit,
nextResetTime,
quotaPeriod,
status,
unit
FROM azure.cognitive_services.usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```