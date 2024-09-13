---
title: tag_values_namespaced
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_values_namespaced
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

Creates, updates, deletes, gets or lists a <code>tag_values_namespaced</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_values_namespaced</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.tag_values_namespaced" /></td></tr>
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
| <CopyableCode code="get_namespaced" /> | `SELECT` | <CopyableCode code="" /> | Retrieves a TagValue by its namespaced name. This method will return `PERMISSION_DENIED` if the value does not exist or the user does not have permission to view it. |

## `SELECT` examples

Retrieves a TagValue by its namespaced name. This method will return `PERMISSION_DENIED` if the value does not exist or the user does not have permission to view it.

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
FROM google.cloudresourcemanager.tag_values_namespaced
WHERE  = '{{  }}'; 
```
