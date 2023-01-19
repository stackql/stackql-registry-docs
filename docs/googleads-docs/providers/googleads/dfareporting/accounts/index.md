---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this account. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this account. This is a required field, and must be less than 128 characters long and be globally unique. |
| `description` | `string` | Description of this account. |
| `countryId` | `string` | ID of the country associated with this account. |
| `reportsConfiguration` | `object` | Reporting Configuration |
| `defaultCreativeSizeId` | `string` | Default placement dimensions for this account. |
| `maximumImageSize` | `string` | Maximum image size allowed for this account, in kilobytes. Value must be greater than or equal to 1. |
| `teaserSizeLimit` | `string` | File size limit in kilobytes of Rich Media teaser creatives. Acceptable values are 1 to 10240, inclusive. |
| `availablePermissionIds` | `array` | User role permissions available to the user roles of this account. |
| `locale` | `string` | Locale of this account. Acceptable values are: - "cs" (Czech) - "de" (German) - "en" (English) - "en-GB" (English United Kingdom) - "es" (Spanish) - "fr" (French) - "it" (Italian) - "ja" (Japanese) - "ko" (Korean) - "pl" (Polish) - "pt-BR" (Portuguese Brazil) - "ru" (Russian) - "sv" (Swedish) - "tr" (Turkish) - "zh-CN" (Chinese Simplified) - "zh-TW" (Chinese Traditional)  |
| `accountProfile` | `string` | Profile for this account. This is a read-only field that can be left blank. |
| `nielsenOcrEnabled` | `boolean` | Whether campaigns created in this account will be enabled for Nielsen OCR reach ratings by default. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#account". |
| `active` | `boolean` | Whether this account is active. |
| `currencyId` | `string` | ID of currency associated with this account. This is a required field. Acceptable values are: - "1" for USD - "2" for GBP - "3" for ESP - "4" for SEK - "5" for CAD - "6" for JPY - "7" for DEM - "8" for AUD - "9" for FRF - "10" for ITL - "11" for DKK - "12" for NOK - "13" for FIM - "14" for ZAR - "15" for IEP - "16" for NLG - "17" for EUR - "18" for KRW - "19" for TWD - "20" for SGD - "21" for CNY - "22" for HKD - "23" for NZD - "24" for MYR - "25" for BRL - "26" for PTE - "28" for CLP - "29" for TRY - "30" for ARS - "31" for PEN - "32" for ILS - "33" for CHF - "34" for VEF - "35" for COP - "36" for GTQ - "37" for PLN - "39" for INR - "40" for THB - "41" for IDR - "42" for CZK - "43" for RON - "44" for HUF - "45" for RUB - "46" for AED - "47" for BGN - "48" for HRK - "49" for MXN - "50" for NGN - "51" for EGP  |
| `activeViewOptOut` | `boolean` | Whether to serve creatives with Active View tags. If disabled, viewability data will not be available for any impressions. |
| `shareReportsWithTwitter` | `boolean` | Share Path to Conversion reports with Twitter. |
| `activeAdsLimitTier` | `string` | Maximum number of active ads allowed for this account. |
| `accountPermissionIds` | `array` | Account permissions assigned to this account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one account by ID. |
| `list` | `SELECT` | `profileId` | Retrieves the list of accounts, possibly filtered. This method supports paging. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing account. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing account. |
