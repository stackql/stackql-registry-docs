---
title: steps__perf_metrics_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - steps__perf_metrics_summary
  - toolresults
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>steps__perf_metrics_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.toolresults.steps__perf_metrics_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appStartTime" /> | `object` |  |
| <CopyableCode code="executionId" /> | `string` | A tool results execution ID. @OutputOnly |
| <CopyableCode code="graphicsStats" /> | `object` | Graphics statistics for the App. The information is collected from 'adb shell dumpsys graphicsstats'. For more info see: https://developer.android.com/training/testing/performance.html Statistics will only be present for API 23+. |
| <CopyableCode code="historyId" /> | `string` | A tool results history ID. @OutputOnly |
| <CopyableCode code="perfEnvironment" /> | `object` | Encapsulates performance environment info |
| <CopyableCode code="perfMetrics" /> | `array` | Set of resource collected |
| <CopyableCode code="projectId" /> | `string` | The cloud project @OutputOnly |
| <CopyableCode code="stepId" /> | `string` | A tool results step ID. @OutputOnly |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_histories_executions_steps_getPerfMetricsSummary" /> | `SELECT` | <CopyableCode code="executionId, historyId, projectId, stepId" /> |
