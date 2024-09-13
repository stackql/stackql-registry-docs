
---
title: places
hide_title: false
hide_table_of_contents: false
keywords:
  - places
  - places
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>place</code> resource or lists <code>places</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>places</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.places.places" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of a place. |
| <CopyableCode code="name" /> | `string` | This Place's resource name, in `places/{place_id}` format. Can be used to look up the Place. |
| <CopyableCode code="accessibilityOptions" /> | `object` | Information about the accessibility options a place offers. |
| <CopyableCode code="addressComponents" /> | `array` | Repeated components for each locality level. Note the following facts about the address_components[] array: - The array of address components may contain more components than the formatted_address. - The array does not necessarily include all the political entities that contain an address, apart from those included in the formatted_address. To retrieve all the political entities that contain a specific address, you should use reverse geocoding, passing the latitude/longitude of the address as a parameter to the request. - The format of the response is not guaranteed to remain the same between requests. In particular, the number of address_components varies based on the address requested and can change over time for the same address. A component can change position in the array. The type of the component can change. A particular component may be missing in a later response. |
| <CopyableCode code="adrFormatAddress" /> | `string` | The place's address in adr microformat: http://microformats.org/wiki/adr. |
| <CopyableCode code="allowsDogs" /> | `boolean` | Place allows dogs. |
| <CopyableCode code="areaSummary" /> | `object` | Experimental: See https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative for more details. AI-generated summary of the area that the place is in. |
| <CopyableCode code="attributions" /> | `array` | A set of data provider that must be shown with this result. |
| <CopyableCode code="businessStatus" /> | `string` | The business status for the place. |
| <CopyableCode code="curbsidePickup" /> | `boolean` | Specifies if the business supports curbside pickup. |
| <CopyableCode code="currentOpeningHours" /> | `object` | Information about business hour of the place. |
| <CopyableCode code="currentSecondaryOpeningHours" /> | `array` | Contains an array of entries for the next seven days including information about secondary hours of a business. Secondary hours are different from a business's main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place. This field includes the special_days subfield of all hours, set for dates that have exceptional hours. |
| <CopyableCode code="delivery" /> | `boolean` | Specifies if the business supports delivery. |
| <CopyableCode code="dineIn" /> | `boolean` | Specifies if the business supports indoor or outdoor seating options. |
| <CopyableCode code="displayName" /> | `object` | Localized variant of a text in a particular language. |
| <CopyableCode code="editorialSummary" /> | `object` | Localized variant of a text in a particular language. |
| <CopyableCode code="evChargeOptions" /> | `object` | Information about the EV Charge Station hosted in Place. Terminology follows https://afdc.energy.gov/fuels/electricity_infrastructure.html One port could charge one car at a time. One port has one or more connectors. One station has one or more ports. |
| <CopyableCode code="formattedAddress" /> | `string` | A full, human-readable address for this place. |
| <CopyableCode code="fuelOptions" /> | `object` | The most recent information about fuel options in a gas station. This information is updated regularly. |
| <CopyableCode code="generativeSummary" /> | `object` | Experimental: See https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative for more details. AI-generated summary of the place. |
| <CopyableCode code="goodForChildren" /> | `boolean` | Place is good for children. |
| <CopyableCode code="goodForGroups" /> | `boolean` | Place accommodates groups. |
| <CopyableCode code="goodForWatchingSports" /> | `boolean` | Place is suitable for watching sports. |
| <CopyableCode code="googleMapsUri" /> | `string` | A URL providing more information about this place. |
| <CopyableCode code="iconBackgroundColor" /> | `string` | Background color for icon_mask in hex format, e.g. #909CE1. |
| <CopyableCode code="iconMaskBaseUri" /> | `string` | A truncated URL to an icon mask. User can access different icon type by appending type suffix to the end (eg, ".svg" or ".png"). |
| <CopyableCode code="internationalPhoneNumber" /> | `string` | A human-readable phone number for the place, in international format. |
| <CopyableCode code="liveMusic" /> | `boolean` | Place provides live music. |
| <CopyableCode code="location" /> | `object` | An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges. |
| <CopyableCode code="menuForChildren" /> | `boolean` | Place has a children's menu. |
| <CopyableCode code="nationalPhoneNumber" /> | `string` | A human-readable phone number for the place, in national format. |
| <CopyableCode code="outdoorSeating" /> | `boolean` | Place provides outdoor seating. |
| <CopyableCode code="parkingOptions" /> | `object` | Information about parking options for the place. A parking lot could support more than one option at the same time. |
| <CopyableCode code="paymentOptions" /> | `object` | Payment options the place accepts. |
| <CopyableCode code="photos" /> | `array` | Information (including references) about photos of this place. A maximum of 10 photos can be returned. |
| <CopyableCode code="plusCode" /> | `object` | Plus code (http://plus.codes) is a location reference with two formats: global code defining a 14mx14m (1/8000th of a degree) or smaller rectangle, and compound code, replacing the prefix with a reference location. |
| <CopyableCode code="priceLevel" /> | `string` | Price level of the place. |
| <CopyableCode code="primaryType" /> | `string` | The primary type of the given result. This type must one of the Places API supported types. For example, "restaurant", "cafe", "airport", etc. A place can only have a single primary type. For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types |
| <CopyableCode code="primaryTypeDisplayName" /> | `object` | Localized variant of a text in a particular language. |
| <CopyableCode code="rating" /> | `number` | A rating between 1.0 and 5.0, based on user reviews of this place. |
| <CopyableCode code="regularOpeningHours" /> | `object` | Information about business hour of the place. |
| <CopyableCode code="regularSecondaryOpeningHours" /> | `array` | Contains an array of entries for information about regular secondary hours of a business. Secondary hours are different from a business's main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place. |
| <CopyableCode code="reservable" /> | `boolean` | Specifies if the place supports reservations. |
| <CopyableCode code="restroom" /> | `boolean` | Place has restroom. |
| <CopyableCode code="reviews" /> | `array` | List of reviews about this place, sorted by relevance. A maximum of 5 reviews can be returned. |
| <CopyableCode code="servesBeer" /> | `boolean` | Specifies if the place serves beer. |
| <CopyableCode code="servesBreakfast" /> | `boolean` | Specifies if the place serves breakfast. |
| <CopyableCode code="servesBrunch" /> | `boolean` | Specifies if the place serves brunch. |
| <CopyableCode code="servesCocktails" /> | `boolean` | Place serves cocktails. |
| <CopyableCode code="servesCoffee" /> | `boolean` | Place serves coffee. |
| <CopyableCode code="servesDessert" /> | `boolean` | Place serves dessert. |
| <CopyableCode code="servesDinner" /> | `boolean` | Specifies if the place serves dinner. |
| <CopyableCode code="servesLunch" /> | `boolean` | Specifies if the place serves lunch. |
| <CopyableCode code="servesVegetarianFood" /> | `boolean` | Specifies if the place serves vegetarian food. |
| <CopyableCode code="servesWine" /> | `boolean` | Specifies if the place serves wine. |
| <CopyableCode code="shortFormattedAddress" /> | `string` | A short, human-readable address for this place. |
| <CopyableCode code="subDestinations" /> | `array` | A list of sub destinations related to the place. |
| <CopyableCode code="takeout" /> | `boolean` | Specifies if the business supports takeout. |
| <CopyableCode code="types" /> | `array` | A set of type tags for this result. For example, "political" and "locality". For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types |
| <CopyableCode code="userRatingCount" /> | `integer` | The total number of reviews (with or without text) for this place. |
| <CopyableCode code="utcOffsetMinutes" /> | `integer` | Number of minutes this place's timezone is currently offset from UTC. This is expressed in minutes to support timezones that are offset by fractions of an hour, e.g. X hours and 15 minutes. |
| <CopyableCode code="viewport" /> | `object` | A latitude-longitude viewport, represented as two diagonally opposite `low` and `high` points. A viewport is considered a closed region, i.e. it includes its boundary. The latitude bounds must range between -90 to 90 degrees inclusive, and the longitude bounds must range between -180 to 180 degrees inclusive. Various cases include: - If `low` = `high`, the viewport consists of that single point. - If `low.longitude` > `high.longitude`, the longitude range is inverted (the viewport crosses the 180 degree longitude line). - If `low.longitude` = -180 degrees and `high.longitude` = 180 degrees, the viewport includes all longitudes. - If `low.longitude` = 180 degrees and `high.longitude` = -180 degrees, the longitude range is empty. - If `low.latitude` > `high.latitude`, the latitude range is empty. Both `low` and `high` must be populated, and the represented box cannot be empty (as specified by the definitions above). An empty viewport will result in an error. For example, this viewport fully encloses New York City: { "low": { "latitude": 40.477398, "longitude": -74.259087 }, "high": { "latitude": 40.91618, "longitude": -73.70018 } } |
| <CopyableCode code="websiteUri" /> | `string` | The authoritative website for this place, e.g. a business' homepage. Note that for places that are part of a chain (e.g. an IKEA store), this will usually be the website for the individual store, not the overall chain. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="placesId" /> | Get the details of a place based on its resource name, which is a string in the `places/{place_id}` format. |
| <CopyableCode code="autocomplete" /> | `EXEC` | <CopyableCode code="" /> | Returns predictions for the given input. |
| <CopyableCode code="search_nearby" /> | `EXEC` | <CopyableCode code="" /> | Search for places near locations. |
| <CopyableCode code="search_text" /> | `EXEC` | <CopyableCode code="" /> | Text query based place search. |

## `SELECT` examples

Get the details of a place based on its resource name, which is a string in the `places/{place_id}` format.

```sql
SELECT
id,
name,
accessibilityOptions,
addressComponents,
adrFormatAddress,
allowsDogs,
areaSummary,
attributions,
businessStatus,
curbsidePickup,
currentOpeningHours,
currentSecondaryOpeningHours,
delivery,
dineIn,
displayName,
editorialSummary,
evChargeOptions,
formattedAddress,
fuelOptions,
generativeSummary,
goodForChildren,
goodForGroups,
goodForWatchingSports,
googleMapsUri,
iconBackgroundColor,
iconMaskBaseUri,
internationalPhoneNumber,
liveMusic,
location,
menuForChildren,
nationalPhoneNumber,
outdoorSeating,
parkingOptions,
paymentOptions,
photos,
plusCode,
priceLevel,
primaryType,
primaryTypeDisplayName,
rating,
regularOpeningHours,
regularSecondaryOpeningHours,
reservable,
restroom,
reviews,
servesBeer,
servesBreakfast,
servesBrunch,
servesCocktails,
servesCoffee,
servesDessert,
servesDinner,
servesLunch,
servesVegetarianFood,
servesWine,
shortFormattedAddress,
subDestinations,
takeout,
types,
userRatingCount,
utcOffsetMinutes,
viewport,
websiteUri
FROM google.places.places
WHERE placesId = '{{ placesId }}'; 
```
