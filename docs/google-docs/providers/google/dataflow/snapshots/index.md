---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataflow.snapshots" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_jobs_snapshots_list" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> | Lists snapshots. |
| <CopyableCode code="projects_locations_snapshots_get" /> | `SELECT` | <CopyableCode code="location, projectId, snapshotId" /> | Gets information about a snapshot. |
| <CopyableCode code="projects_locations_snapshots_list" /> | `SELECT` | <CopyableCode code="location, projectId" /> | Lists snapshots. |
| <CopyableCode code="projects_snapshots_get" /> | `SELECT` | <CopyableCode code="projectId, snapshotId" /> | Gets information about a snapshot. |
| <CopyableCode code="projects_snapshots_list" /> | `SELECT` | <CopyableCode code="projectId" /> | Lists snapshots. |
| <CopyableCode code="projects_delete_snapshots" /> | `DELETE` | <CopyableCode code="projectId" /> | Deletes a snapshot. |
| <CopyableCode code="projects_locations_snapshots_delete" /> | `DELETE` | <CopyableCode code="location, projectId, snapshotId" /> | Deletes a snapshot. |
