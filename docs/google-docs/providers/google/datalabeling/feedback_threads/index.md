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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feedback_threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.feedback_threads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}' |
| `feedbackThreadMetadata` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotatedDatasets_feedbackThreads_get` | `SELECT` | `annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId` | Get a FeedbackThread object. |
| `projects_datasets_annotatedDatasets_feedbackThreads_list` | `SELECT` | `annotatedDatasetsId, datasetsId, projectsId` | List FeedbackThreads with pagination. |
| `projects_datasets_annotatedDatasets_feedbackThreads_delete` | `DELETE` | `annotatedDatasetsId, datasetsId, feedbackThreadsId, projectsId` | Delete a FeedbackThread. |
