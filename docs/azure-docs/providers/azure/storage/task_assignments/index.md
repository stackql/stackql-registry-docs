---
title: task_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - task_assignments
  - storage
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

Creates, updates, deletes, gets or lists a <code>task_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.task_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_task_assignments', value: 'view', },
        { label: 'task_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_context" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="report" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageTaskAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="task_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the storage task assignment. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, storageTaskAssignmentName, subscriptionId" /> | Get the storage task assignment properties |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all the storage task assignments in an account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, storageTaskAssignmentName, subscriptionId, data__properties" /> | Asynchronously creates a new storage task assignment sub-resource with the specified parameters. If a storage task assignment is already created and a subsequent create request is issued with different properties, the storage task assignment properties will be updated. If a storage task assignment is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, storageTaskAssignmentName, subscriptionId" /> | Delete the storage task assignment sub-resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, storageTaskAssignmentName, subscriptionId" /> | Update storage task assignment properties |

## `SELECT` examples

List all the storage task assignments in an account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_task_assignments', value: 'view', },
        { label: 'task_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
accountName,
enabled,
execution_context,
provisioning_state,
report,
resourceGroupName,
run_status,
storageTaskAssignmentName,
subscriptionId,
task_id,
type
FROM azure.storage.vw_task_assignments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.storage.task_assignments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task_assignments</code> resource.

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
INSERT INTO azure.storage.task_assignments (
accountName,
resourceGroupName,
storageTaskAssignmentName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ storageTaskAssignmentName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: taskId
          value: string
        - name: enabled
          value: boolean
        - name: description
          value: string
        - name: executionContext
          value:
            - name: target
              value:
                - name: prefix
                  value:
                    - string
                - name: excludePrefix
                  value:
                    - string
            - name: trigger
              value:
                - name: type
                  value: string
                - name: parameters
                  value:
                    - name: startFrom
                      value: string
                    - name: interval
                      value: integer
                    - name: intervalUnit
                      value: string
                    - name: endBy
                      value: string
                    - name: startOn
                      value: string
        - name: report
          value:
            - name: prefix
              value: string
        - name: provisioningState
          value: string
        - name: runStatus
          value:
            - name: taskAssignmentId
              value: string
            - name: storageAccountId
              value: string
            - name: startTime
              value: string
            - name: finishTime
              value: string
            - name: objectsTargetedCount
              value: string
            - name: objectsOperatedOnCount
              value: string
            - name: objectFailedCount
              value: string
            - name: objectsSucceededCount
              value: string
            - name: runStatusError
              value: string
            - name: runStatusEnum
              value: string
            - name: summaryReportPath
              value: string
            - name: taskId
              value: string
            - name: taskVersion
              value: string
            - name: runResult
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>task_assignments</code> resource.

```sql
/*+ update */
UPDATE azure.storage.task_assignments
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskAssignmentName = '{{ storageTaskAssignmentName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>task_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.task_assignments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskAssignmentName = '{{ storageTaskAssignmentName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
