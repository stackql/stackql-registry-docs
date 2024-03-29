---
title: tag_keys_namespaced
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_keys_namespaced
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_keys_namespaced</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.tag_keys_namespaced</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name for a TagKey. Must be in the format `tagKeys/&#123;tag_key_id&#125;`, where `tag_key_id` is the generated numeric id for the TagKey. |
| `description` | `string` | Optional. User-assigned description of the TagKey. Must not exceed 256 characters. Read-write. |
| `etag` | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details. |
| `parent` | `string` | Immutable. The resource name of the TagKey's parent. A TagKey can be parented by an Organization or a Project. For a TagKey parented by an Organization, its parent must be in the form `organizations/&#123;org_id&#125;`. For a TagKey parented by a Project, its parent can be in the form `projects/&#123;project_id&#125;` or `projects/&#123;project_number&#125;`. |
| `updateTime` | `string` | Output only. Update time. |
| `namespacedName` | `string` | Output only. Immutable. Namespaced name of the TagKey. |
| `purpose` | `string` | Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines. A purpose cannot be changed once set. |
| `shortName` | `string` | Required. Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace. The short name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `createTime` | `string` | Output only. Creation time. |
| `purposeData` | `object` | Optional. Purpose data corresponds to the policy system that the tag is intended for. See documentation for `Purpose` for formatting of this field. Purpose data cannot be changed once set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_namespaced` | `SELECT` |  |
