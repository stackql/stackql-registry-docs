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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.tag_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the TagBinding. This is a String of the form: `tagBindings/&#123;full-resource-name&#125;/&#123;tag-value-name&#125;` (e.g. `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456`). |
| <CopyableCode code="parent" /> | `string` | The full resource name of the resource the TagValue is bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123` |
| <CopyableCode code="tagValue" /> | `string` | The TagValue of the TagBinding. Must be of the form `tagValues/456`. |
| <CopyableCode code="tagValueNamespacedName" /> | `string` | The namespaced name for the TagValue of the TagBinding. Must be in the format `&#123;parent_id&#125;/&#123;tag_key_short_name&#125;/&#123;short_name&#125;`. For methods that support TagValue namespaced name, only one of tag_value_namespaced_name or tag_value may be filled. Requests with both fields will be rejected. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` |  | Lists the TagBindings for the given Google Cloud resource, as specified with `parent`. NOTE: The `parent` field is expected to be a full resource name: https://cloud.google.com/apis/design/resource_names#full_resource_name |
| <CopyableCode code="create" /> | `INSERT` |  | Creates a TagBinding between a TagValue and a Google Cloud resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="tagBindingsId" /> | Deletes a TagBinding. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists the TagBindings for the given Google Cloud resource, as specified with `parent`. NOTE: The `parent` field is expected to be a full resource name: https://cloud.google.com/apis/design/resource_names#full_resource_name |
