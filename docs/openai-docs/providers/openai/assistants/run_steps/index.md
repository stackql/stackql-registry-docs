---
title: run_steps
hide_title: false
hide_table_of_contents: false
keywords:
  - run_steps
  - assistants
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

Creates, updates, deletes, gets or lists a <code>run_steps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>run_steps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.assistants.run_steps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the run step, which can be referenced in API endpoints. |
| <CopyableCode code="assistant_id" /> | `string` | The ID of the [assistant](/docs/api-reference/assistants) associated with the run step. |
| <CopyableCode code="cancelled_at" /> | `integer` | The Unix timestamp (in seconds) for when the run step was cancelled. |
| <CopyableCode code="completed_at" /> | `integer` | The Unix timestamp (in seconds) for when the run step completed. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the run step was created. |
| <CopyableCode code="expired_at" /> | `integer` | The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired. |
| <CopyableCode code="failed_at" /> | `integer` | The Unix timestamp (in seconds) for when the run step failed. |
| <CopyableCode code="last_error" /> | `object` | The last error associated with this run step. Will be `null` if there are no errors. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `thread.run.step`. |
| <CopyableCode code="run_id" /> | `string` | The ID of the [run](/docs/api-reference/runs) that this run step is a part of. |
| <CopyableCode code="status" /> | `string` | The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`. |
| <CopyableCode code="step_details" /> | `object` | The details of the run step. |
| <CopyableCode code="thread_id" /> | `string` | The ID of the [thread](/docs/api-reference/threads) that was run. |
| <CopyableCode code="type" /> | `string` | The type of run step, which can be either `message_creation` or `tool_calls`. |
| <CopyableCode code="usage" /> | `object` | Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_run_step" /> | `SELECT` | <CopyableCode code="run_id, step_id, thread_id" /> |  |
| <CopyableCode code="list_run_steps" /> | `SELECT` | <CopyableCode code="run_id, thread_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
assistant_id,
cancelled_at,
completed_at,
created_at,
expired_at,
failed_at,
last_error,
metadata,
object,
run_id,
status,
step_details,
thread_id,
type,
usage
FROM openai.assistants.run_steps
WHERE run_id = '{{ run_id }}'
AND thread_id = '{{ thread_id }}';
```