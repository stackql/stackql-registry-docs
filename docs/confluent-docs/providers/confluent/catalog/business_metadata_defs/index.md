---
title: business_metadata_defs
hide_title: false
hide_table_of_contents: false
keywords:
  - business_metadata_defs
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

Creates, updates, deletes, gets or lists a <code>business_metadata_defs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_metadata_defs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.catalog.business_metadata_defs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name |
| <CopyableCode code="description" /> | `string` | The description |
| <CopyableCode code="attributeDefs" /> | `array` | The attribute definitions |
| <CopyableCode code="category" /> | `string` | The category |
| <CopyableCode code="createTime" /> | `integer` | The create time |
| <CopyableCode code="createdBy" /> | `string` | The creator |
| <CopyableCode code="guid" /> | `string` | The internal guid |
| <CopyableCode code="options" /> | `object` | The options |
| <CopyableCode code="serviceType" /> | `string` | The service type |
| <CopyableCode code="typeVersion" /> | `string` | The type version |
| <CopyableCode code="updateTime" /> | `integer` | The update time |
| <CopyableCode code="updatedBy" /> | `string` | The updater |
| <CopyableCode code="version" /> | `integer` | The version |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_business_metadata_defs" /> | `SELECT` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk retrieval API for retrieving business metadata definitions. |
| <CopyableCode code="get_business_metadata_def_by_name" /> | `SELECT` | <CopyableCode code="bmName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Get the business metadata definition with the given name. |
| <CopyableCode code="create_business_metadata_defs" /> | `INSERT` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk create API for business metadata definitions. |
| <CopyableCode code="delete_business_metadata_def" /> | `DELETE` | <CopyableCode code="bmName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Delete API for business metadata definition identified by its name. |
| <CopyableCode code="update_business_metadata_defs" /> | `EXEC` | <CopyableCode code="" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk update API for business metadata definitions. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Bulk retrieval API for retrieving business metadata definitions.


```sql
SELECT
name,
description,
attributeDefs,
category,
createTime,
createdBy,
guid,
options,
serviceType,
typeVersion,
updateTime,
updatedBy,
version
FROM confluent.catalog.business_metadata_defs
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>business_metadata_defs</code> resource.

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
INSERT INTO confluent.catalog.business_metadata_defs (

)
SELECT 

;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: business_metadata_defs
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>business_metadata_defs</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.catalog.business_metadata_defs
WHERE bmName = '{{ bmName }}';
```
