---
title: keys_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_metrics
  - recaptchaenterprise
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

Creates, updates, deletes, gets or lists a <code>keys_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The name of the metrics, in the format `projects/{project}/keys/{key}/metrics`. |
| <CopyableCode code="challengeMetrics" /> | `array` | Metrics are continuous and in order by dates, and in the granularity of day. Only challenge-based keys (CHECKBOX, INVISIBLE) have challenge-based data. |
| <CopyableCode code="scoreMetrics" /> | `array` | Metrics are continuous and in order by dates, and in the granularity of day. All Key types should have score-based data. |
| <CopyableCode code="startTime" /> | `string` | Inclusive start time aligned to a day (UTC). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_metrics" /> | `SELECT` | <CopyableCode code="keysId, projectsId" /> | Get some aggregated metrics for a Key. This data can be used to build dashboards. |

## `SELECT` examples

Get some aggregated metrics for a Key. This data can be used to build dashboards.

```sql
SELECT
name,
challengeMetrics,
scoreMetrics,
startTime
FROM google.recaptchaenterprise.keys_metrics
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}';
```
