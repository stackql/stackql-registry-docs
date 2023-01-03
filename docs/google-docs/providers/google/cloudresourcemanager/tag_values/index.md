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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.tag_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Resource name for TagValue in the format `tagValues/456`. |
| `description` | `string` | Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write. |
| `namespacedName` | `string` | Output only. Namespaced name of the TagValue. Must be in the format `{organization_id}/{tag_key_short_name}/{short_name}`. |
| `parent` | `string` | Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/{tag_key_id}`. |
| `shortName` | `string` | Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `updateTime` | `string` | Output only. Update time. |
| `createTime` | `string` | Output only. Creation time. |
| `etag` | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `tagValues_get` | `SELECT` | `tagValuesId` | Retrieves TagValue. If the TagValue or namespaced name does not exist, or if the user does not have permission to view it, this method will return `PERMISSION_DENIED`. |
| `tagValues_list` | `SELECT` |  | Lists all TagValues for a specific TagKey. |
| `tagValues_create` | `INSERT` |  | Creates a TagValue as a child of the specified TagKey. If a another request with the same parameters is sent while the original request is in process the second request will receive an error. A maximum of 1000 TagValues can exist under a TagKey at any given time. |
| `tagValues_delete` | `DELETE` | `tagValuesId` | Deletes a TagValue. The TagValue cannot have any bindings when it is deleted. |
| `tagValues_patch` | `EXEC` | `tagValuesId` | Updates the attributes of the TagValue resource. |
