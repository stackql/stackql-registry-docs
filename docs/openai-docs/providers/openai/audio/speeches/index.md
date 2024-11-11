---
title: speeches
hide_title: false
hide_table_of_contents: false
keywords:
  - speeches
  - audio
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

Creates, updates, deletes, gets or lists a <code>speeches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>speeches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.audio.speeches" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_speech" /> | `INSERT` | <CopyableCode code="data__input, data__model, data__voice" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>speeches</code> resource.

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
INSERT INTO openai.audio.speeches (
data__model,
data__input,
data__voice,
data__response_format,
data__speed
)
SELECT 
'{{ model }}',
'{{ input }}',
'{{ voice }}',
'{{ response_format }}',
'{{ speed }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO openai.audio.speeches (
data__model,
data__input,
data__voice
)
SELECT 
'{{ model }}',
'{{ input }}',
'{{ voice }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: speeches
  props:
    - name: data__input
      value: string
    - name: data__model
      value: string
    - name: data__voice
      value: string
    - name: model
      value: string
    - name: input
      value: string
    - name: voice
      value: string
    - name: response_format
      value: string
    - name: speed
      value: number

```
</TabItem>
</Tabs>
