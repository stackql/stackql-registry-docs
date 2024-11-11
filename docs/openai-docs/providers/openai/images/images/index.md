---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - images
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

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.images.images" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_image" /> | `INSERT` | <CopyableCode code="data__prompt" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>images</code> resource.

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
INSERT INTO openai.images.images (
data__prompt,
data__model,
data__n,
data__quality,
data__response_format,
data__size,
data__style,
data__user
)
SELECT 
'{{ prompt }}',
'{{ model }}',
'{{ n }}',
'{{ quality }}',
'{{ response_format }}',
'{{ size }}',
'{{ style }}',
'{{ user }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO openai.images.images (
    data__prompt
    )
    SELECT 
    '{{ prompt }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: images
  props:
    - name: data__prompt
      value: string
    - name: prompt
      value: string
    - name: model
      value: string
    - name: 'n'
      value: integer
    - name: quality
      value: string
    - name: response_format
      value: string
    - name: size
      value: string
    - name: style
      value: string
    - name: user
      value: string

```
</TabItem>
</Tabs>
