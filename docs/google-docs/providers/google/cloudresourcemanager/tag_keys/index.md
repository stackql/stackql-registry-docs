---
title: tag_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_keys
  - cloudresourcemanager
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

Creates, updates, deletes, gets or lists a <code>tag_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.tag_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name for a TagKey. Must be in the format `tagKeys/{tag_key_id}`, where `tag_key_id` is the generated numeric id for the TagKey. |
| <CopyableCode code="description" /> | `string` | Optional. User-assigned description of the TagKey. Must not exceed 256 characters. Read-write. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time. |
| <CopyableCode code="etag" /> | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details. |
| <CopyableCode code="namespacedName" /> | `string` | Output only. Immutable. Namespaced name of the TagKey. |
| <CopyableCode code="parent" /> | `string` | Immutable. The resource name of the TagKey's parent. A TagKey can be parented by an Organization or a Project. For a TagKey parented by an Organization, its parent must be in the form `organizations/{org_id}`. For a TagKey parented by a Project, its parent can be in the form `projects/{project_id}` or `projects/{project_number}`. |
| <CopyableCode code="purpose" /> | `string` | Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines. A purpose cannot be changed once set. |
| <CopyableCode code="purposeData" /> | `object` | Optional. Purpose data corresponds to the policy system that the tag is intended for. See documentation for `Purpose` for formatting of this field. Purpose data cannot be changed once set. |
| <CopyableCode code="shortName" /> | `string` | Required. Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace. The short name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="tagKeysId" /> | Retrieves a TagKey. This method will return `PERMISSION_DENIED` if the key does not exist or the user does not have permission to view it. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all TagKeys for a parent resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a new TagKey. If another request with the same parameters is sent while the original request is in process, the second request will receive an error. A maximum of 1000 TagKeys can exist under a parent at any given time. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="tagKeysId" /> | Deletes a TagKey. The TagKey cannot be deleted if it has any child TagValues. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="tagKeysId" /> | Updates the attributes of the TagKey resource. |

## `SELECT` examples

Lists all TagKeys for a parent resource.

```sql
SELECT
name,
description,
createTime,
etag,
namespacedName,
parent,
purpose,
purposeData,
shortName,
updateTime
FROM google.cloudresourcemanager.tag_keys
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_keys</code> resource.

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
INSERT INTO google.cloudresourcemanager.tag_keys (
,
name,
parent,
shortName,
description,
etag,
purpose,
purposeData
)
SELECT 
'{{  }}',
'{{ name }}',
'{{ parent }}',
'{{ shortName }}',
'{{ description }}',
'{{ etag }}',
'{{ purpose }}',
'{{ purposeData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: parent
      value: '{{ parent }}'
    - name: shortName
      value: '{{ shortName }}'
    - name: description
      value: '{{ description }}'
    - name: etag
      value: '{{ etag }}'
    - name: purpose
      value: '{{ purpose }}'
    - name: purposeData
      value: '{{ purposeData }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tag_keys</code> resource.

```sql
/*+ update */
UPDATE google.cloudresourcemanager.tag_keys
SET 
name = '{{ name }}',
parent = '{{ parent }}',
shortName = '{{ shortName }}',
description = '{{ description }}',
etag = '{{ etag }}',
purpose = '{{ purpose }}',
purposeData = '{{ purposeData }}'
WHERE 
tagKeysId = '{{ tagKeysId }}';
```

## `DELETE` example

Deletes the specified <code>tag_keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudresourcemanager.tag_keys
WHERE tagKeysId = '{{ tagKeysId }}';
```
