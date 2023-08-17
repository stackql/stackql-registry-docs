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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_values_namespaced</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.tag_values_namespaced</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Resource name for TagValue in the format `tagValues/456`. |
| `description` | `string` | Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write. |
| `namespacedName` | `string` | Output only. The namespaced name of the TagValue. Can be in the form `&#123;organization_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;` or `&#123;project_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;` or `&#123;project_number&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;`. |
| `parent` | `string` | Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/&#123;tag_key_id&#125;`. |
| `shortName` | `string` | Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `updateTime` | `string` | Output only. Update time. |
| `createTime` | `string` | Output only. Creation time. |
| `etag` | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_namespaced` | `SELECT` |  |
