---
title: job_checkpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - job_checkpoints
  - fine_tuning
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

Creates, updates, deletes, gets or lists a <code>job_checkpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_checkpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.fine_tuning.job_checkpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The checkpoint identifier, which can be referenced in the API endpoints. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the checkpoint was created. |
| <CopyableCode code="fine_tuned_model_checkpoint" /> | `string` | The name of the fine-tuned checkpoint model that is created. |
| <CopyableCode code="fine_tuning_job_id" /> | `string` | The name of the fine-tuning job that this checkpoint was created from. |
| <CopyableCode code="metrics" /> | `object` | Metrics at the step number during the fine-tuning job. |
| <CopyableCode code="object" /> | `string` | The object type, which is always "fine_tuning.job.checkpoint". |
| <CopyableCode code="step_number" /> | `integer` | The step number that the checkpoint was created at. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_fine_tuning_job_checkpoints" /> | `SELECT` | <CopyableCode code="fine_tuning_job_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
created_at,
fine_tuned_model_checkpoint,
fine_tuning_job_id,
metrics,
object,
step_number
FROM openai.fine_tuning.job_checkpoints
WHERE fine_tuning_job_id = '{{ fine_tuning_job_id }}';
```