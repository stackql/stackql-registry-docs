---
title: effective_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - effective_tags
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
<tr><td><b>Name</b></td><td><code>effective_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.effective_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inherited` | `boolean` | Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource, inherited will be false. |
| `namespacedTagKey` | `string` | The namespaced name of the TagKey. Can be in the form `&#123;organization_id&#125;/&#123;tag_key_short_name&#125;` or `&#123;project_id&#125;/&#123;tag_key_short_name&#125;` or `&#123;project_number&#125;/&#123;tag_key_short_name&#125;`. |
| `namespacedTagValue` | `string` | The namespaced name of the TagValue. Can be in the form `&#123;organization_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;` or `&#123;project_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;` or `&#123;project_number&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;`. |
| `tagKey` | `string` | The name of the TagKey, in the format `tagKeys/&#123;id&#125;`, such as `tagKeys/123`. |
| `tagKeyParentName` | `string` | The parent name of the tag key. Must be in the format `organizations/&#123;organization_id&#125;` or `projects/&#123;project_number&#125;` |
| `tagValue` | `string` | Resource name for TagValue in the format `tagValues/456`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
