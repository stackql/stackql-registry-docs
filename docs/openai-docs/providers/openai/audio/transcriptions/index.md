---
title: transcriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - transcriptions
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

Creates, updates, deletes, gets or lists a <code>transcriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transcriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.audio.transcriptions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_transcription" /> | `INSERT` | <CopyableCode code="" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transcriptions</code> resource.

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
INSERT INTO openai.audio.transcriptions (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: transcriptions
  props: []

```
</TabItem>
</Tabs>
