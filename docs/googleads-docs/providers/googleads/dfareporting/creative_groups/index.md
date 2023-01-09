---
title: creative_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - creative_groups
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
<tr><td><b>Name</b></td><td><code>creative_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.creative_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this creative group. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this creative group. This is a required field and must be less than 256 characters long and unique among creative groups of the same advertiser. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#creativeGroup". |
| `subaccountId` | `string` | Subaccount ID of this creative group. This is a read-only field that can be left blank. |
| `accountId` | `string` | Account ID of this creative group. This is a read-only field that can be left blank. |
| `advertiserId` | `string` | Advertiser ID of this creative group. This is a required field on insertion. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `groupNumber` | `integer` | Subgroup of the creative group. Assign your creative groups to a subgroup in order to filter or manage them more easily. This field is required on insertion and is read-only after insertion. Acceptable values are 1 to 2, inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `creativeGroups_get` | `SELECT` | `id, profileId` | Gets one creative group by ID. |
| `creativeGroups_list` | `SELECT` | `profileId` | Retrieves a list of creative groups, possibly filtered. This method supports paging. |
| `creativeGroups_insert` | `EXEC` | `profileId` | Inserts a new creative group. |
| `creativeGroups_patch` | `EXEC` | `id, profileId` | Updates an existing creative group. This method supports patch semantics. |
| `creativeGroups_update` | `EXEC` | `profileId` | Updates an existing creative group. |
