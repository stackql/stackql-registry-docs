---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - cloudidentity
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Group`. Shall be of the form `groups/{group}`. |
| <CopyableCode code="description" /> | `string` | An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters. |
| <CopyableCode code="additionalGroupKeys" /> | `array` | Output only. Additional group keys associated with the Group. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the `Group` was created. |
| <CopyableCode code="displayName" /> | `string` | The display name of the `Group`. |
| <CopyableCode code="dynamicGroupMetadata" /> | `object` | Dynamic group metadata like queries and status. |
| <CopyableCode code="groupKey" /> | `object` | A unique identifier for an entity in the Cloud Identity Groups API. An entity can represent either a group with an optional `namespace` or a user without a `namespace`. The combination of `id` and `namespace` must be unique; however, the same `id` can be used with different `namespace`s. |
| <CopyableCode code="labels" /> | `object` | Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value. |
| <CopyableCode code="parent" /> | `string` | Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source}` for external [identity-mapped groups](https://support.google.com/a/answer/9039510) or `customers/{customer_id}` for Google Groups. The `customer_id` must begin with "C" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the `Group` was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId" /> | Retrieves a `Group`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists the `Group` resources under a customer or namespace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupsId" /> | Deletes a `Group`. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="groupsId" /> | Updates a `Group`. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="" /> | Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Group` by its `EntityKey`. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="" /> | Searches for `Group` resources matching a specified query. |

## `SELECT` examples

Lists the `Group` resources under a customer or namespace.

```sql
SELECT
name,
description,
additionalGroupKeys,
createTime,
displayName,
dynamicGroupMetadata,
groupKey,
labels,
parent,
updateTime
FROM google.cloudidentity.groups
;
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

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
INSERT INTO google.cloudidentity.groups (
groupKey,
parent,
displayName,
description,
labels,
dynamicGroupMetadata
)
SELECT 
'{{ groupKey }}',
'{{ parent }}',
'{{ displayName }}',
'{{ description }}',
'{{ labels }}',
'{{ dynamicGroupMetadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: groupKey
      value:
        - name: id
          value: string
        - name: namespace
          value: string
    - name: additionalGroupKeys
      value:
        - - name: id
            value: string
          - name: namespace
            value: string
    - name: parent
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: dynamicGroupMetadata
      value:
        - name: queries
          value:
            - - name: resourceType
                value: string
              - name: query
                value: string
        - name: status
          value:
            - name: status
              value: string
            - name: statusTime
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>groups</code> resource.

```sql
/*+ update */
UPDATE google.cloudidentity.groups
SET 
groupKey = '{{ groupKey }}',
parent = '{{ parent }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
labels = '{{ labels }}',
dynamicGroupMetadata = '{{ dynamicGroupMetadata }}'
WHERE 
groupsId = '{{ groupsId }}';
```

## `DELETE` example

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudidentity.groups
WHERE groupsId = '{{ groupsId }}';
```
