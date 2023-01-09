---
title: webproperties
hide_title: false
hide_table_of_contents: false
keywords:
  - webproperties
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
<tr><td><b>Name</b></td><td><code>webproperties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.webproperties</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Web property ID of the form UA-XXXXX-YY. |
| `name` | `string` | Name of this web property. |
| `starred` | `boolean` | Indicates whether this web property is starred or not. |
| `permissions` | `object` | Permissions the user has for this web property. |
| `defaultProfileId` | `string` | Default view (profile) ID. |
| `level` | `string` | Level for this web property. Possible values are STANDARD or PREMIUM. |
| `kind` | `string` | Resource type for Analytics WebProperty. |
| `profileCount` | `integer` | View (Profile) count for this web property. |
| `created` | `string` | Time this web property was created. |
| `childLink` | `object` | Child link for this web property. Points to the list of views (profiles) for this web property. |
| `updated` | `string` | Time this web property was last modified. |
| `dataRetentionTtl` | `string` | The length of time for which user and event data is retained.<br />This property cannot be set on insert. |
| `dataRetentionResetOnNewActivity` | `boolean` | Set to true to reset the retention period of the user identifier with each new event from that user (thus setting the expiration date to current time plus retention period).<br />Set to false to delete data associated with the user identifier automatically after the rentention period.<br />This property cannot be set on insert. |
| `selfLink` | `string` | Link for this web property. |
| `industryVertical` | `string` | The industry vertical/category selected for this web property. |
| `parentLink` | `object` | Parent link for this web property. Points to the account to which this web property belongs. |
| `internalWebPropertyId` | `string` | Internal ID for this web property. |
| `websiteUrl` | `string` | Website url for this web property. |
| `accountId` | `string` | Account ID to which this web property belongs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_webproperties_get` | `SELECT` | `accountId, webPropertyId` | Gets a web property to which the user has access. |
| `management_webproperties_list` | `SELECT` | `accountId` | Lists web properties to which the user has access. |
| `management_webproperties_insert` | `EXEC` | `accountId` | Create a new property if the account has fewer than 20 properties. Web properties are visible in the Google Analytics interface only if they have at least one profile. |
| `management_webproperties_patch` | `EXEC` | `accountId, webPropertyId` | Updates an existing web property. This method supports patch semantics. |
| `management_webproperties_update` | `EXEC` | `accountId, webPropertyId` | Updates an existing web property. |
