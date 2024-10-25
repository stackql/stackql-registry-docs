---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - fine_tuning
  - openai    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage OpenAI and ChatGPT resources using SQL.
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.fine_tuning.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The object identifier, which can be referenced in the API endpoints. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the fine-tuning job was created. |
| <CopyableCode code="error" /> | `object` | For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure. |
| <CopyableCode code="estimated_finish" /> | `integer` | The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running. |
| <CopyableCode code="fine_tuned_model" /> | `string` | The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running. |
| <CopyableCode code="finished_at" /> | `integer` | The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running. |
| <CopyableCode code="hyperparameters" /> | `object` | The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/fine-tuning) for more details. |
| <CopyableCode code="integrations" /> | `array` | A list of integrations to enable for this fine-tuning job. |
| <CopyableCode code="model" /> | `string` | The base model that is being fine-tuned. |
| <CopyableCode code="object" /> | `string` | The object type, which is always "fine_tuning.job". |
| <CopyableCode code="organization_id" /> | `string` | The organization that owns the fine-tuning job. |
| <CopyableCode code="result_files" /> | `array` | The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents). |
| <CopyableCode code="seed" /> | `integer` | The seed used for the fine-tuning job. |
| <CopyableCode code="status" /> | `string` | The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`. |
| <CopyableCode code="trained_tokens" /> | `integer` | The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running. |
| <CopyableCode code="training_file" /> | `string` | The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents). |
| <CopyableCode code="validation_file" /> | `string` | The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_paginated_fine_tuning_jobs" /> | `SELECT` |  |
| <CopyableCode code="retrieve_fine_tuning_job" /> | `SELECT` | <CopyableCode code="fine_tuning_job_id" /> |
| <CopyableCode code="create_fine_tuning_job" /> | `INSERT` | <CopyableCode code="data__model, data__training_file" /> |
| <CopyableCode code="cancel_fine_tuning_job" /> | `EXEC` | <CopyableCode code="fine_tuning_job_id" /> |
