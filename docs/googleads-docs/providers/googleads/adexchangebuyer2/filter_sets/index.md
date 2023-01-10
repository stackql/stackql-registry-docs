---
title: filter_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - filter_sets
  - adexchangebuyer2
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
<tr><td><b>Name</b></td><td><code>filter_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.filter_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the filter set. Filter set names must be unique globally and match one of the patterns: - `bidders/*/filterSets/*` (for accessing bidder-level troubleshooting data) - `bidders/*/accounts/*/filterSets/*` (for accessing account-level troubleshooting data) This field is required in create operations. |
| `absoluteDateRange` | `object` | An absolute date range, specified by its start date and end date. The supported range of dates begins 30 days before today and ends today. Validity checked upon filter set creation. If a filter set with an absolute date range is run at a later date more than 30 days after start_date, it will fail. |
| `realtimeTimeRange` | `object` | An open-ended realtime time range specified by the start timestamp. For filter sets that specify a realtime time range RTB metrics continue to be aggregated throughout the lifetime of the filter set. |
| `dealId` | `string` | The ID of the deal on which to filter; optional. This field may be set only for a filter set that accesses account-level troubleshooting data, for example, one whose name matches the `bidders/*/accounts/*/filterSets/*` pattern. |
| `platforms` | `array` | The list of platforms on which to filter; may be empty. The filters represented by multiple platforms are ORed together (for example, if non-empty, results must match any one of the platforms). |
| `sellerNetworkIds` | `array` | For Authorized Buyers only. The list of IDs of the seller (publisher) networks on which to filter; may be empty. The filters represented by multiple seller network IDs are ORed together (for example, if non-empty, results must match any one of the publisher networks). See [seller-network-ids](https://developers.google.com/authorized-buyers/rtb/downloads/seller-network-ids) file for the set of existing seller network IDs. |
| `timeSeriesGranularity` | `string` | The granularity of time intervals if a time series breakdown is preferred; optional. |
| `environment` | `string` | The environment on which to filter; optional. |
| `publisherIdentifiers` | `array` | For Open Bidding partners only. The list of publisher identifiers on which to filter; may be empty. The filters represented by multiple publisher identifiers are ORed together. |
| `creativeId` | `string` | The ID of the creative on which to filter; optional. This field may be set only for a filter set that accesses account-level troubleshooting data, for example, one whose name matches the `bidders/*/accounts/*/filterSets/*` pattern. |
| `relativeDateRange` | `object` | A relative date range, specified by an offset and a duration. The supported range of dates begins 30 days before today and ends today, for example, the limits for these values are: offset_days &gt;= 0 duration_days &gt;= 1 offset_days + duration_days &lt;= 30 |
| `format` | `string` | Creative format bidded on or allowed to bid on, can be empty. |
| `formats` | `array` | Creative formats bidded on or allowed to bid on, can be empty. Although this field is a list, it can only be populated with a single item. A HTTP 400 bad request error will be returned in the response if you specify multiple items. |
| `breakdownDimensions` | `array` | The set of dimensions along which to break down the response; may be empty. If multiple dimensions are requested, the breakdown is along the Cartesian product of the requested dimensions. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_accounts_filterSets_get` | `SELECT` | `accountsId, biddersId, filterSetsId` | Retrieves the requested filter set for the account with the given account ID. |
| `bidders_accounts_filterSets_list` | `SELECT` | `accountsId, biddersId` | Lists all filter sets for the account with the given account ID. |
| `bidders_filterSets_get` | `SELECT` | `biddersId, filterSetsId` | Retrieves the requested filter set for the account with the given account ID. |
| `bidders_filterSets_list` | `SELECT` | `biddersId` | Lists all filter sets for the account with the given account ID. |
| `bidders_accounts_filterSets_create` | `INSERT` | `accountsId, biddersId` | Creates the specified filter set for the account with the given account ID. |
| `bidders_filterSets_create` | `INSERT` | `biddersId` | Creates the specified filter set for the account with the given account ID. |
| `bidders_accounts_filterSets_delete` | `DELETE` | `accountsId, biddersId, filterSetsId` | Deletes the requested filter set from the account with the given account ID. |
| `bidders_filterSets_delete` | `DELETE` | `biddersId, filterSetsId` | Deletes the requested filter set from the account with the given account ID. |
