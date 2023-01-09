---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - androidmanagement
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidmanagement.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the app in the form enterprises/&#123;enterprise&#125;/applications/&#123;package_name&#125;. |
| `description` | `string` | The localized promotional description, if available. |
| `smallIconUrl` | `string` | A link to a smaller image that can be used as an icon for the app. This image is suitable for use up to a pixel size of 128 x 128. |
| `recentChanges` | `string` | A localised description of the recent changes made to the app. |
| `appVersions` | `array` | Versions currently available for this app. |
| `title` | `string` | The title of the app. Localized. |
| `minAndroidSdkVersion` | `integer` | The minimum Android SDK necessary to run the app. |
| `appPricing` | `string` | Whether this app is free, free with in-app purchases, or paid. If the pricing is unspecified, this means the app is not generally available anymore (even though it might still be available to people who own it). |
| `screenshotUrls` | `array` | A list of screenshot links representing the app. |
| `updateTime` | `string` | Output only. The approximate time (within 7 days) the app was last published. |
| `permissions` | `array` | The permissions required by the app. |
| `playStoreUrl` | `string` | A link to the (consumer) Google Play details page for the app. |
| `appTracks` | `array` | Application tracks visible to the enterprise. |
| `availableCountries` | `array` | The countries which this app is available in as per ISO 3166-1 alpha-2. |
| `fullDescription` | `string` | Full app description, if available. |
| `contentRating` | `string` | The content rating for this app. |
| `features` | `array` | Noteworthy features (if any) of this app. |
| `distributionChannel` | `string` | How and to whom the package is made available. |
| `author` | `string` | The name of the author of the apps (for example, the app developer). |
| `iconUrl` | `string` | A link to an image that can be used as an icon for the app. This image is suitable for use up to a pixel size of 512 x 512. |
| `managedProperties` | `array` | The set of managed properties available to be pre-configured for the app. |
| `category` | `string` | The app category (e.g. RACING, SOCIAL, etc.) |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `enterprises_applications_get` | `SELECT` | `applicationsId, enterprisesId` |
