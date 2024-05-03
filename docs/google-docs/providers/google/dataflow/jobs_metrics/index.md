---
title: jobs_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_metrics
  - dataflow
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
<tr><td><b>Name</b></td><td><code>jobs_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.jobs_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metricTime" /> | `string` | Timestamp as of which metric values are current. |
| <CopyableCode code="metrics" /> | `array` | All metrics for this job. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_jobs_get_metrics" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> |
| <CopyableCode code="projects_locations_jobs_get_metrics" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> |
