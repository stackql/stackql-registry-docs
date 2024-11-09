---
title: group_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - group_mappings
  - iam
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

Creates, updates, deletes, gets or lists a <code>group_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.group_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A description explaining the purpose and use of the group mapping. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | The name of the group mapping. |
| <CopyableCode code="filter" /> | `string` | A single group identifier or a condition based on [supported CEL operators](https://docs.confluent.io/cloud/current/access-management/authenticate/sso/group-mapping/overview.html#supported-cel-operators-for-group-mapping) that defines which groups are included. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="principal" /> | `string` | The unique federated identity associated with this group mapping. |
| <CopyableCode code="state" /> | `string` | The current state of the group mapping. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2sso_group_mapping" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to read a group mapping. |
| <CopyableCode code="list_iam_v2sso_group_mappings" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all group mappings. |
| <CopyableCode code="create_iam_v2sso_group_mapping" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to create a group mapping. |
| <CopyableCode code="delete_iam_v2sso_group_mapping" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to delete a group mapping. |
| <CopyableCode code="update_iam_v2sso_group_mapping" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to update a group mapping. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all group mappings.


```sql
SELECT
id,
description,
api_version,
display_name,
filter,
kind,
metadata,
principal,
state
FROM confluent.iam.group_mappings
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group_mappings</code> resource.

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
INSERT INTO confluent.iam.group_mappings (
data__display_name,
data__description,
data__filter
)
SELECT 
'{{ display_name }}',
'{{ description }}',
'{{ filter }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: group_mappings
  props:
    - name: display_name
      value: string
    - name: description
      value: string
    - name: filter
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>group_mappings</code> resource.

```sql
/*+ update */
UPDATE confluent.iam.group_mappings
SET 
metadata = '{{ metadata }}',
display_name = '{{ display_name }}',
description = '{{ description }}',
filter = '{{ filter }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>group_mappings</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.group_mappings
WHERE id = '{{ id }}';
```
