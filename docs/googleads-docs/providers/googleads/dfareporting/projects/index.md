---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this project. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this project. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#project". |
| `advertiserId` | `string` | Advertiser ID of this project. |
| `subaccountId` | `string` | Subaccount ID of this project. |
| `targetCpcNanos` | `string` | CPC that the advertiser is targeting. |
| `endDate` | `string` |  |
| `targetCpmActiveViewNanos` | `string` | vCPM from Active View that the advertiser is targeting. |
| `targetCpaNanos` | `string` | CPA that the advertiser is targeting. |
| `accountId` | `string` | Account ID of this project. |
| `audienceAgeGroup` | `string` | Audience age group of this project. |
| `overview` | `string` | Overview of this project. |
| `clientBillingCode` | `string` | Client billing code of this project. |
| `targetClicks` | `string` | Number of clicks that the advertiser is targeting. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `clientName` | `string` | Name of the project client. |
| `targetCpmNanos` | `string` | CPM that the advertiser is targeting. |
| `startDate` | `string` |  |
| `targetConversions` | `string` | Number of conversions that the advertiser is targeting. |
| `audienceGender` | `string` | Audience gender of this project. |
| `budget` | `string` | Budget of this project in the currency specified by the current account. The value stored in this field represents only the non-fractional amount. For example, for USD, the smallest value that can be represented by this field is 1 US dollar. |
| `targetImpressions` | `string` | Number of impressions that the advertiser is targeting. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one project by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of projects, possibly filtered. This method supports paging . |
