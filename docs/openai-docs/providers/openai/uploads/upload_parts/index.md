---
title: upload_parts
hide_title: false
hide_table_of_contents: false
keywords:
  - upload_parts
  - uploads
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

Creates, updates, deletes, gets or lists a <code>upload_parts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>upload_parts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.uploads.upload_parts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_upload_part" /> | `INSERT` | <CopyableCode code="upload_id" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>upload_parts</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO openai.uploads.upload_parts (
upload_id
)
SELECT 
'{{ upload_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: upload_parts
  props:
    - name: upload_id
      value: string

```
</TabItem>
</Tabs>
