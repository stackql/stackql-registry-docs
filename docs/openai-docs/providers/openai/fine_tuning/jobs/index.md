---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_paginated_fine_tuning_jobs" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="retrieve_fine_tuning_job" /> | `SELECT` | <CopyableCode code="fine_tuning_job_id" /> |  |
| <CopyableCode code="create_fine_tuning_job" /> | `INSERT` | <CopyableCode code="data__model, data__training_file" /> |  |
| <CopyableCode code="cancel_fine_tuning_job" /> | `EXEC` | <CopyableCode code="fine_tuning_job_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
created_at,
error,
estimated_finish,
fine_tuned_model,
finished_at,
hyperparameters,
integrations,
model,
object,
organization_id,
result_files,
seed,
status,
trained_tokens,
training_file,
validation_file
FROM openai.fine_tuning.jobs
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO openai.fine_tuning.jobs (
data__model,
data__training_file,
data__hyperparameters,
data__suffix,
data__validation_file,
data__integrations,
data__seed
)
SELECT 
'{{ model }}',
'{{ training_file }}',
'{{ hyperparameters }}',
'{{ suffix }}',
'{{ validation_file }}',
'{{ integrations }}',
'{{ seed }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO openai.fine_tuning.jobs (
    data__model,
data__training_file
    )
    SELECT 
    '{{ model }}',
'{{ training_file }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: jobs
  props:
    - name: data__model
      value: string
    - name: data__training_file
      value: string
    - name: model
      value: string
    - name: training_file
      value: string
    - name: hyperparameters
      props:
        - name: batch_size
          value: string
        - name: learning_rate_multiplier
          value: string
        - name: n_epochs
          value: string
    - name: suffix
      value: string
    - name: validation_file
      value: string
    - name: integrations
      value: array
      props:
        - name: type
          value: string
        - name: wandb
          props:
            - name: project
              value: string
            - name: name
              value: string
            - name: entity
              value: string
            - name: tags
              value: array
    - name: seed
      value: integer

```
</TabItem>
</Tabs>
