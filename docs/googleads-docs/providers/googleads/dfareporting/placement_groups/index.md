---
title: placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_groups
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
<tr><td><b>Name</b></td><td><code>placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.placement_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this placement group. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this placement group. This is a required field and must be less than 256 characters long. |
| `pricingSchedule` | `object` | Pricing Schedule |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `directorySiteId` | `string` | Directory site ID associated with this placement group. On insert, you must set either this field or the site_id field to specify the site associated with this placement group. This is a required field that is read-only after insertion. |
| `externalId` | `string` | External ID for this placement. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#placementGroup". |
| `campaignId` | `string` | Campaign ID of this placement group. This field is required on insertion. |
| `primaryPlacementId` | `string` | ID of the primary placement, used to calculate the media cost of a roadblock (placement group). Modifying this field will automatically modify the primary field on all affected roadblock child placements. |
| `createInfo` | `object` | Modification timestamp. |
| `siteId` | `string` | Site ID associated with this placement group. On insert, you must set either this field or the directorySiteId field to specify the site associated with this placement group. This is a required field that is read-only after insertion. |
| `placementGroupType` | `string` | Type of this placement group. A package is a simple group of placements that acts as a single pricing point for a group of tags. A roadblock is a group of placements that not only acts as a single pricing point, but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned placements to be marked as primary for reporting. This field is required on insertion. |
| `directorySiteIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `childPlacementIds` | `array` | IDs of placements which are assigned to this placement group. This is a read-only, auto-generated field. |
| `comment` | `string` | Comments for this placement group. |
| `campaignIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `advertiserId` | `string` | Advertiser ID of this placement group. This is a required field on insertion. |
| `accountId` | `string` | Account ID of this placement group. This is a read-only field that can be left blank. |
| `siteIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `contentCategoryId` | `string` | ID of the content category assigned to this placement group. |
| `activeStatus` | `string` | Whether this placement group is active, inactive, archived or permanently archived. |
| `placementStrategyId` | `string` | ID of the placement strategy assigned to this placement group. |
| `subaccountId` | `string` | Subaccount ID of this placement group. This is a read-only field that can be left blank. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `primaryPlacementIdDimensionValue` | `object` | Represents a DimensionValue resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `placementGroups_get` | `SELECT` | `id, profileId` | Gets one placement group by ID. |
| `placementGroups_list` | `SELECT` | `profileId` | Retrieves a list of placement groups, possibly filtered. This method supports paging. |
| `placementGroups_insert` | `EXEC` | `profileId` | Inserts a new placement group. |
| `placementGroups_patch` | `EXEC` | `id, profileId` | Updates an existing placement group. This method supports patch semantics. |
| `placementGroups_update` | `EXEC` | `profileId` | Updates an existing placement group. |
