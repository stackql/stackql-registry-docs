---
title: processor_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - processor_versions
  - documentai
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

Creates, updates, deletes or gets an <code>processor_version</code> resource or lists <code>processor_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>processor_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.documentai.processor_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}` |
| <CopyableCode code="createTime" /> | `string` | The time the processor version was created. |
| <CopyableCode code="deprecationInfo" /> | `object` | Information about the upcoming deprecation of this processor version. |
| <CopyableCode code="displayName" /> | `string` | The display name of the processor version. |
| <CopyableCode code="documentSchema" /> | `object` | The schema defines the output of the processed document by a processor. |
| <CopyableCode code="genAiModelInfo" /> | `object` | Information about Generative AI model-based processor versions. |
| <CopyableCode code="googleManaged" /> | `boolean` | Output only. Denotes that this `ProcessorVersion` is managed by Google. |
| <CopyableCode code="kmsKeyName" /> | `string` | The KMS key name used for encryption. |
| <CopyableCode code="kmsKeyVersionName" /> | `string` | The KMS key version with which data is encrypted. |
| <CopyableCode code="latestEvaluation" /> | `object` | Gives a short summary of an evaluation, and links to the evaluation itself. |
| <CopyableCode code="modelType" /> | `string` | Output only. The model type of this processor version. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the processor version. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_processors_processor_versions_get" /> | `SELECT` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Gets a processor version detail. |
| <CopyableCode code="projects_locations_processors_processor_versions_list" /> | `SELECT` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Lists all versions of a processor. |
| <CopyableCode code="projects_locations_processors_processor_versions_delete" /> | `DELETE` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Deletes the processor version, all artifacts under the processor version will be deleted. |
| <CopyableCode code="projects_locations_processors_processor_versions_batch_process" /> | `EXEC` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| <CopyableCode code="projects_locations_processors_processor_versions_deploy" /> | `EXEC` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Deploys the processor version. |
| <CopyableCode code="projects_locations_processors_processor_versions_evaluate_processor_version" /> | `EXEC` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Evaluates a ProcessorVersion against annotated documents, producing an Evaluation. |
| <CopyableCode code="projects_locations_processors_processor_versions_process" /> | `EXEC` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Processes a single document. |
| <CopyableCode code="projects_locations_processors_processor_versions_train" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata. |
| <CopyableCode code="projects_locations_processors_processor_versions_undeploy" /> | `EXEC` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Undeploys the processor version. |

## `SELECT` examples

Lists all versions of a processor.

```sql
SELECT
name,
createTime,
deprecationInfo,
displayName,
documentSchema,
genAiModelInfo,
googleManaged,
kmsKeyName,
kmsKeyVersionName,
latestEvaluation,
modelType,
satisfiesPzi,
satisfiesPzs,
state
FROM google.documentai.processor_versions
WHERE locationsId = '{{ locationsId }}'
AND processorsId = '{{ processorsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified processor_version resource.

```sql
DELETE FROM google.documentai.processor_versions
WHERE locationsId = '{{ locationsId }}'
AND processorVersionsId = '{{ processorVersionsId }}'
AND processorsId = '{{ processorsId }}'
AND projectsId = '{{ projectsId }}';
```
