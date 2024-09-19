---
title: annotated_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - annotated_datasets
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

Creates, updates, deletes, gets or lists a <code>annotated_datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotated_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.annotated_datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. AnnotatedDataset resource name in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id} |
| <CopyableCode code="description" /> | `string` | Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters. |
| <CopyableCode code="annotationSource" /> | `string` | Output only. Source of the annotation. |
| <CopyableCode code="annotationType" /> | `string` | Output only. Type of the annotation. It is specified when starting labeling task. |
| <CopyableCode code="blockingResources" /> | `array` | Output only. The names of any related resources that are blocking changes to the annotated dataset. |
| <CopyableCode code="completedExampleCount" /> | `string` | Output only. Number of examples that have annotation in the annotated dataset. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the AnnotatedDataset was created. |
| <CopyableCode code="displayName" /> | `string` | Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters. |
| <CopyableCode code="exampleCount" /> | `string` | Output only. Number of examples in the annotated dataset. |
| <CopyableCode code="labelStats" /> | `object` | Statistics about annotation specs. |
| <CopyableCode code="metadata" /> | `object` | Metadata on AnnotatedDataset. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_annotated_datasets_get" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | Gets an annotated dataset by resource name. |
| <CopyableCode code="projects_datasets_annotated_datasets_list" /> | `SELECT` | <CopyableCode code="datasetsId, projectsId" /> | Lists annotated datasets for a dataset. Pagination is supported. |
| <CopyableCode code="projects_datasets_annotated_datasets_delete" /> | `DELETE` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | Deletes an annotated dataset by resource name. |

## `SELECT` examples

Lists annotated datasets for a dataset. Pagination is supported.

```sql
SELECT
name,
description,
annotationSource,
annotationType,
blockingResources,
completedExampleCount,
createTime,
displayName,
exampleCount,
labelStats,
metadata
FROM google.datalabeling.annotated_datasets
WHERE datasetsId = '{{ datasetsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>annotated_datasets</code> resource.

```sql
/*+ delete */
DELETE FROM google.datalabeling.annotated_datasets
WHERE annotatedDatasetsId = '{{ annotatedDatasetsId }}'
AND datasetsId = '{{ datasetsId }}'
AND projectsId = '{{ projectsId }}';
```
