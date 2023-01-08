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
| `tagValue` | `string` | Resource name for TagValue in the format `tagValues/456`. |
| `inherited` | `boolean` | Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource, inherited will be false. |
| `namespacedTagKey` | `string` | The namespaced_name of the TagKey. Now only supported in the format of `&#123;organization_id&#125;/&#123;tag_key_short_name&#125;`. Other formats will be supported when we add non-org parented tags. |
| `namespacedTagValue` | `string` | Namespaced name of the TagValue. Now only supported in the format `&#123;organization_id&#125;/&#123;tag_key_short_name&#125;/&#123;tag_value_short_name&#125;`. Other formats will be supported when we add non-org parented tags. |
| `tagKey` | `string` | The name of the TagKey, in the format `tagKeys/&#123;id&#125;`, such as `tagKeys/123`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `effectiveTags_list` | `SELECT` |  |
