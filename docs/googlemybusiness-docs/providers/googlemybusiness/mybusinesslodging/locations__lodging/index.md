---
title: locations__lodging
hide_title: false
hide_table_of_contents: false
keywords:
  - locations__lodging
  - mybusinesslodging
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
<tr><td><b>Name</b></td><td><code>locations__lodging</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinesslodging.locations__lodging</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Google identifier for this location in the form: `locations/&#123;location_id&#125;/lodging` |
| `someUnits` | `object` | Features and available amenities in the guest unit. |
| `foodAndDrink` | `object` | Meals, snacks, and beverages available at the property. |
| `services` | `object` | Conveniences or help provided by the property to facilitate an easier, more comfortable stay. |
| `housekeeping` | `object` | Conveniences provided in guest units to facilitate an easier, more comfortable stay. |
| `connectivity` | `object` | The ways in which the property provides guests with the ability to access the internet. |
| `activities` | `object` | Amenities and features related to leisure and play. |
| `transportation` | `object` | Vehicles or vehicular services facilitated or owned by the property. |
| `guestUnits` | `array` | Individual GuestUnitTypes that are available in this Lodging. |
| `property` | `object` | General factual information about the property's physical structure and important dates. |
| `sustainability` | `object` | Sustainability practices implemented at the hotel. |
| `accessibility` | `object` | Physical adaptations made to the property in consideration of varying levels of human physical ability. |
| `allUnits` | `object` | Features and available amenities in the guest unit. |
| `healthAndSafety` | `object` | Health and safety measures implemented by the hotel during COVID-19. |
| `wellness` | `object` | Guest facilities at the property to promote or maintain health, beauty, and fitness. |
| `families` | `object` | Services and amenities for families and young guests. |
| `policies` | `object` | Property rules that impact guests. |
| `commonLivingArea` | `object` | An individual room, such as kitchen, bathroom, bedroom, within a bookable guest unit. |
| `pools` | `object` | Swimming pool or recreational water facilities available at the hotel. |
| `parking` | `object` | Parking options at the property. |
| `pets` | `object` | Policies regarding guest-owned animals. |
| `metadata` | `object` | Metadata for the Lodging. |
| `business` | `object` | Features of the property of specific interest to the business traveler. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `locations_getLodging` | `SELECT` | `locationsId` |
