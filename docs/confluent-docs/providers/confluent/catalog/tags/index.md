---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - catalog
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.catalog.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attributes" /> | `object` | The tag attributes |
| <CopyableCode code="entityGuid" /> | `string` | The internal entity guid |
| <CopyableCode code="entityName" /> | `string` | The qualified name of the entity |
| <CopyableCode code="entityStatus" /> | `string` | The entity status |
| <CopyableCode code="entityType" /> | `string` | The entity type |
| <CopyableCode code="error" /> | `object` | Error message of this operation |
| <CopyableCode code="propagate" /> | `boolean` | Whether to propagate the tag |
| <CopyableCode code="removePropagationsOnEntityDelete" /> | `boolean` | Whether to remove propagations on entity delete |
| <CopyableCode code="typeName" /> | `string` | The tag name |
| <CopyableCode code="validityPeriods" /> | `array` | The validity periods |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_tags" /> | `SELECT` | <CopyableCode code="qualifiedName, typeName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets the list of tags for a given entity represented by a qualified name. |
| <CopyableCode code="create_tags" /> | `INSERT` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk API to create multiple tags. |
| <CopyableCode code="delete_tag" /> | `DELETE` | <CopyableCode code="qualifiedName, tagName, typeName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Delete a tag for an entity. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk API to update multiple tags. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets the list of tags for a given entity represented by a qualified name.


```sql
SELECT
attributes,
entityGuid,
entityName,
entityStatus,
entityType,
error,
propagate,
removePropagationsOnEntityDelete,
typeName,
validityPeriods
FROM confluent.catalog.tags
WHERE qualifiedName = '{{ qualifiedName }}'
AND typeName = '{{ typeName }}';
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
INSERT INTO confluent.catalog.tags (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: tags
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tags</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.catalog.tags
WHERE qualifiedName = '{{ qualifiedName }}'
AND tagName = '{{ tagName }}'
AND typeName = '{{ typeName }}';
```
