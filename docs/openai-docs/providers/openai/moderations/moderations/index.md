---
title: moderations
hide_title: false
hide_table_of_contents: false
keywords:
  - moderations
  - moderations
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

Creates, updates, deletes, gets or lists a <code>moderations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>moderations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.moderations.moderations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_moderation" /> | `INSERT` | <CopyableCode code="data__input" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>moderations</code> resource.

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
INSERT INTO openai.moderations.moderations (
data__input,
data__model
)
SELECT 
'{{ input }}',
'{{ model }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO openai.moderations.moderations (
data__input
)
SELECT 
'{{ input }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: moderations
  props:
    - name: data__input
      value: string
    - name: input
      value: string
    - name: model
      value: string

```
</TabItem>
</Tabs>
