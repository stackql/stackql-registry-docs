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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feedback_messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.feedback_messages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the feedback message in a feedback thread. Format: 'project/&#123;project_id&#125;/datasets/&#123;dataset_id&#125;/annotatedDatasets/&#123;annotated_dataset_id&#125;/feedbackThreads/&#123;feedback_thread_id&#125;/feedbackMessage/&#123;feedback_message_id&#125;' |
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
| <CopyableCode code="_projects_datasets_annotated_datasets_feedback_threads_feedback_messages_list" /> | `EXEC` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | List FeedbackMessages with pagination. |
