---
title: business_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - business_metadata
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

Creates, updates, deletes, gets or lists a <code>business_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.catalog.business_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attributes" /> | `object` | The business metadata attributes |
| <CopyableCode code="entityName" /> | `string` | The qualified name of the entity |
| <CopyableCode code="entityType" /> | `string` | The entity type |
| <CopyableCode code="error" /> | `object` | Error message of this operation |
| <CopyableCode code="typeName" /> | `string` | The business metadata name |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_business_metadata" /> | `SELECT` | <CopyableCode code="qualifiedName, typeName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets the list of business metadata for a given entity represented by a qualified name. |
| <CopyableCode code="create_business_metadata" /> | `INSERT` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk API to create multiple business metadata. |
| <CopyableCode code="delete_business_metadata" /> | `DELETE` | <CopyableCode code="bmName, qualifiedName, typeName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Delete a business metadata on an entity. |
| <CopyableCode code="update_business_metadata" /> | `EXEC` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk API to update multiple business metadata. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets the list of business metadata for a given entity represented by a qualified name.


```sql
SELECT
attributes,
entityName,
entityType,
error,
typeName
FROM confluent.catalog.business_metadata
WHERE qualifiedName = '{{ qualifiedName }}'
AND typeName = '{{ typeName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>business_metadata</code> resource.

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
INSERT INTO confluent.catalog.business_metadata (

)
SELECT 

;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: business_metadata
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>business_metadata</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.catalog.business_metadata
WHERE bmName = '{{ bmName }}'
AND qualifiedName = '{{ qualifiedName }}'
AND typeName = '{{ typeName }}';
```
