---
title: tag_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_bindings
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

Creates, updates, deletes, gets or lists a <code>tag_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.tag_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the TagBinding. This is a String of the form: `tagBindings/{full-resource-name}/{tag-value-name}` (e.g. `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456`). |
| <CopyableCode code="parent" /> | `string` | The full resource name of the resource the TagValue is bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123` |
| <CopyableCode code="tagValue" /> | `string` | The TagValue of the TagBinding. Must be of the form `tagValues/456`. |
| <CopyableCode code="tagValueNamespacedName" /> | `string` | The namespaced name for the TagValue of the TagBinding. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`. For methods that support TagValue namespaced name, only one of tag_value_namespaced_name or tag_value may be filled. Requests with both fields will be rejected. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists the TagBindings for the given Google Cloud resource, as specified with `parent`. NOTE: The `parent` field is expected to be a full resource name: https://cloud.google.com/apis/design/resource_names#full_resource_name |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a TagBinding between a TagValue and a Google Cloud resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="tagBindingsId" /> | Deletes a TagBinding. |

## `SELECT` examples

Lists the TagBindings for the given Google Cloud resource, as specified with `parent`. NOTE: The `parent` field is expected to be a full resource name: https://cloud.google.com/apis/design/resource_names#full_resource_name

```sql
SELECT
name,
parent,
tagValue,
tagValueNamespacedName
FROM google.cloudresourcemanager.tag_bindings
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_bindings</code> resource.

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
INSERT INTO google.cloudresourcemanager.tag_bindings (
,
parent,
tagValue,
tagValueNamespacedName
)
SELECT 
'{{  }}',
'{{ parent }}',
'{{ tagValue }}',
'{{ tagValueNamespacedName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: parent
      value: '{{ parent }}'
    - name: tagValue
      value: '{{ tagValue }}'
    - name: tagValueNamespacedName
      value: '{{ tagValueNamespacedName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tag_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudresourcemanager.tag_bindings
WHERE tagBindingsId = '{{ tagBindingsId }}';
```
