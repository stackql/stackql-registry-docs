---
title: completions
hide_title: false
hide_table_of_contents: false
keywords:
  - completions
  - completions
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

Creates, updates, deletes, gets or lists a <code>completions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>completions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.completions.completions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_completion" /> | `INSERT` | <CopyableCode code="data__model, data__prompt" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>completions</code> resource.

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
INSERT INTO openai.completions.completions (
data__model,
data__prompt,
data__best_of,
data__echo,
data__frequency_penalty,
data__logit_bias,
data__logprobs,
data__max_tokens,
data__n,
data__presence_penalty,
data__seed,
data__stop,
data__stream,
data__stream_options,
data__suffix,
data__temperature,
data__top_p,
data__user
)
SELECT 
'{{ model }}',
'{{ prompt }}',
'{{ best_of }}',
'{{ echo }}',
'{{ frequency_penalty }}',
'{{ logit_bias }}',
'{{ logprobs }}',
'{{ max_tokens }}',
'{{ n }}',
'{{ presence_penalty }}',
'{{ seed }}',
'{{ stop }}',
'{{ stream }}',
'{{ stream_options }}',
'{{ suffix }}',
'{{ temperature }}',
'{{ top_p }}',
'{{ user }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO openai.completions.completions (
data__model,
data__prompt
)
SELECT 
'{{ model }}',
'{{ prompt }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: completions
  props:
    - name: data__model
      value: string
    - name: data__prompt
      value: string
    - name: model
      value: string
    - name: prompt
      value: string
    - name: best_of
      value: integer
    - name: echo
      value: boolean
    - name: frequency_penalty
      value: number
    - name: logit_bias
      value: object
    - name: logprobs
      value: integer
    - name: max_tokens
      value: integer
    - name: 'n'
      value: integer
    - name: presence_penalty
      value: number
    - name: seed
      value: integer
    - name: stop
      value: string
    - name: stream
      value: boolean
    - name: stream_options
      props:
        - name: include_usage
          value: boolean
    - name: suffix
      value: string
    - name: temperature
      value: number
    - name: top_p
      value: number
    - name: user
      value: string

```
</TabItem>
</Tabs>
