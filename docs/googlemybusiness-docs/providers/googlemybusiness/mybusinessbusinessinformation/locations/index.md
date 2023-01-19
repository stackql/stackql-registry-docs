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
| `locations` | `array` | The locations. |
| `nextPageToken` | `string` | If the number of locations exceeded the requested page size, this field is populated with a token to fetch the next page of locations on a subsequent call to `ListLocations`. If there are no more locations, this field is not present in the response. |
| `totalSize` | `integer` | The approximate number of Locations in the list irrespective of pagination. |
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
