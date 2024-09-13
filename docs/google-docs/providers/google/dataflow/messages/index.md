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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>message</code> resource or lists <code>messages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.messages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Deprecated. |
| <CopyableCode code="messageImportance" /> | `string` | Importance level of the message. |
| <CopyableCode code="messageText" /> | `string` | The text of the message. |
| <CopyableCode code="time" /> | `string` | The timestamp of the message. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_messages_list" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> | Request the job status. To request the status of a job, we recommend using `projects.locations.jobs.messages.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.messages.list` is not recommended, as you can only request the status of jobs that are running in `us-central1`. |
| <CopyableCode code="projects_locations_jobs_messages_list" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> | Request the job status. To request the status of a job, we recommend using `projects.locations.jobs.messages.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.messages.list` is not recommended, as you can only request the status of jobs that are running in `us-central1`. |

## `SELECT` examples

Request the job status. To request the status of a job, we recommend using `projects.locations.jobs.messages.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.messages.list` is not recommended, as you can only request the status of jobs that are running in `us-central1`.

```sql
SELECT
id,
messageImportance,
messageText,
time
FROM google.dataflow.messages
WHERE jobId = '{{ jobId }}'
AND projectId = '{{ projectId }}'; 
```
