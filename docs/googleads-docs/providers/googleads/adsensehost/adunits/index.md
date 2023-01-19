---
title: adunits
hide_title: false
hide_table_of_contents: false
keywords:
  - adunits
  - adsensehost
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
<tr><td><b>Name</b></td><td><code>adunits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsensehost.adunits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of this ad unit. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format. |
| `name` | `string` | Name of this ad unit. |
| `contentAdsSettings` | `object` | Settings specific to content ads (AFC) and highend mobile content ads (AFMC - deprecated). |
| `customStyle` | `object` |  |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#adUnit. |
| `mobileContentAdsSettings` | `object` | Settings specific to WAP mobile content ads (AFMC - deprecated). |
| `status` | `string` | Status of this ad unit. Possible values are:<br />NEW: Indicates that the ad unit was created within the last seven days and does not yet have any activity associated with it.<br /><br />ACTIVE: Indicates that there has been activity on this ad unit in the last seven days.<br /><br />INACTIVE: Indicates that there has been no activity on this ad unit in the last seven days. |
| `code` | `string` | Identity code of this ad unit, not necessarily unique across ad clients. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_adunits_get` | `SELECT` | `accountId, adClientId, adUnitId` | Get the specified host ad unit in this AdSense account. |
| `accounts_adunits_list` | `SELECT` | `accountId, adClientId` | List all ad units in the specified publisher's AdSense account. |
| `accounts_adunits_delete` | `DELETE` | `accountId, adClientId, adUnitId` | Delete the specified ad unit from the specified publisher AdSense account. |
| `accounts_adunits_insert` | `EXEC` | `accountId, adClientId` | Insert the supplied ad unit into the specified publisher AdSense account. |
| `accounts_adunits_patch` | `EXEC` | `accountId, adClientId, adUnitId` | Update the supplied ad unit in the specified publisher AdSense account. This method supports patch semantics. |
| `accounts_adunits_update` | `EXEC` | `accountId, adClientId` | Update the supplied ad unit in the specified publisher AdSense account. |
