---
title: translations
hide_title: false
hide_table_of_contents: false
keywords:
  - translations
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

Creates, updates, deletes, gets or lists a <code>translations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>translations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.audio.translations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_translation" /> | `INSERT` | <CopyableCode code="" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>translations</code> resource.

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
INSERT INTO openai.audio.translations (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: translations
  props: []

```
</TabItem>
</Tabs>
