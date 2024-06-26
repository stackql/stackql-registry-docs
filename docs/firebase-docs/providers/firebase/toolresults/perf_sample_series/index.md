---
title: perf_sample_series
hide_title: false
hide_table_of_contents: false
keywords:
  - perf_sample_series
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
<tr><td><b>Name</b></td><td><code>perf_sample_series</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.toolresults.perf_sample_series" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="basicPerfSampleSeries" /> | `object` | Encapsulates the metadata for basic sample series represented by a line chart |
| <CopyableCode code="executionId" /> | `string` | A tool results execution ID. @OutputOnly |
| <CopyableCode code="historyId" /> | `string` | A tool results history ID. @OutputOnly |
| <CopyableCode code="projectId" /> | `string` | The cloud project @OutputOnly |
| <CopyableCode code="sampleSeriesId" /> | `string` | A sample series id @OutputOnly |
| <CopyableCode code="stepId" /> | `string` | A tool results step ID. @OutputOnly |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_histories_executions_steps_perfSampleSeries_get" /> | `SELECT` | <CopyableCode code="executionId, historyId, projectId, sampleSeriesId, stepId" /> | Gets a PerfSampleSeries. May return any of the following error code(s): - NOT_FOUND - The specified PerfSampleSeries does not exist |
| <CopyableCode code="projects_histories_executions_steps_perfSampleSeries_list" /> | `SELECT` | <CopyableCode code="executionId, historyId, projectId, stepId" /> | Lists PerfSampleSeries for a given Step. The request provides an optional filter which specifies one or more PerfMetricsType to include in the result; if none returns all. The resulting PerfSampleSeries are sorted by ids. May return any of the following canonical error codes: - NOT_FOUND - The containing Step does not exist |
| <CopyableCode code="projects_histories_executions_steps_perfSampleSeries_create" /> | `INSERT` | <CopyableCode code="executionId, historyId, projectId, stepId" /> | Creates a PerfSampleSeries. May return any of the following error code(s): - ALREADY_EXISTS - PerfMetricSummary already exists for the given Step - NOT_FOUND - The containing Step does not exist |
