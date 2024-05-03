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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the metrics, in the format "projects/&#123;project&#125;/keys/&#123;key&#125;/metrics". |
| <CopyableCode code="challengeMetrics" /> | `array` | Metrics will be continuous and in order by dates, and in the granularity of day. Only challenge-based keys (CHECKBOX, INVISIBLE), will have challenge-based data. |
| <CopyableCode code="scoreMetrics" /> | `array` | Metrics will be continuous and in order by dates, and in the granularity of day. All Key types should have score-based data. |
| <CopyableCode code="startTime" /> | `string` | Inclusive start time aligned to a day (UTC). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_metrics" /> | `SELECT` | <CopyableCode code="keysId, projectsId" /> |
