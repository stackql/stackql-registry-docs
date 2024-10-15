---
title: predictions_training_results
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions_training_results
  - customer_insights
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

Creates, updates, deletes, gets or lists a <code>predictions_training_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predictions_training_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.predictions_training_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="canonicalProfiles" /> | `array` | Canonical profiles. |
| <CopyableCode code="predictionDistribution" /> | `object` | The definition of the prediction distribution. |
| <CopyableCode code="primaryProfileInstanceCount" /> | `integer` | Instance count of the primary profile. |
| <CopyableCode code="scoreName" /> | `string` | Score name. |
| <CopyableCode code="tenantId" /> | `string` | The hub name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId" /> | Gets training results. |

## `SELECT` examples

Gets training results.


```sql
SELECT
canonicalProfiles,
predictionDistribution,
primaryProfileInstanceCount,
scoreName,
tenantId
FROM azure_extras.customer_insights.predictions_training_results
WHERE hubName = '{{ hubName }}'
AND predictionName = '{{ predictionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```