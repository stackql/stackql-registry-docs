---
title: restore_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_plans
  - gkebackup
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
<tr><td><b>Name</b></td><td><code>restore_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkebackup.restore_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the RestorePlan resource. Format: `projects/*/locations/*/restorePlans/*`. |
| <CopyableCode code="description" /> | `string` | Optional. User specified descriptive string for this RestorePlan. |
| <CopyableCode code="backupPlan" /> | `string` | Required. Immutable. A reference to the BackupPlan from which Backups may be used as the source for Restores created via this RestorePlan. Format: `projects/*/locations/*/backupPlans/*`. |
| <CopyableCode code="cluster" /> | `string` | Required. Immutable. The target cluster into which Restores created via this RestorePlan will restore data. NOTE: the cluster's region must be the same as the RestorePlan. Valid formats: - `projects/*/locations/*/clusters/*` - `projects/*/zones/*/clusters/*` |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when this RestorePlan resource was created. |
| <CopyableCode code="etag" /> | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestorePlan`, and systems are expected to put that etag in the request to `UpdateRestorePlan` or `DeleteRestorePlan` to ensure that their change will be applied to the same version of the resource. |
| <CopyableCode code="labels" /> | `object` | Optional. A set of custom labels supplied by user. |
| <CopyableCode code="restoreConfig" /> | `object` | Configuration of a restore. |
| <CopyableCode code="state" /> | `string` | Output only. State of the RestorePlan. This State field reflects the various stages a RestorePlan can be in during the Create operation. |
| <CopyableCode code="stateReason" /> | `string` | Output only. Human-readable description of why RestorePlan is in the current `state` |
| <CopyableCode code="uid" /> | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when this RestorePlan resource was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, restorePlansId" /> | Retrieve the details of a single RestorePlan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists RestorePlans in a given location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new RestorePlan in a given location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, restorePlansId" /> | Deletes an existing RestorePlan. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, restorePlansId" /> | Update a RestorePlan. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists RestorePlans in a given location. |
