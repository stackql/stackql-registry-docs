---
title: work_items
hide_title: false
hide_table_of_contents: false
keywords:
  - work_items
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
<tr><td><b>Name</b></td><td><code>work_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.work_items" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_work_items_lease" /> | `EXEC` | <CopyableCode code="jobId, projectId" /> | Leases a dataflow WorkItem to run. |
| <CopyableCode code="projects_jobs_work_items_report_status" /> | `EXEC` | <CopyableCode code="jobId, projectId" /> | Reports the status of dataflow WorkItems leased by a worker. |
| <CopyableCode code="projects_locations_jobs_work_items_lease" /> | `EXEC` | <CopyableCode code="jobId, location, projectId" /> | Leases a dataflow WorkItem to run. |
| <CopyableCode code="projects_locations_jobs_work_items_report_status" /> | `EXEC` | <CopyableCode code="jobId, location, projectId" /> | Reports the status of dataflow WorkItems leased by a worker. |
