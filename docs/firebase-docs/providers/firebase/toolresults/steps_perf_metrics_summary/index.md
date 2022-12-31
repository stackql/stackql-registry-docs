---
title: steps_perf_metrics_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - steps_perf_metrics_summary
  - toolresults
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>steps_perf_metrics_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.toolresults.steps_perf_metrics_summary</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `graphicsStats` | `object` | Graphics statistics for the App. The information is collected from 'adb shell dumpsys graphicsstats'. For more info see: https://developer.android.com/training/testing/performance.html Statistics will only be present for API 23+. |
| `historyId` | `string` | A tool results history ID. @OutputOnly |
| `perfEnvironment` | `object` | Encapsulates performance environment info |
| `perfMetrics` | `array` | Set of resource collected |
| `projectId` | `string` | The cloud project @OutputOnly |
| `stepId` | `string` | A tool results step ID. @OutputOnly |
| `appStartTime` | `object` |  |
| `executionId` | `string` | A tool results execution ID. @OutputOnly |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_histories_executions_steps_getPerfMetricsSummary` | `SELECT` | `executionId, historyId, projectId, stepId` |
