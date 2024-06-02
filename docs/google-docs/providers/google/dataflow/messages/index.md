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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataflow.messages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Deprecated. |
| <CopyableCode code="messageImportance" /> | `string` | Importance level of the message. |
| <CopyableCode code="messageText" /> | `string` | The text of the message. |
| <CopyableCode code="time" /> | `string` | The timestamp of the message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_jobs_messages_list" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> |
| <CopyableCode code="projects_locations_jobs_messages_list" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> |
| <CopyableCode code="_projects_jobs_messages_list" /> | `EXEC` | <CopyableCode code="jobId, projectId" /> |
| <CopyableCode code="_projects_locations_jobs_messages_list" /> | `EXEC` | <CopyableCode code="jobId, location, projectId" /> |
