---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
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
<tr><td><b>Name</b></td><td><code>campaigns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.campaigns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this campaign. This is a read-only auto-generated field. |
| `name` | `string` | Name of this campaign. This is a required field and must be less than 512 characters long and unique among campaigns of the same advertiser. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `adBlockingConfiguration` | `object` | Campaign ad blocking settings. |
| `billingInvoiceCode` | `string` | Billing invoice code included in the Campaign Manager client billing invoices associated with the campaign. |
| `advertiserId` | `string` | Advertiser ID of this campaign. This is a required field. |
| `endDate` | `string` |  |
| `startDate` | `string` |  |
| `createInfo` | `object` | Modification timestamp. |
| `accountId` | `string` | Account ID of this campaign. This is a read-only field that can be left blank. |
| `additionalCreativeOptimizationConfigurations` | `array` | Additional creative optimization configurations for the campaign. |
| `advertiserGroupId` | `string` | Advertiser group ID of the associated advertiser. |
| `subaccountId` | `string` | Subaccount ID of this campaign. This is a read-only field that can be left blank. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#campaign". |
| `creativeGroupIds` | `array` | List of creative group IDs that are assigned to the campaign. |
| `archived` | `boolean` | Whether this campaign has been archived. |
| `measurementPartnerLink` | `object` |  |
| `creativeOptimizationConfiguration` | `object` | Creative optimization settings. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `defaultLandingPageId` | `string` | The default landing page ID for this campaign. |
| `comment` | `string` | Arbitrary comments about this campaign. Must be less than 256 characters long. |
| `clickThroughUrlSuffixProperties` | `object` | Click Through URL Suffix settings. |
| `eventTagOverrides` | `array` | Overrides that can be used to activate or deactivate advertiser event tags. |
| `audienceSegmentGroups` | `array` | Audience segment groups assigned to this campaign. Cannot have more than 300 segment groups. |
| `defaultClickThroughEventTagProperties` | `object` | Properties of inheriting and overriding the default click-through event tag. A campaign may override the event tag defined at the advertiser level, and an ad may also override the campaign's setting further. |
| `externalId` | `string` | External ID for this campaign. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one campaign by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of campaigns, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new campaign. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing campaign. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing campaign. |
