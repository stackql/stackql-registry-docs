---
title: publisher_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - publisher_profiles
  - authorizedbuyersmarketplace
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>publisher_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.authorizedbuyersmarketplace.publisher_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the publisher profile. Format: `buyers/&#123;buyer&#125;/publisherProfiles/&#123;publisher_profile&#125;` |
| `displayName` | `string` | Display name of the publisher profile. Can be used to filter the response of the publisherProfiles.list method. |
| `isParent` | `boolean` | Indicates if this profile is the parent profile of the seller. A parent profile represents all the inventory from the seller, as opposed to child profile that is created to brand a portion of inventory. One seller has only one parent publisher profile, and can have multiple child profiles. See https://support.google.com/admanager/answer/6035806 for details. Can be used to filter the response of the publisherProfiles.list method by setting the filter to "is_parent: true". |
| `domains` | `array` | The list of domains represented in this publisher profile. Empty if this is a parent profile. These are top private domains, meaning that these will not contain a string like "photos.google.co.uk/123", but will instead contain "google.co.uk". Can be used to filter the response of the publisherProfiles.list method. |
| `audienceDescription` | `string` | Description on the publisher's audience. |
| `samplePageUrl` | `string` | URL to a sample content page. |
| `pitchStatement` | `string` | Statement explaining what's unique about publisher's business, and why buyers should partner with the publisher. |
| `topHeadlines` | `array` | Up to three key metrics and rankings. For example, "#1 Mobile News Site for 20 Straight Months". |
| `mediaKitUrl` | `string` | URL to additional marketing and sales materials. |
| `publisherCode` | `string` | A unique identifying code for the seller. This value is the same for all of the seller's parent and child publisher profiles. Can be used to filter the response of the publisherProfiles.list method. |
| `logoUrl` | `string` | A Google public URL to the logo for this publisher profile. The logo is stored as a PNG, JPG, or GIF image. |
| `overview` | `string` | Overview of the publisher. |
| `directDealsContact` | `string` | Contact information for direct reservation deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |
| `programmaticDealsContact` | `string` | Contact information for programmatic deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |
| `mobileApps` | `array` | The list of apps represented in this publisher profile. Empty if this is a parent profile. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `buyers_publisherProfiles_get` | `SELECT` | `buyersId, publisherProfilesId` | Gets the requested publisher profile by name. |
| `buyers_publisherProfiles_list` | `SELECT` | `buyersId` | Lists publisher profiles. The returned publisher profiles aren't in any defined order. The order of the results might change. A new publisher profile can appear in any place in the list of returned results. |
