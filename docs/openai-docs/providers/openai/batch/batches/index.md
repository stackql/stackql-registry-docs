---
title: batches
hide_title: false
hide_table_of_contents: false
keywords:
  - batches
  - batch
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>batches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.batch.batches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="cancelled_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch was cancelled. |
| <CopyableCode code="cancelling_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch started cancelling. |
| <CopyableCode code="completed_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch was completed. |
| <CopyableCode code="completion_window" /> | `string` | The time frame within which the batch should be processed. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch was created. |
| <CopyableCode code="endpoint" /> | `string` | The OpenAI API endpoint used by the batch. |
| <CopyableCode code="error_file_id" /> | `string` | The ID of the file containing the outputs of requests with errors. |
| <CopyableCode code="errors" /> | `object` |  |
| <CopyableCode code="expired_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch expired. |
| <CopyableCode code="expires_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch will expire. |
| <CopyableCode code="failed_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch failed. |
| <CopyableCode code="finalizing_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch started finalizing. |
| <CopyableCode code="in_progress_at" /> | `integer` | The Unix timestamp (in seconds) for when the batch started processing. |
| <CopyableCode code="input_file_id" /> | `string` | The ID of the input file for the batch. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `batch`. |
| <CopyableCode code="output_file_id" /> | `string` | The ID of the file containing the outputs of successfully executed requests. |
| <CopyableCode code="request_counts" /> | `object` | The request counts for different statuses within the batch. |
| <CopyableCode code="status" /> | `string` | The current status of the batch. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_batches" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="retrieve_batch" /> | `SELECT` | <CopyableCode code="batch_id" /> |  |
| <CopyableCode code="create_batch" /> | `INSERT` | <CopyableCode code="data__completion_window, data__endpoint, data__input_file_id" /> |  |
| <CopyableCode code="cancel_batch" /> | `EXEC` | <CopyableCode code="batch_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
cancelled_at,
cancelling_at,
completed_at,
completion_window,
created_at,
endpoint,
error_file_id,
errors,
expired_at,
expires_at,
failed_at,
finalizing_at,
in_progress_at,
input_file_id,
metadata,
object,
output_file_id,
request_counts,
status
FROM openai.batch.batches
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>batches</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO openai.batch.batches (
data__input_file_id,
data__endpoint,
data__completion_window,
data__metadata
)
SELECT 
'{{ input_file_id }}',
'{{ endpoint }}',
'{{ completion_window }}',
'{{ metadata }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO openai.batch.batches (
data__input_file_id,
data__endpoint,
data__completion_window
)
SELECT 
'{{ input_file_id }}',
'{{ endpoint }}',
'{{ completion_window }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: batches
  props:
    - name: data__completion_window
      value: string
    - name: data__endpoint
      value: string
    - name: data__input_file_id
      value: string
    - name: input_file_id
      value: string
    - name: endpoint
      value: string
    - name: completion_window
      value: string
    - name: metadata
      value: object

```
</TabItem>
</Tabs>
