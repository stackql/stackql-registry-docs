---
title: role_management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policies
  - authorization
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>role_management_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_management_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_management_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_management_policies', value: 'view', },
        { label: 'role_management_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The role management policy Id. |
| <CopyableCode code="name" /> | `text` | The role management policy name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="effective_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_organization_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleManagementPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The role management policy type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role management policy Id. |
| <CopyableCode code="name" /> | `string` | The role management policy name. |
| <CopyableCode code="properties" /> | `object` | Role management policy properties with scope. |
| <CopyableCode code="type" /> | `string` | The role management policy type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleManagementPolicyName, scope" /> | Get the specified role management policy for a resource scope |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets role management policies for a resource scope. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleManagementPolicyName, scope" /> | Delete a role management policy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="roleManagementPolicyName, scope" /> | Update a role management policy |

## `SELECT` examples

Gets role management policies for a resource scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_management_policies', value: 'view', },
        { label: 'role_management_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
display_name,
effective_rules,
is_organization_default,
last_modified_by,
last_modified_date_time,
policy_properties,
roleManagementPolicyName,
rules,
scope,
type
FROM azure.authorization.vw_role_management_policies
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.role_management_policies
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>role_management_policies</code> resource.

```sql
/*+ update */
UPDATE azure.authorization.role_management_policies
SET 
properties = '{{ properties }}'
WHERE 
roleManagementPolicyName = '{{ roleManagementPolicyName }}'
AND scope = '{{ scope }}';
```

## `DELETE` example

Deletes the specified <code>role_management_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.authorization.role_management_policies
WHERE roleManagementPolicyName = '{{ roleManagementPolicyName }}'
AND scope = '{{ scope }}';
```
