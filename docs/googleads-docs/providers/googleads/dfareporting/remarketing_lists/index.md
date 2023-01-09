---
title: remarketing_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - remarketing_lists
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
<tr><td><b>Name</b></td><td><code>remarketing_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.remarketing_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Remarketing list ID. This is a read-only, auto-generated field. |
| `name` | `string` | Name of the remarketing list. This is a required field. Must be no greater than 128 characters long. |
| `description` | `string` | Remarketing list description. |
| `lifeSpan` | `string` | Number of days that a user should remain in the remarketing list without an impression. Acceptable values are 1 to 540, inclusive. |
| `listPopulationRule` | `object` | Remarketing List Population Rule. |
| `listSize` | `string` | Number of users currently in the list. This is a read-only field. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#remarketingList". |
| `active` | `boolean` | Whether this remarketing list is active. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `accountId` | `string` | Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |
| `advertiserId` | `string` | Dimension value for the advertiser ID that owns this remarketing list. This is a required field. |
| `listSource` | `string` | Product from which this remarketing list was originated. |
| `subaccountId` | `string` | Subaccount ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `remarketingLists_get` | `SELECT` | `id, profileId` | Gets one remarketing list by ID. |
| `remarketingLists_list` | `SELECT` | `advertiserId, profileId` | Retrieves a list of remarketing lists, possibly filtered. This method supports paging. |
| `remarketingLists_insert` | `EXEC` | `profileId` | Inserts a new remarketing list. |
| `remarketingLists_patch` | `EXEC` | `id, profileId` | Updates an existing remarketing list. This method supports patch semantics. |
| `remarketingLists_update` | `EXEC` | `profileId` | Updates an existing remarketing list. |
