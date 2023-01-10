---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - mybusinessbusinessinformation
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessbusinessinformation.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Google identifier for this location in the form: `locations/&#123;location_id&#125;`. |
| `storefrontAddress` | `object` | Represents a postal address, e.g. for postal delivery or payments addresses. Given a postal address, a postal service can deliver items to a premise, P.O. Box or similar. It is not intended to model geographical locations (roads, towns, mountains). In typical usage an address would be created via user input or from importing existing data, depending on the type of process. Advice on address input / editing: - Use an internationalization-ready address widget such as https://github.com/google/libaddressinput) - Users should not be presented with UI elements for input or editing of fields outside countries where that field is used. For more guidance on how to use this schema, please see: https://support.google.com/business/answer/6397478 |
| `phoneNumbers` | `object` | A collection of phone numbers for the business. During updates, both fields must be set. Clients may not update just the primary or additional phone numbers using the update mask. International phone format is preferred, such as "+1 415 555 0132", see more in (https://developers.google.com/style/phone-numbers#international-phone-numbers). |
| `openInfo` | `object` | Information related to the opening state of the business. |
| `metadata` | `object` | Additional non-user-editable information about the location. |
| `websiteUri` | `string` | Optional. A URL for this business. If possible, use a URL that represents this individual business location instead of a generic website/URL that represents all locations, or the brand. |
| `profile` | `object` | All information pertaining to the location's profile. |
| `labels` | `array` | Optional. A collection of free-form strings to allow you to tag your business. These labels are NOT user facing; only you can see them. Must be between 1-255 characters per label. |
| `regularHours` | `object` | Represents the time periods that this location is open for business. Holds a collection of TimePeriod instances. |
| `serviceItems` | `array` | Optional. List of services supported by merchants. A service can be haircut, install water heater, etc. Duplicated service items will be removed automatically. |
| `title` | `string` | Required. Location name should reflect your business's real-world name, as used consistently on your storefront, website, and stationery, and as known to customers. Any additional information, when relevant, can be included in other fields of the resource (for example, `Address`, `Categories`). Don't add unnecessary information to your name (for example, prefer "Google" over "Google Inc. - Mountain View Corporate Headquarters"). Don't include marketing taglines, store codes, special characters, hours or closed/open status, phone numbers, website URLs, service/product information, location/address or directions, or containment information (for example, "Chase ATM in Duane Reade"). |
| `serviceArea` | `object` | Service area businesses provide their service at the customer's location (for example, a locksmith or plumber). |
| `languageCode` | `string` | Immutable. The language of the location. Set during creation and not updateable. |
| `storeCode` | `string` | Optional. External identifier for this location, which must be unique within a given account. This is a means of associating the location with your own records. |
| `latlng` | `object` | An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges. |
| `specialHours` | `object` | Represents a set of time periods when a location's operational hours differ from its normal business hours. |
| `relationshipData` | `object` | Information of all parent and children locations related to this one. |
| `moreHours` | `array` | Optional. More hours for a business's different departments or specific customers. |
| `categories` | `object` | A collection of categories that describes the business. During updates, both fields must be set. Clients are prohibited from individually updating the primary or additional categories using the update mask. |
| `adWordsLocationExtensions` | `object` | Additional information that is surfaced in AdWords. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_locations_list` | `SELECT` | `accountsId` | Lists the locations for the specified account. |
| `get` | `SELECT` | `locationsId` | Returns the specified location. |
| `accounts_locations_create` | `INSERT` | `accountsId` | Creates a new Location that will be owned by the logged in user. |
| `delete` | `DELETE` | `locationsId` | Deletes a location. If this location cannot be deleted using the API and it is marked so in the `google.mybusiness.businessinformation.v1.LocationState`, use the [Google Business Profile](https://business.google.com/manage/) website. |
| `associate` | `EXEC` | `locationsId` | Associates a location to a place ID. Any previous association is overwritten. This operation is only valid if the location is unverified. The association must be valid, that is, it appears in the list of `SearchGoogleLocations`. |
| `clearLocationAssociation` | `EXEC` | `locationsId` | Clears an association between a location and its place ID. This operation is only valid if the location is unverified. |
| `patch` | `EXEC` | `locationsId` | Updates the specified location. |
| `updateAttributes` | `EXEC` | `locationsId` | Update attributes for a given location. |
