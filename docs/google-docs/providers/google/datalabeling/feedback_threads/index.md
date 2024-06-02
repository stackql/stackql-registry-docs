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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feedback_threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datalabeling.feedback_threads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the feedback thread. Format: 'project/&#123;project_id&#125;/datasets/&#123;dataset_id&#125;/annotatedDatasets/&#123;annotated_dataset_id&#125;/feedbackThreads/&#123;feedback_thread_id&#125;' |
| <CopyableCode code="feedbackThreadMetadata" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_get" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | Get a FeedbackThread object. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_list" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | List FeedbackThreads with pagination. |
| <CopyableCode code="projects_datasets_annotated_datasets_feedback_threads_delete" /> | `DELETE` | <CopyableCode code="annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId" /> | Delete a FeedbackThread. |
| <CopyableCode code="_projects_datasets_annotated_datasets_feedback_threads_list" /> | `EXEC` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | List FeedbackThreads with pagination. |
