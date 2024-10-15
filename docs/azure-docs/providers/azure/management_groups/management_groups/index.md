---
title: management_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - management_groups
  - management_groups
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

Creates, updates, deletes, gets or lists a <code>management_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.management_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_groups', value: 'view', },
        { label: 'management_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 |
| <CopyableCode code="name" /> | `text` | The name of the management group. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="children" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource.  For example, Microsoft.Management/managementGroups |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 |
| <CopyableCode code="name" /> | `string` | The name of the management group. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="properties" /> | `object` | The generic properties of a management group. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId" /> | Get the details of the management group.
 |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List management groups for the authenticated user.
 |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId" /> | Create or update a management group.
If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.
 |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId" /> | Delete management group.
If a management group contains child resources, the request will fail.
 |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupId" /> | Update a management group.
 |

## `SELECT` examples

List management groups for the authenticated user.


<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_groups', value: 'view', },
        { label: 'management_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
children,
details,
display_name,
groupId,
tenant_id,
type
FROM azure.management_groups.vw_management_groups
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.management_groups.management_groups
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_groups</code> resource.

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
INSERT INTO azure.management_groups.management_groups (
groupId,
name,
properties
)
SELECT 
'{{ groupId }}',
'{{ name }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: type
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: tenantId
          value: string
        - name: displayName
          value: string
        - name: details
          value:
            - name: version
              value: number
            - name: updatedTime
              value: string
            - name: updatedBy
              value: string
            - name: parent
              value:
                - name: id
                  value: string
                - name: name
                  value: string
                - name: displayName
                  value: string
        - name: children
          value:
            - - name: type
                value: []
              - name: id
                value: string
              - name: name
                value: string
              - name: displayName
                value: string
              - name: children
                value:
                  - - name: id
                      value: string
                    - name: name
                      value: string
                    - name: displayName
                      value: string
                    - name: children
                      value:
                        - - name: id
                            value: string
                          - name: name
                            value: string
                          - name: displayName
                            value: string
                          - name: children
                            value:
                              - - name: id
                                  value: string
                                - name: name
                                  value: string
                                - name: displayName
                                  value: string
                                - name: children
                                  value:
                                    - - name: id
                                        value: string
                                      - name: name
                                        value: string
                                      - name: displayName
                                        value: string
                                      - name: children
                                        value:
                                          - - name: id
                                              value: string
                                            - name: name
                                              value: string
                                            - name: displayName
                                              value: string
                                            - name: children
                                              value:
                                                - - name: id
                                                    value: string
                                                  - name: name
                                                    value: string
                                                  - name: displayName
                                                    value: string
                                                  - name: children
                                                    value:
                                                      - - name: id
                                                          value: string
                                                        - name: name
                                                          value: string
                                                        - name: displayName
                                                          value: string
                                                        - name: children
                                                          value:
                                                            - - name: id
                                                                value: string
                                                              - name: name
                                                                value: string
                                                              - name: displayName
                                                                value: string
                                                              - name: children
                                                                value:
                                                                  - []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>management_groups</code> resource.

```sql
/*+ update */
UPDATE azure.management_groups.management_groups
SET 
displayName = '{{ displayName }}',
parentGroupId = '{{ parentGroupId }}'
WHERE 
groupId = '{{ groupId }}';
```

## `DELETE` example

Deletes the specified <code>management_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.management_groups.management_groups
WHERE groupId = '{{ groupId }}';
```
