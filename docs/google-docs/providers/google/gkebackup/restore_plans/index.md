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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>restore_plans</code> resource.

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

## `SELECT` examples

Lists RestorePlans in a given location.

```sql
SELECT
name,
description,
backupPlan,
cluster,
createTime,
etag,
labels,
restoreConfig,
state,
stateReason,
uid,
updateTime
FROM google.gkebackup.restore_plans
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>restore_plans</code> resource.

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
INSERT INTO google.gkebackup.restore_plans (
locationsId,
projectsId,
description,
backupPlan,
cluster,
restoreConfig,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ backupPlan }}',
'{{ cluster }}',
'{{ restoreConfig }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: description
      value: string
    - name: backupPlan
      value: string
    - name: cluster
      value: string
    - name: restoreConfig
      value:
        - name: volumeDataRestorePolicy
          value: string
        - name: clusterResourceConflictPolicy
          value: string
        - name: namespacedResourceRestoreMode
          value: string
        - name: clusterResourceRestoreScope
          value:
            - name: selectedGroupKinds
              value:
                - - name: resourceGroup
                    value: string
                  - name: resourceKind
                    value: string
            - name: excludedGroupKinds
              value:
                - - name: resourceGroup
                    value: string
                  - name: resourceKind
                    value: string
            - name: allGroupKinds
              value: boolean
            - name: noGroupKinds
              value: boolean
        - name: allNamespaces
          value: boolean
        - name: selectedNamespaces
          value:
            - name: namespaces
              value:
                - string
        - name: selectedApplications
          value:
            - name: namespacedNames
              value:
                - - name: namespace
                    value: string
                  - name: name
                    value: string
        - name: noNamespaces
          value: boolean
        - name: substitutionRules
          value:
            - - name: targetNamespaces
                value:
                  - string
              - name: targetGroupKinds
                value:
                  - - name: resourceGroup
                      value: string
                    - name: resourceKind
                      value: string
              - name: targetJsonPath
                value: string
              - name: originalValuePattern
                value: string
              - name: newValue
                value: string
        - name: transformationRules
          value:
            - - name: fieldActions
                value:
                  - - name: op
                      value: string
                    - name: fromPath
                      value: string
                    - name: path
                      value: string
                    - name: value
                      value: string
              - name: resourceFilter
                value:
                  - name: namespaces
                    value:
                      - string
                  - name: groupKinds
                    value:
                      - - name: resourceGroup
                          value: string
                        - name: resourceKind
                          value: string
                  - name: jsonPath
                    value: string
              - name: description
                value: string
        - name: volumeDataRestorePolicyBindings
          value:
            - - name: policy
                value: string
              - name: volumeType
                value: string
        - name: restoreOrder
          value:
            - name: groupKindDependencies
              value:
                - - name: satisfying
                    value:
                      - name: resourceGroup
                        value: string
                      - name: resourceKind
                        value: string
    - name: labels
      value: object
    - name: etag
      value: string
    - name: state
      value: string
    - name: stateReason
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>restore_plans</code> resource.

```sql
/*+ update */
UPDATE google.gkebackup.restore_plans
SET 
description = '{{ description }}',
backupPlan = '{{ backupPlan }}',
cluster = '{{ cluster }}',
restoreConfig = '{{ restoreConfig }}',
labels = '{{ labels }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND restorePlansId = '{{ restorePlansId }}';
```

## `DELETE` example

Deletes the specified <code>restore_plans</code> resource.

```sql
/*+ delete */
DELETE FROM google.gkebackup.restore_plans
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND restorePlansId = '{{ restorePlansId }}';
```
