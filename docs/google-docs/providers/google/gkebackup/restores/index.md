
---
title: restores
hide_title: false
hide_table_of_contents: false
keywords:
  - restores
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>restore</code> resource or lists <code>restores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkebackup.restores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the Restore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*` |
| <CopyableCode code="description" /> | `string` | User specified descriptive string for this Restore. |
| <CopyableCode code="backup" /> | `string` | Required. Immutable. A reference to the Backup used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's backup_plan. Format: `projects/*/locations/*/backupPlans/*/backups/*`. |
| <CopyableCode code="cluster" /> | `string` | Output only. The target cluster into which this Restore will restore data. Valid formats: - `projects/*/locations/*/clusters/*` - `projects/*/zones/*/clusters/*` Inherited from parent RestorePlan's cluster value. |
| <CopyableCode code="completeTime" /> | `string` | Output only. Timestamp of when the restore operation completed. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when this Restore resource was created. |
| <CopyableCode code="etag" /> | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestore`, and systems are expected to put that etag in the request to `UpdateRestore` or `DeleteRestore` to ensure that their change will be applied to the same version of the resource. |
| <CopyableCode code="filter" /> | `object` | Defines the filter for `Restore`. This filter can be used to further refine the resource selection of the `Restore` beyond the coarse-grained scope defined in the `RestorePlan`. `exclusion_filters` take precedence over `inclusion_filters`. If a resource matches both `inclusion_filters` and `exclusion_filters`, it will not be restored. |
| <CopyableCode code="labels" /> | `object` | A set of custom labels supplied by user. |
| <CopyableCode code="resourcesExcludedCount" /> | `integer` | Output only. Number of resources excluded during the restore execution. |
| <CopyableCode code="resourcesFailedCount" /> | `integer` | Output only. Number of resources that failed to be restored during the restore execution. |
| <CopyableCode code="resourcesRestoredCount" /> | `integer` | Output only. Number of resources restored during the restore execution. |
| <CopyableCode code="restoreConfig" /> | `object` | Configuration of a restore. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the Restore. |
| <CopyableCode code="stateReason" /> | `string` | Output only. Human-readable description of why the Restore is in its current state. |
| <CopyableCode code="uid" /> | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when this Restore resource was last updated. |
| <CopyableCode code="volumeDataRestorePolicyOverrides" /> | `array` | Optional. Immutable. Overrides the volume data restore policies selected in the Restore Config for override-scoped resources. |
| <CopyableCode code="volumesRestoredCount" /> | `integer` | Output only. Number of volumes restored during the restore execution. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, restorePlansId, restoresId" /> | Retrieves the details of a single Restore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, restorePlansId" /> | Lists the Restores for a given RestorePlan. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, restorePlansId" /> | Creates a new Restore for the given RestorePlan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, restorePlansId, restoresId" /> | Deletes an existing Restore. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, restorePlansId, restoresId" /> | Update a Restore. |

## `SELECT` examples

Lists the Restores for a given RestorePlan.

```sql
SELECT
name,
description,
backup,
cluster,
completeTime,
createTime,
etag,
filter,
labels,
resourcesExcludedCount,
resourcesFailedCount,
resourcesRestoredCount,
restoreConfig,
state,
stateReason,
uid,
updateTime,
volumeDataRestorePolicyOverrides,
volumesRestoredCount
FROM google.gkebackup.restores
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND restorePlansId = '{{ restorePlansId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>restores</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.gkebackup.restores (
locationsId,
projectsId,
restorePlansId,
name,
uid,
createTime,
updateTime,
description,
backup,
cluster,
restoreConfig,
labels,
state,
stateReason,
completeTime,
resourcesRestoredCount,
resourcesExcludedCount,
resourcesFailedCount,
volumesRestoredCount,
etag,
filter,
volumeDataRestorePolicyOverrides
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ restorePlansId }}',
'{{ name }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ backup }}',
'{{ cluster }}',
'{{ restoreConfig }}',
'{{ labels }}',
'{{ state }}',
'{{ stateReason }}',
'{{ completeTime }}',
'{{ resourcesRestoredCount }}',
'{{ resourcesExcludedCount }}',
'{{ resourcesFailedCount }}',
'{{ volumesRestoredCount }}',
'{{ etag }}',
'{{ filter }}',
'{{ volumeDataRestorePolicyOverrides }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: backup
        value: '{{ backup }}'
      - name: cluster
        value: '{{ cluster }}'
      - name: restoreConfig
        value: '{{ restoreConfig }}'
      - name: labels
        value: '{{ labels }}'
      - name: state
        value: '{{ state }}'
      - name: stateReason
        value: '{{ stateReason }}'
      - name: completeTime
        value: '{{ completeTime }}'
      - name: resourcesRestoredCount
        value: '{{ resourcesRestoredCount }}'
      - name: resourcesExcludedCount
        value: '{{ resourcesExcludedCount }}'
      - name: resourcesFailedCount
        value: '{{ resourcesFailedCount }}'
      - name: volumesRestoredCount
        value: '{{ volumesRestoredCount }}'
      - name: etag
        value: '{{ etag }}'
      - name: filter
        value: '{{ filter }}'
      - name: volumeDataRestorePolicyOverrides
        value: '{{ volumeDataRestorePolicyOverrides }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a restore only if the necessary resources are available.

```sql
UPDATE google.gkebackup.restores
SET 
name = '{{ name }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
backup = '{{ backup }}',
cluster = '{{ cluster }}',
restoreConfig = '{{ restoreConfig }}',
labels = '{{ labels }}',
state = '{{ state }}',
stateReason = '{{ stateReason }}',
completeTime = '{{ completeTime }}',
resourcesRestoredCount = '{{ resourcesRestoredCount }}',
resourcesExcludedCount = '{{ resourcesExcludedCount }}',
resourcesFailedCount = '{{ resourcesFailedCount }}',
volumesRestoredCount = '{{ volumesRestoredCount }}',
etag = '{{ etag }}',
filter = '{{ filter }}',
volumeDataRestorePolicyOverrides = '{{ volumeDataRestorePolicyOverrides }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND restorePlansId = '{{ restorePlansId }}'
AND restoresId = '{{ restoresId }}';
```

## `DELETE` example

Deletes the specified restore resource.

```sql
DELETE FROM google.gkebackup.restores
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND restorePlansId = '{{ restorePlansId }}'
AND restoresId = '{{ restoresId }}';
```
