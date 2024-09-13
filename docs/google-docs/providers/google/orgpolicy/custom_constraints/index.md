---
title: custom_constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_constraints
  - orgpolicy
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

Creates, updates, deletes, gets or lists a <code>custom_constraints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.orgpolicy.custom_constraints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Name of the constraint. This is unique within the organization. Format of the name should be * `organizations/{organization_id}/customConstraints/{custom_constraint_id}` Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms` The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/` is not counted. |
| <CopyableCode code="description" /> | `string` | Detailed information about this custom policy constraint. The max length of the description is 2000 characters. |
| <CopyableCode code="actionType" /> | `string` | Allow or deny type. |
| <CopyableCode code="condition" /> | `string` | Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true` The max length of the condition is 1000 characters. |
| <CopyableCode code="displayName" /> | `string` | One line display name for the UI. The max length of the display_name is 200 characters. |
| <CopyableCode code="methodTypes" /> | `array` | All the operations being applied for this constraint. |
| <CopyableCode code="resourceTypes" /> | `array` | Immutable. The resource instance type on which this policy applies. Format will be of the form : `/` Example: * `compute.googleapis.com/Instance`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_custom_constraints_get" /> | `SELECT` | <CopyableCode code="customConstraintsId, organizationsId" /> | Gets a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the custom constraint does not exist. |
| <CopyableCode code="organizations_custom_constraints_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Retrieves all of the custom constraints that exist on a particular organization resource. |
| <CopyableCode code="organizations_custom_constraints_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the organization does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the constraint already exists on the given organization. |
| <CopyableCode code="organizations_custom_constraints_delete" /> | `DELETE` | <CopyableCode code="customConstraintsId, organizationsId" /> | Deletes a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. |
| <CopyableCode code="organizations_custom_constraints_patch" /> | `UPDATE` | <CopyableCode code="customConstraintsId, organizationsId" /> | Updates a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Note: the supplied policy will perform a full overwrite of all fields. |

## `SELECT` examples

Retrieves all of the custom constraints that exist on a particular organization resource.

```sql
SELECT
name,
description,
actionType,
condition,
displayName,
methodTypes,
resourceTypes,
updateTime
FROM google.orgpolicy.custom_constraints
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_constraints</code> resource.

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
INSERT INTO google.orgpolicy.custom_constraints (
organizationsId,
name,
methodTypes,
description,
resourceTypes,
displayName,
updateTime,
actionType,
condition
)
SELECT 
'{{ organizationsId }}',
'{{ name }}',
'{{ methodTypes }}',
'{{ description }}',
'{{ resourceTypes }}',
'{{ displayName }}',
'{{ updateTime }}',
'{{ actionType }}',
'{{ condition }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: methodTypes
        value: '{{ methodTypes }}'
      - name: description
        value: '{{ description }}'
      - name: resourceTypes
        value: '{{ resourceTypes }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: actionType
        value: '{{ actionType }}'
      - name: condition
        value: '{{ condition }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_constraints</code> resource.

```sql
/*+ update */
UPDATE google.orgpolicy.custom_constraints
SET 
name = '{{ name }}',
methodTypes = '{{ methodTypes }}',
description = '{{ description }}',
resourceTypes = '{{ resourceTypes }}',
displayName = '{{ displayName }}',
updateTime = '{{ updateTime }}',
actionType = '{{ actionType }}',
condition = '{{ condition }}'
WHERE 
customConstraintsId = '{{ customConstraintsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>custom_constraints</code> resource.

```sql
/*+ delete */
DELETE FROM google.orgpolicy.custom_constraints
WHERE customConstraintsId = '{{ customConstraintsId }}'
AND organizationsId = '{{ organizationsId }}';
```
