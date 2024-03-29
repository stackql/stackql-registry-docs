---
title: messages
hide_title: false
hide_table_of_contents: false
keywords:
  - messages
  - dataflow
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Deprecated. |
| `time` | `string` | The timestamp of the message. |
| `messageImportance` | `string` | Importance level of the message. |
| `messageText` | `string` | The text of the message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_jobs_messages_list` | `SELECT` | `jobId, projectId` |
| `projects_locations_jobs_messages_list` | `SELECT` | `jobId, location, projectId` |
| `_projects_jobs_messages_list` | `EXEC` | `jobId, projectId` |
| `_projects_locations_jobs_messages_list` | `EXEC` | `jobId, location, projectId` |
