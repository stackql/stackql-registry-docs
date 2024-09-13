
---
title: slices
hide_title: false
hide_table_of_contents: false
keywords:
  - slices
  - aiplatform
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

Creates, updates, deletes or gets an <code>slice</code> resource or lists <code>slices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.slices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the ModelEvaluationSlice. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this ModelEvaluationSlice was created. |
| <CopyableCode code="metrics" /> | `any` | Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri |
| <CopyableCode code="metricsSchemaUri" /> | `string` | Output only. Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluationSlice. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). |
| <CopyableCode code="modelExplanation" /> | `object` | Aggregated explanation metrics for a Model over a set of instances. |
| <CopyableCode code="slice" /> | `object` | Definition of a slice. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="evaluationsId, locationsId, modelsId, projectsId, slicesId" /> | Gets a ModelEvaluationSlice. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="evaluationsId, locationsId, modelsId, projectsId" /> | Lists ModelEvaluationSlices in a ModelEvaluation. |
| <CopyableCode code="batch_import" /> | `EXEC` | <CopyableCode code="evaluationsId, locationsId, modelsId, projectsId, slicesId" /> | Imports a list of externally generated EvaluatedAnnotations. |

## `SELECT` examples

Lists ModelEvaluationSlices in a ModelEvaluation.

```sql
SELECT
name,
createTime,
metrics,
metricsSchemaUri,
modelExplanation,
slice
FROM google.aiplatform.slices
WHERE evaluationsId = '{{ evaluationsId }}'
AND locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}'; 
```
