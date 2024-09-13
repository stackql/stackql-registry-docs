
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>effective_tag</code> resource or lists <code>effective_tags</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>effective_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.effective_tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="inherited" /> | `boolean` | Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource, inherited will be false. |
| <CopyableCode code="namespacedTagKey" /> | `string` | The namespaced name of the TagKey. Can be in the form `{organization_id}/{tag_key_short_name}` or `{project_id}/{tag_key_short_name}` or `{project_number}/{tag_key_short_name}`. |
| <CopyableCode code="namespacedTagValue" /> | `string` | The namespaced name of the TagValue. Can be in the form `{organization_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_number}/{tag_key_short_name}/{tag_value_short_name}`. |
| <CopyableCode code="tagKey" /> | `string` | The name of the TagKey, in the format `tagKeys/{id}`, such as `tagKeys/123`. |
| <CopyableCode code="tagKeyParentName" /> | `string` | The parent name of the tag key. Must be in the format `organizations/{organization_id}` or `projects/{project_number}` |
| <CopyableCode code="tagValue" /> | `string` | Resource name for TagValue in the format `tagValues/456`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Return a list of effective tags for the given Google Cloud resource, as specified in `parent`. |

## `SELECT` examples

Return a list of effective tags for the given Google Cloud resource, as specified in `parent`.

```sql
SELECT
inherited,
namespacedTagKey,
namespacedTagValue,
tagKey,
tagKeyParentName,
tagValue
FROM google.cloudresourcemanager.effective_tags
WHERE  = '{{  }}'; 
```
