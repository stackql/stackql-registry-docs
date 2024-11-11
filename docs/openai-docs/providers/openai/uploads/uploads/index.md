---
title: uploads
hide_title: false
hide_table_of_contents: false
keywords:
  - uploads
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

Creates, updates, deletes, gets or lists a <code>uploads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.uploads.uploads" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_upload" /> | `INSERT` | <CopyableCode code="data__bytes, data__filename, data__mime_type, data__purpose" /> |  |
| <CopyableCode code="cancel_upload" /> | `EXEC` | <CopyableCode code="upload_id" /> |  |
| <CopyableCode code="complete_upload" /> | `EXEC` | <CopyableCode code="upload_id, data__part_ids" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>uploads</code> resource.

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
INSERT INTO openai.uploads.uploads (
data__filename,
data__purpose,
data__bytes,
data__mime_type
)
SELECT 
'{{ filename }}',
'{{ purpose }}',
'{{ bytes }}',
'{{ mime_type }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: uploads
  props:
    - name: data__bytes
      value: string
    - name: data__filename
      value: string
    - name: data__mime_type
      value: string
    - name: data__purpose
      value: string
    - name: filename
      value: string
    - name: purpose
      value: string
    - name: bytes
      value: integer
    - name: mime_type
      value: string

```
</TabItem>
</Tabs>
