---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The tag name ID. |
| <CopyableCode code="count" /> | `object` | Tag count. |
| <CopyableCode code="tagName" /> | `string` | The tag name. |
| <CopyableCode code="values" /> | `array` | The list of tag values. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_at_scope" /> | `SELECT` | <CopyableCode code="scope" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId, tagName" /> | This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'. |
| <CopyableCode code="create_or_update_at_scope" /> | `INSERT` | <CopyableCode code="scope, data__properties" /> | This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId, tagName" /> | This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted. |
| <CopyableCode code="delete_at_scope" /> | `EXEC` | <CopyableCode code="scope" /> |  |
| <CopyableCode code="update_at_scope" /> | `EXEC` | <CopyableCode code="scope" /> | This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The 'replace' option replaces the entire set of existing tags with a new set. The 'merge' option allows adding tags with new names and updating the values of tags with existing names. The 'delete' option allows selectively deleting tags based on given names or name/value pairs. |

## `SELECT` examples




```sql
SELECT
id,
count,
tagName,
values
FROM azure.resources.tags
WHERE scope = '{{ scope }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags</code> resource.

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
INSERT INTO azure.resources.tags (
subscriptionId,
tagName
)
SELECT 
'{{ subscriptionId }}',
'{{ tagName }}'
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

Deletes the specified <code>tags</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resources.tags
WHERE subscriptionId = '{{ subscriptionId }}'
AND tagName = '{{ tagName }}';
```
