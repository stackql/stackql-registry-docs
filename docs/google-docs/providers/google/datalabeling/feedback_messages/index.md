
---
title: feedback_messages
hide_title: false
hide_table_of_contents: false
keywords:
  - feedback_messages
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

Creates, updates, deletes or gets an <code>feedback_message</code> resource or lists <code>feedback_messages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feedback_messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.feedback_messages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the feedback message in a feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}' |
| <CopyableCode code="body" /> | `string` | String content of the feedback. Maximum of 10000 characters. |
| <CopyableCode code="createTime" /> | `string` | Create time. |
| <CopyableCode code="image" /> | `string` | The image storing this feedback if the feedback is an image representing operator's comments. |
| <CopyableCode code="operatorFeedbackMetadata" /> | `object` | Metadata describing the feedback from the operator. |
| <CopyableCode code="requesterFeedbackMetadata" /> | `object` | Metadata describing the feedback from the labeling task requester. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_feedback_messages_get" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackMessagesId, feedbackThreadsId, projectsId" /> | Get a FeedbackMessage object. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_feedback_messages_list" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | List FeedbackMessages with pagination. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_feedback_messages_create" /> | `INSERT` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | Create a FeedbackMessage object. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_feedback_messages_delete" /> | `DELETE` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackMessagesId, feedbackThreadsId, projectsId" /> | Delete a FeedbackMessage. |

## `SELECT` examples

List FeedbackMessages with pagination.

```sql
SELECT
name,
body,
createTime,
image,
operatorFeedbackMetadata,
requesterFeedbackMetadata
FROM google.datalabeling.feedback_messages
WHERE annotatedDatasetsId = '{{ annotatedDatasetsId }}'
AND datasetsId = '{{ datasetsId }}'
AND feedbackThreadsId = '{{ feedbackThreadsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>feedback_messages</code> resource.

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
INSERT INTO google.datalabeling.feedback_messages (
annotatedDatasetsId,
datasetsId,
feedbackThreadsId,
projectsId,
requesterFeedbackMetadata,
operatorFeedbackMetadata,
name,
body,
image,
createTime
)
SELECT 
'{{ annotatedDatasetsId }}',
'{{ datasetsId }}',
'{{ feedbackThreadsId }}',
'{{ projectsId }}',
'{{ requesterFeedbackMetadata }}',
'{{ operatorFeedbackMetadata }}',
'{{ name }}',
'{{ body }}',
'{{ image }}',
'{{ createTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: requesterFeedbackMetadata
        value: '{{ requesterFeedbackMetadata }}'
      - name: operatorFeedbackMetadata
        value: '{{ operatorFeedbackMetadata }}'
      - name: name
        value: '{{ name }}'
      - name: body
        value: '{{ body }}'
      - name: image
        value: '{{ image }}'
      - name: createTime
        value: '{{ createTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified feedback_message resource.

```sql
DELETE FROM google.datalabeling.feedback_messages
WHERE annotatedDatasetsId = '{{ annotatedDatasetsId }}'
AND datasetsId = '{{ datasetsId }}'
AND feedbackMessagesId = '{{ feedbackMessagesId }}'
AND feedbackThreadsId = '{{ feedbackThreadsId }}'
AND projectsId = '{{ projectsId }}';
```
