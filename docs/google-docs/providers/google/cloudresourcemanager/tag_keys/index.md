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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.tag_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name for a TagKey. Must be in the format `tagKeys/{tag_key_id}`, where `tag_key_id` is the generated numeric id for the TagKey. |
| `description` | `string` | Optional. User-assigned description of the TagKey. Must not exceed 256 characters. Read-write. |
| `purpose` | `string` | Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines. A purpose cannot be changed once set. |
| `shortName` | `string` | Required. Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace. The short name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `purposeData` | `object` | Optional. Purpose data corresponds to the policy system that the tag is intended for. See documentation for `Purpose` for formatting of this field. Purpose data cannot be changed once set. |
| `createTime` | `string` | Output only. Creation time. |
| `etag` | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details. |
| `namespacedName` | `string` | Output only. Immutable. Namespaced name of the TagKey. |
| `updateTime` | `string` | Output only. Update time. |
| `parent` | `string` | Immutable. The resource name of the new TagKey's parent. Must be of the form `organizations/{org_id}`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `tagKeys_get` | `SELECT` | `tagKeysId` | Retrieves a TagKey. This method will return `PERMISSION_DENIED` if the key does not exist or the user does not have permission to view it. |
| `tagKeys_list` | `SELECT` |  | Lists all TagKeys for a parent resource. |
| `tagKeys_create` | `INSERT` |  | Creates a new TagKey. If another request with the same parameters is sent while the original request is in process, the second request will receive an error. A maximum of 1000 TagKeys can exist under a parent at any given time. |
| `tagKeys_delete` | `DELETE` | `tagKeysId` | Deletes a TagKey. The TagKey cannot be deleted if it has any child TagValues. |
| `tagKeys_patch` | `EXEC` | `tagKeysId` | Updates the attributes of the TagKey resource. |
