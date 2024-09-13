---
title: data_layers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_layers
  - solar
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

Creates, updates, deletes, gets or lists a <code>data_layers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_layers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.solar.data_layers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annualFluxUrl" /> | `string` | The URL for the annual flux map (annual sunlight on roofs) of the region. Values are kWh/kW/year. This is *unmasked flux*: flux is computed for every location, not just building rooftops. Invalid locations are stored as -9999: locations outside our coverage area will be invalid, and a few locations inside the coverage area, where we were unable to calculate flux, will also be invalid. |
| <CopyableCode code="dsmUrl" /> | `string` | The URL for an image of the DSM (Digital Surface Model) of the region. Values are in meters above EGM96 geoid (i.e., sea level). Invalid locations (where we don't have data) are stored as -9999. |
| <CopyableCode code="hourlyShadeUrls" /> | `array` | Twelve URLs for hourly shade, corresponding to January...December, in order. Each GeoTIFF will contain 24 bands, corresponding to the 24 hours of the day. Each pixel is a 32 bit integer, corresponding to the (up to) 31 days of that month; a 1 bit means that the corresponding location is able to see the sun at that day, of that hour, of that month. Invalid locations are stored as -9999 (since this is negative, it has bit 31 set, and no valid value could have bit 31 set as that would correspond to the 32nd day of the month). An example may be useful. If you want to know whether a point (at pixel location (x, y)) saw sun at 4pm on the 22nd of June you would: 1. fetch the sixth URL in this list (corresponding to June). 1. look up the 17th channel (corresponding to 4pm). 1. read the 32-bit value at (x, y). 1. read bit 21 of the value (corresponding to the 22nd of the month). 1. if that bit is a 1, then that spot saw the sun at 4pm 22 June. More formally: Given `month` (1-12), `day` (1...month max; February has 28 days) and `hour` (0-23), the shade/sun for that month/day/hour at a position `(x, y)` is the bit ``` (hourly_shade[month - 1])(x, y)[hour] & (1 << (day - 1)) ``` where `(x, y)` is spatial indexing, `[month - 1]` refers to fetching the `month - 1`st URL (indexing from zero), `[hour]` is indexing into the channels, and a final non-zero result means "sunny". There are no leap days, and DST doesn't exist (all days are 24 hours long; noon is always "standard time" noon). |
| <CopyableCode code="imageryDate" /> | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp |
| <CopyableCode code="imageryProcessedDate" /> | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp |
| <CopyableCode code="imageryQuality" /> | `string` | The quality of the result's imagery. |
| <CopyableCode code="maskUrl" /> | `string` | The URL for the building mask image: one bit per pixel saying whether that pixel is considered to be part of a rooftop or not. |
| <CopyableCode code="monthlyFluxUrl" /> | `string` | The URL for the monthly flux map (sunlight on roofs, broken down by month) of the region. Values are kWh/kW/year. The GeoTIFF pointed to by this URL will contain twelve bands, corresponding to January...December, in order. |
| <CopyableCode code="rgbUrl" /> | `string` | The URL for an image of RGB data (aerial photo) of the region. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Gets solar information for a region surrounding a location. Returns an error with code `NOT_FOUND` if the location is outside the coverage area. |

## `SELECT` examples

Gets solar information for a region surrounding a location. Returns an error with code `NOT_FOUND` if the location is outside the coverage area.

```sql
SELECT
annualFluxUrl,
dsmUrl,
hourlyShadeUrls,
imageryDate,
imageryProcessedDate,
imageryQuality,
maskUrl,
monthlyFluxUrl,
rgbUrl
FROM google.solar.data_layers
WHERE  = '{{  }}'; 
```
