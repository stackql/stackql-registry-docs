---
title: tags_values
hide_title: false
hide_table_of_contents: false
keywords:
  - tags_values
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>tags_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.tags_values" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId, tagName, tagValue" /> | This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId, tagName, tagValue" /> | This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags_values</code> resource.

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
INSERT INTO azure.resources.tags_values (
subscriptionId,
tagName,
tagValue
)
SELECT 
'{{ subscriptionId }}',
'{{ tagName }}',
'{{ tagValue }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tags_values</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resources.tags_values
WHERE subscriptionId = '{{ subscriptionId }}'
AND tagName = '{{ tagName }}'
AND tagValue = '{{ tagValue }}';
```
