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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudresourcemanager.tag_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Resource name for TagValue in the format `tagValues/456`. |
| <CopyableCode code="description" /> | `string` | Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time. |
| <CopyableCode code="etag" /> | `string` | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details. |
| <CopyableCode code="namespacedName" /> | `string` | Output only. The namespaced name of the TagValue. Can be in the form `&#123;organization_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;` or `&#123;project_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;` or `&#123;project_number&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;`. |
| <CopyableCode code="parent" /> | `string` | Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/&#123;tag_key_id&#125;`. |
| <CopyableCode code="shortName" /> | `string` | Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="tagValuesId" /> | Retrieves a TagValue. This method will return `PERMISSION_DENIED` if the value does not exist or the user does not have permission to view it. |
| <CopyableCode code="list" /> | `SELECT` |  | Lists all TagValues for a specific TagKey. |
| <CopyableCode code="create" /> | `INSERT` |  | Creates a TagValue as a child of the specified TagKey. If a another request with the same parameters is sent while the original request is in process the second request will receive an error. A maximum of 1000 TagValues can exist under a TagKey at any given time. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="tagValuesId" /> | Deletes a TagValue. The TagValue cannot have any bindings when it is deleted. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists all TagValues for a specific TagKey. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="tagValuesId" /> | Updates the attributes of the TagValue resource. |
