---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - datapipelines
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

Creates, updates, deletes or gets an <code>job</code> resource or lists <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datapipelines.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The internal ID for the job. |
| <CopyableCode code="name" /> | `string` | Required. The fully qualified resource name for the job. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time of job creation. |
| <CopyableCode code="dataflowJobDetails" /> | `object` | Pipeline job details specific to the Dataflow API. This is encapsulated here to allow for more executors to store their specific details separately. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time of job termination. This is absent if the job is still running. |
| <CopyableCode code="state" /> | `string` | The current state of the job. |
| <CopyableCode code="status" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, pipelinesId, projectsId" /> | Lists jobs for a given pipeline. Throws a "FORBIDDEN" error if the caller doesn't have permission to access it. |

## `SELECT` examples

Lists jobs for a given pipeline. Throws a "FORBIDDEN" error if the caller doesn't have permission to access it.

```sql
SELECT
id,
name,
createTime,
dataflowJobDetails,
endTime,
state,
status
FROM google.datapipelines.jobs
WHERE locationsId = '{{ locationsId }}'
AND pipelinesId = '{{ pipelinesId }}'
AND projectsId = '{{ projectsId }}'; 
```
