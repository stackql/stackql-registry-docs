---
title: locations__voice_of_merchant_state
hide_title: false
hide_table_of_contents: false
keywords:
  - locations__voice_of_merchant_state
  - mybusinessverifications
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations__voice_of_merchant_state</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessverifications.locations__voice_of_merchant_state</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `verify` | `object` | Indicates that the location requires verification. Contains information about the current verification actions performed on the location. |
| `waitForVoiceOfMerchant` | `object` | Indicates that the location will gain voice of merchant after passing review. |
| `complyWithGuidelines` | `object` | Indicates that the location fails to comply with our [guidelines](https://support.google.com/business/answer/3038177). |
| `hasBusinessAuthority` | `boolean` | Indicates whether the location has the authority (ownership) over the business on Google. If true, another location cannot take over and become the dominant listing on Maps. However, edits will not become live unless Voice of Merchant is gained (i.e. has_voice_of_merchant is true). |
| `hasVoiceOfMerchant` | `boolean` | Indicates whether the location is in good standing and has control over the business on Google. Any edits made to the location will propagate to Maps after passing the review phase. |
| `resolveOwnershipConflict` | `object` | Indicates that the location duplicates another location that is in good standing. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `locations_getVoiceOfMerchantState` | `SELECT` | `locationsId` |
