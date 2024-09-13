
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>snapshot</code> resource or lists <code>snapshots</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of this snapshot. |
| <CopyableCode code="description" /> | `string` | User specified description of the snapshot. Maybe empty. |
| <CopyableCode code="creationTime" /> | `string` | The time this snapshot was created. |
| <CopyableCode code="diskSizeBytes" /> | `string` | The disk byte size of the snapshot. Only available for snapshots in READY state. |
| <CopyableCode code="projectId" /> | `string` | The project this snapshot belongs to. |
| <CopyableCode code="pubsubMetadata" /> | `array` | Pub/Sub snapshot metadata. |
| <CopyableCode code="region" /> | `string` | Cloud region where this snapshot lives in, e.g., "us-central1". |
| <CopyableCode code="sourceJobId" /> | `string` | The job this snapshot was created from. |
| <CopyableCode code="state" /> | `string` | State of the snapshot. |
| <CopyableCode code="ttl" /> | `string` | The time after which this snapshot will be automatically deleted. |

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

## `SELECT` examples

Lists snapshots.

```sql
SELECT
id,
description,
creationTime,
diskSizeBytes,
projectId,
pubsubMetadata,
region,
sourceJobId,
state,
ttl
FROM google.dataflow.snapshots
WHERE projectId = '{{ projectId }}'; 
```

## `DELETE` example

Deletes the specified snapshot resource.

```sql
DELETE FROM google.dataflow.snapshots
WHERE projectId = '{{ projectId }}';
```
