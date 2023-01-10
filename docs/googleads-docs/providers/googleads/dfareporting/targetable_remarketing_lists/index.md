---
title: targetable_remarketing_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - targetable_remarketing_lists
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
<tr><td><b>Name</b></td><td><code>targetable_remarketing_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.targetable_remarketing_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Targetable remarketing list ID. |
| `name` | `string` | Name of the targetable remarketing list. Is no greater than 128 characters long. |
| `description` | `string` | Targetable remarketing list description. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#targetableRemarketingList". |
| `accountId` | `string` | Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |
| `active` | `boolean` | Whether this targetable remarketing list is active. |
| `listSize` | `string` | Number of users currently in the list. This is a read-only field. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `subaccountId` | `string` | Subaccount ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |
| `lifeSpan` | `string` | Number of days that a user should remain in the targetable remarketing list without an impression. |
| `listSource` | `string` | Product from which this targetable remarketing list was originated. |
| `advertiserId` | `string` | Dimension value for the advertiser ID that owns this targetable remarketing list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `targetableRemarketingLists_get` | `SELECT` | `id, profileId` | Gets one remarketing list by ID. |
| `targetableRemarketingLists_list` | `SELECT` | `advertiserId, profileId` | Retrieves a list of targetable remarketing lists, possibly filtered. This method supports paging. |
