---
title: step_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - step_entries
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

Creates, updates, deletes, gets or lists a <code>step_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>step_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workflowexecutions.step_entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full resource name of the step entry. Each step entry has a unique entry ID, which is a monotonically increasing counter. Step entry names have the format: `projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}/stepEntries/{step_entry}`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the step entry. |
| <CopyableCode code="entryId" /> | `string` | Output only. The numeric ID of this step entry, used for navigation. |
| <CopyableCode code="exception" /> | `object` | Exception describes why the step entry failed. |
| <CopyableCode code="navigationInfo" /> | `object` | NavigationInfo describes what steps if any come before or after this step, or what steps are parents or children of this step. |
| <CopyableCode code="routine" /> | `string` | Output only. The name of the routine this step entry belongs to. A routine name is the subworkflow name defined in the YAML source code. The top level routine name is `main`. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the step entry. |
| <CopyableCode code="step" /> | `string` | Output only. The name of the step this step entry belongs to. |
| <CopyableCode code="stepEntryMetadata" /> | `object` | StepEntryMetadata contains metadata information about this step. |
| <CopyableCode code="stepType" /> | `string` | Output only. The type of the step this step entry belongs to. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recently updated time of the step entry. |
| <CopyableCode code="variableData" /> | `object` | VariableData contains the variable data for this step. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="executionsId, locationsId, projectsId, stepEntriesId, workflowsId" /> | Gets a step entry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> | Lists step entries for the corresponding workflow execution. Returned entries are ordered by their create_time. |

## `SELECT` examples

Lists step entries for the corresponding workflow execution. Returned entries are ordered by their create_time.

```sql
SELECT
name,
createTime,
entryId,
exception,
navigationInfo,
routine,
state,
step,
stepEntryMetadata,
stepType,
updateTime,
variableData
FROM google.workflowexecutions.step_entries
WHERE executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workflowsId = '{{ workflowsId }}';
```
