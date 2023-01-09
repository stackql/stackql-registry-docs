---
title: publisher_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - publisher_profiles
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
<tr><td><b>Name</b></td><td><code>publisher_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.publisher_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `audienceDescription` | `string` | Description on the publisher's audience. |
| `topHeadlines` | `array` | Up to three key metrics and rankings. Max 100 characters each. For example "#1 Mobile News Site for 20 Straight Months". |
| `isParent` | `boolean` | Indicates if this profile is the parent profile of the seller. A parent profile represents all the inventory from the seller, as opposed to child profile that is created to brand a portion of inventory. One seller should have only one parent publisher profile, and can have multiple child profiles. Publisher profiles for the same seller will have same value of field google.ads.adexchange.buyer.v2beta1.PublisherProfile.seller. See https://support.google.com/admanager/answer/6035806 for details. |
| `directDealsContact` | `string` | Contact information for direct reservation deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |
| `overview` | `string` | Overview of the publisher. |
| `programmaticDealsContact` | `string` | Contact information for programmatic deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |
| `domains` | `array` | The list of domains represented in this publisher profile. Empty if this is a parent profile. These are top private domains, meaning that these will not contain a string like "photos.google.co.uk/123", but will instead contain "google.co.uk". |
| `mediaKitUrl` | `string` | URL to additional marketing and sales materials. |
| `logoUrl` | `string` | A Google public URL to the logo for this publisher profile. The logo is stored as a PNG, JPG, or GIF image. |
| `samplePageUrl` | `string` | URL to a sample content page. |
| `displayName` | `string` | Name of the publisher profile. |
| `seller` | `object` | Represents a seller of inventory. Each seller is identified by a unique Ad Manager account ID. |
| `mobileApps` | `array` | The list of apps represented in this publisher profile. Empty if this is a parent profile. |
| `publisherProfileId` | `string` | Unique ID for publisher profile. |
| `googlePlusUrl` | `string` | URL to publisher's Google+ page. |
| `rateCardInfoUrl` | `string` | URL to a publisher rate card. |
| `buyerPitchStatement` | `string` | Statement explaining what's unique about publisher's business, and why buyers should partner with the publisher. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_publisherProfiles_get` | `SELECT` | `accountId, publisherProfileId` | Gets the requested publisher profile by id. |
| `accounts_publisherProfiles_list` | `SELECT` | `accountId` | List all publisher profiles visible to the buyer |
