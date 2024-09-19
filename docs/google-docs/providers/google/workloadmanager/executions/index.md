---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
  - workloadmanager
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

Creates, updates, deletes, gets or lists a <code>executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workloadmanager.executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of execution resource. The format is projects/{project}/locations/{location}/evaluations/{evaluation}/executions/{execution} |
| <CopyableCode code="endTime" /> | `string` | Output only. [Output only] End time stamp |
| <CopyableCode code="evaluationId" /> | `string` | Output only. [Output only] Evaluation ID |
| <CopyableCode code="externalDataSources" /> | `array` | Optional. External data sources |
| <CopyableCode code="inventoryTime" /> | `string` | Output only. [Output only] Inventory time stamp |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="runType" /> | `string` | type represent whether the execution executed directly by user or scheduled according evaluation.schedule field. |
| <CopyableCode code="startTime" /> | `string` | Output only. [Output only] Start time stamp |
| <CopyableCode code="state" /> | `string` | Output only. [Output only] State |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="evaluationsId, executionsId, locationsId, projectsId" /> | Gets details of a single Execution. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="evaluationsId, locationsId, projectsId" /> | Lists Executions in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="evaluationsId, executionsId, locationsId, projectsId" /> | Deletes a single Execution. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="evaluationsId, locationsId, projectsId" /> | Creates a new Execution in a given project and location. |

## `SELECT` examples

Lists Executions in a given project and location.

```sql
SELECT
name,
endTime,
evaluationId,
externalDataSources,
inventoryTime,
labels,
runType,
startTime,
state
FROM google.workloadmanager.executions
WHERE evaluationsId = '{{ evaluationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>executions</code> resource.

```sql
/*+ delete */
DELETE FROM google.workloadmanager.executions
WHERE evaluationsId = '{{ evaluationsId }}'
AND executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
