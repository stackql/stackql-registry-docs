---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - datalabeling
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

Creates, updates, deletes, gets or lists a <code>evaluations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.evaluations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of an evaluation. The name has the following format: "projects/{project_id}/datasets/{dataset_id}/evaluations/ {evaluation_id}' |
| <CopyableCode code="annotationType" /> | `string` | Output only. Type of task that the model version being evaluated performs, as defined in the evaluationJobConfig.inputConfig.annotationType field of the evaluation job that created this evaluation. |
| <CopyableCode code="config" /> | `object` | Configuration details used for calculating evaluation metrics and creating an Evaluation. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp for when this evaluation was created. |
| <CopyableCode code="evaluatedItemCount" /> | `string` | Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. |
| <CopyableCode code="evaluationJobRunTime" /> | `string` | Output only. Timestamp for when the evaluation job that created this evaluation ran. |
| <CopyableCode code="evaluationMetrics" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_evaluations_get" /> | `SELECT` | <CopyableCode code="datasetsId, evaluationsId, projectsId" /> | Gets an evaluation by resource name (to search, use projects.evaluations.search). |
| <CopyableCode code="projects_evaluations_search" /> | `EXEC` | <CopyableCode code="projectsId" /> | Searches evaluations within a project. |

## `SELECT` examples

Gets an evaluation by resource name (to search, use projects.evaluations.search).

```sql
SELECT
name,
annotationType,
config,
createTime,
evaluatedItemCount,
evaluationJobRunTime,
evaluationMetrics
FROM google.datalabeling.evaluations
WHERE datasetsId = '{{ datasetsId }}'
AND evaluationsId = '{{ evaluationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
