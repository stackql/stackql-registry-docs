---
title: advertisers
hide_title: false
hide_table_of_contents: false
keywords:
  - advertisers
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
<tr><td><b>Name</b></td><td><code>advertisers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.advertisers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this advertiser. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this advertiser. This is a required field and must be less than 256 characters long and unique among advertisers of the same account. |
| `subaccountId` | `string` | Subaccount ID of this advertiser.This is a read-only field that can be left blank. |
| `defaultEmail` | `string` | Default email address used in sender field for tag emails. |
| `suspended` | `boolean` | Suspension status of this advertiser. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `floodlightConfigurationId` | `string` | Floodlight configuration ID of this advertiser. The floodlight configuration ID will be created automatically, so on insert this field should be left blank. This field can be set to another advertiser's floodlight configuration ID in order to share that advertiser's floodlight configuration with this advertiser, so long as: - This advertiser's original floodlight configuration is not already associated with floodlight activities or floodlight activity groups. - This advertiser's original floodlight configuration is not already shared with another advertiser.  |
| `originalFloodlightConfigurationId` | `string` | Original floodlight configuration before any sharing occurred. Set the floodlightConfigurationId of this advertiser to originalFloodlightConfigurationId to unshare the advertiser's current floodlight configuration. You cannot unshare an advertiser's floodlight configuration if the shared configuration has activities associated with any campaign or placement. |
| `defaultClickThroughEventTagId` | `string` | ID of the click-through event tag to apply by default to the landing pages of this advertiser's campaigns. |
| `clickThroughUrlSuffix` | `string` | Suffix added to click-through URL of ad creative associations under this advertiser. Must be less than 129 characters long. |
| `advertiserGroupId` | `string` | ID of the advertiser group this advertiser belongs to. You can group advertisers for reporting purposes, allowing you to see aggregated information for all advertisers in each group. |
| `floodlightConfigurationIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#advertiser". |
| `status` | `string` | Status of this advertiser. |
| `measurementPartnerLink` | `object` |  |
| `accountId` | `string` | Account ID of this advertiser.This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one advertiser by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of advertisers, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new advertiser. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing advertiser. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing advertiser. |
