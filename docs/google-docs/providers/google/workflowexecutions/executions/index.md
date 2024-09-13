---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
  - workflowexecutions
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

Creates, updates, deletes or gets an <code>execution</code> resource or lists <code>executions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workflowexecutions.executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} |
| <CopyableCode code="argument" /> | `string` | Input parameters of the execution represented as a JSON string. The size limit is 32KB. *Note*: If you are using the REST API directly to run your workflow, you must escape any JSON string value of `argument`. Example: `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'` |
| <CopyableCode code="callLogLevel" /> | `string` | The call logging level associated to this execution. |
| <CopyableCode code="createTime" /> | `string` | Output only. Marks the creation of the execution. |
| <CopyableCode code="disableConcurrencyQuotaOverflowBuffering" /> | `boolean` | Optional. If set to true, the execution will not be backlogged when the concurrency quota is exhausted. The backlog execution starts when the concurrency quota becomes available. |
| <CopyableCode code="duration" /> | `string` | Output only. Measures the duration of the execution. |
| <CopyableCode code="endTime" /> | `string` | Output only. Marks the end of execution, successful or not. |
| <CopyableCode code="error" /> | `object` | Error describes why the execution was abnormally terminated. |
| <CopyableCode code="executionHistoryLevel" /> | `string` | Optional. Describes the level of the execution history feature to apply to this execution. If not specified, the level of the execution history feature will be determined by its workflow's execution history level. If the value is different from its workflow's value, it will override the workflow's execution history level for this exeuction. |
| <CopyableCode code="labels" /> | `object` | Labels associated with this execution. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution. |
| <CopyableCode code="result" /> | `string` | Output only. Output of the execution represented as a JSON string. The value can only be present if the execution's state is `SUCCEEDED`. |
| <CopyableCode code="startTime" /> | `string` | Output only. Marks the beginning of execution. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the execution. |
| <CopyableCode code="stateError" /> | `object` | Describes an error related to the current state of the Execution resource. |
| <CopyableCode code="status" /> | `object` | Represents the current status of this execution. |
| <CopyableCode code="workflowRevisionId" /> | `string` | Output only. Revision of the workflow this execution is using. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> | Returns an execution of the given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workflowsId" /> | Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first). |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, workflowsId" /> | Creates a new execution using the latest revision of the given workflow. For more information, see Execute a workflow. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> | Cancels an execution of the given name. |
| <CopyableCode code="export_data" /> | `EXEC` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> | Returns all metadata stored about an execution, excluding most data that is already accessible using other API methods. |

## `SELECT` examples

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

```sql
SELECT
name,
argument,
callLogLevel,
createTime,
disableConcurrencyQuotaOverflowBuffering,
duration,
endTime,
error,
executionHistoryLevel,
labels,
result,
startTime,
state,
stateError,
status,
workflowRevisionId
FROM google.workflowexecutions.executions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workflowsId = '{{ workflowsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>executions</code> resource.

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
INSERT INTO google.workflowexecutions.executions (
locationsId,
projectsId,
workflowsId,
name,
createTime,
startTime,
endTime,
duration,
state,
argument,
result,
error,
workflowRevisionId,
callLogLevel,
status,
labels,
stateError,
disableConcurrencyQuotaOverflowBuffering,
executionHistoryLevel
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ workflowsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ startTime }}',
'{{ endTime }}',
'{{ duration }}',
'{{ state }}',
'{{ argument }}',
'{{ result }}',
'{{ error }}',
'{{ workflowRevisionId }}',
'{{ callLogLevel }}',
'{{ status }}',
'{{ labels }}',
'{{ stateError }}',
true|false,
'{{ executionHistoryLevel }}'
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
      - name: createTime
        value: '{{ createTime }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: duration
        value: '{{ duration }}'
      - name: state
        value: '{{ state }}'
      - name: argument
        value: '{{ argument }}'
      - name: result
        value: '{{ result }}'
      - name: error
        value: '{{ error }}'
      - name: workflowRevisionId
        value: '{{ workflowRevisionId }}'
      - name: callLogLevel
        value: '{{ callLogLevel }}'
      - name: status
        value: '{{ status }}'
      - name: labels
        value: '{{ labels }}'
      - name: stateError
        value: '{{ stateError }}'
      - name: disableConcurrencyQuotaOverflowBuffering
        value: '{{ disableConcurrencyQuotaOverflowBuffering }}'
      - name: executionHistoryLevel
        value: '{{ executionHistoryLevel }}'

```
</TabItem>
</Tabs>
