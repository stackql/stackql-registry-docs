---
title: tag_values
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_values
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

Creates, updates, deletes, gets or lists a <code>tag_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.tag_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Resource name for TagValue in the format `tagValues/456`. |
| <CopyableCode code="description" /> | `string` | Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time. |
| <CopyableCode code="etag" /> | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details. |
| <CopyableCode code="namespacedName" /> | `string` | Output only. The namespaced name of the TagValue. Can be in the form `{organization_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_number}/{tag_key_short_name}/{tag_value_short_name}`. |
| <CopyableCode code="parent" /> | `string` | Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/{tag_key_id}`. |
| <CopyableCode code="shortName" /> | `string` | Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="tagValuesId" /> | Retrieves a TagValue. This method will return `PERMISSION_DENIED` if the value does not exist or the user does not have permission to view it. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all TagValues for a specific TagKey. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a TagValue as a child of the specified TagKey. If a another request with the same parameters is sent while the original request is in process the second request will receive an error. A maximum of 1000 TagValues can exist under a TagKey at any given time. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="tagValuesId" /> | Deletes a TagValue. The TagValue cannot have any bindings when it is deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="tagValuesId" /> | Updates the attributes of the TagValue resource. |

## `SELECT` examples

Lists all TagValues for a specific TagKey.

```sql
SELECT
name,
description,
createTime,
etag,
namespacedName,
parent,
shortName,
updateTime
FROM google.cloudresourcemanager.tag_values
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_values</code> resource.

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
INSERT INTO google.cloudresourcemanager.tag_values (
,
name,
parent,
shortName,
namespacedName,
description,
createTime,
updateTime,
etag
)
SELECT 
'{{  }}',
'{{ name }}',
'{{ parent }}',
'{{ shortName }}',
'{{ namespacedName }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ etag }}'
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
      - name: parent
        value: '{{ parent }}'
      - name: shortName
        value: '{{ shortName }}'
      - name: namespacedName
        value: '{{ namespacedName }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: etag
        value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tag_values</code> resource.

```sql
/*+ update */
UPDATE google.cloudresourcemanager.tag_values
SET 
name = '{{ name }}',
parent = '{{ parent }}',
shortName = '{{ shortName }}',
namespacedName = '{{ namespacedName }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
etag = '{{ etag }}'
WHERE 
tagValuesId = '{{ tagValuesId }}';
```

## `DELETE` example

Deletes the specified <code>tag_values</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudresourcemanager.tag_values
WHERE tagValuesId = '{{ tagValuesId }}';
```
