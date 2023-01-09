---
title: dynamic_targeting_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - dynamic_targeting_keys
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dynamic_targeting_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.dynamic_targeting_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#dynamicTargetingKeysListResponse". |
| `dynamicTargetingKeys` | `array` | Dynamic targeting key collection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `dynamicTargetingKeys_list` | `SELECT` | `profileId` | Retrieves a list of dynamic targeting keys. |
| `dynamicTargetingKeys_delete` | `DELETE` | `name, objectId, objectType, profileId` | Deletes an existing dynamic targeting key. |
| `dynamicTargetingKeys_insert` | `EXEC` | `profileId` | Inserts a new dynamic targeting key. Keys must be created at the advertiser level before being assigned to the advertiser's ads, creatives, or placements. There is a maximum of 1000 keys per advertiser, out of which a maximum of 20 keys can be assigned per ad, creative, or placement. |
