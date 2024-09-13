---
title: feedback_threads
hide_title: false
hide_table_of_contents: false
keywords:
  - feedback_threads
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

Creates, updates, deletes or gets an <code>feedback_thread</code> resource or lists <code>feedback_threads</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feedback_threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.feedback_threads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}' |
| <CopyableCode code="feedbackThreadMetadata" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_get" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | Get a FeedbackThread object. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_list" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | List FeedbackThreads with pagination. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_delete" /> | `DELETE` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | Delete a FeedbackThread. |

## `SELECT` examples

List FeedbackThreads with pagination.

```sql
SELECT
name,
feedbackThreadMetadata
FROM google.datalabeling.feedback_threads
WHERE annotatedDatasetsId = '{{ annotatedDatasetsId }}'
AND datasetsId = '{{ datasetsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified feedback_thread resource.

```sql
DELETE FROM google.datalabeling.feedback_threads
WHERE annotatedDatasetsId = '{{ annotatedDatasetsId }}'
AND datasetsId = '{{ datasetsId }}'
AND feedbackThreadsId = '{{ feedbackThreadsId }}'
AND projectsId = '{{ projectsId }}';
```
