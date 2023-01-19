---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | View (Profile) ID. |
| `name` | `string` | Name of this view (profile). |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this view (profile) belongs. |
| `currency` | `string` | The currency type associated with this view (profile), defaults to USD. The supported values are:<br />USD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD, HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL, ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD, SAR, SGD, VEF, LVL |
| `created` | `string` | Time this view (profile) was created. |
| `starred` | `boolean` | Indicates whether this view (profile) is starred or not. |
| `webPropertyId` | `string` | Web property ID of the form UA-XXXXX-YY to which this view (profile) belongs. |
| `selfLink` | `string` | Link for this view (profile). |
| `defaultPage` | `string` | Default page for this view (profile). |
| `botFilteringEnabled` | `boolean` | Indicates whether bot filtering is enabled for this view (profile). |
| `siteSearchCategoryParameters` | `string` | Site search category parameters for this view (profile). |
| `timezone` | `string` | Time zone for which this view (profile) has been configured. Time zones are identified by strings from the TZ database. |
| `updated` | `string` | Time this view (profile) was last modified. |
| `enhancedECommerceTracking` | `boolean` | Indicates whether enhanced ecommerce tracking is enabled for this view (profile). This property can only be enabled if ecommerce tracking is enabled. |
| `childLink` | `object` | Child link for this view (profile). Points to the list of goals for this view (profile). |
| `stripSiteSearchCategoryParameters` | `boolean` | Whether or not Analytics will strip search category parameters from the URLs in your reports. |
| `websiteUrl` | `string` | Website URL for this view (profile). |
| `accountId` | `string` | Account ID to which this view (profile) belongs. |
| `type` | `string` | View (Profile) type. Supported types: WEB or APP. |
| `excludeQueryParameters` | `string` | The query parameters that are excluded from this view (profile). |
| `permissions` | `object` | Permissions the user has for this view (profile). |
| `eCommerceTracking` | `boolean` | Indicates whether ecommerce tracking is enabled for this view (profile). |
| `parentLink` | `object` | Parent link for this view (profile). Points to the web property to which this view (profile) belongs. |
| `stripSiteSearchQueryParameters` | `boolean` | Whether or not Analytics will strip search query parameters from the URLs in your reports. |
| `siteSearchQueryParameters` | `string` | The site search query parameters for this view (profile). |
| `kind` | `string` | Resource type for Analytics view (profile). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_profiles_get` | `SELECT` | `accountId, profileId, webPropertyId` | Gets a view (profile) to which the user has access. |
| `management_profiles_list` | `SELECT` | `accountId, webPropertyId` | Lists views (profiles) to which the user has access. |
| `management_profiles_delete` | `DELETE` | `accountId, profileId, webPropertyId` | Deletes a view (profile). |
| `management_profiles_insert` | `EXEC` | `accountId, webPropertyId` | Create a new view (profile). |
| `management_profiles_patch` | `EXEC` | `accountId, profileId, webPropertyId` | Updates an existing view (profile). This method supports patch semantics. |
| `management_profiles_update` | `EXEC` | `accountId, profileId, webPropertyId` | Updates an existing view (profile). |
