---
title: floodlight_activity_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - floodlight_activity_groups
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
<tr><td><b>Name</b></td><td><code>floodlight_activity_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.floodlight_activity_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this floodlight activity group. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this floodlight activity group. This is a required field. Must be less than 65 characters long and cannot contain quotes. |
| `advertiserId` | `string` | Advertiser ID of this floodlight activity group. If this field is left blank, the value will be copied over either from the floodlight configuration's advertiser or from the existing activity group's advertiser. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#floodlightActivityGroup". |
| `tagString` | `string` | Value of the type= parameter in the floodlight tag, which the ad servers use to identify the activity group that the activity belongs to. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being a-z0-9[ _ ]. This tag string must also be unique among activity groups of the same floodlight configuration. This field is read-only after insertion. |
| `type` | `string` | Type of the floodlight activity group. This is a required field that is read-only after insertion. |
| `floodlightConfigurationIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `floodlightConfigurationId` | `string` | Floodlight configuration ID of this floodlight activity group. This is a required field. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `accountId` | `string` | Account ID of this floodlight activity group. This is a read-only field that can be left blank. |
| `subaccountId` | `string` | Subaccount ID of this floodlight activity group. This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `floodlightActivityGroups_get` | `SELECT` | `id, profileId` | Gets one floodlight activity group by ID. |
| `floodlightActivityGroups_list` | `SELECT` | `profileId` | Retrieves a list of floodlight activity groups, possibly filtered. This method supports paging. |
| `floodlightActivityGroups_insert` | `EXEC` | `profileId` | Inserts a new floodlight activity group. |
| `floodlightActivityGroups_patch` | `EXEC` | `id, profileId` | Updates an existing floodlight activity group. This method supports patch semantics. |
| `floodlightActivityGroups_update` | `EXEC` | `profileId` | Updates an existing floodlight activity group. |
