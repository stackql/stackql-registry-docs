---
title: lodging_google_updated
hide_title: false
hide_table_of_contents: false
keywords:
  - lodging_google_updated
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
<tr><td><b>Name</b></td><td><code>lodging_google_updated</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinesslodging.lodging_google_updated</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `diffMask` | `string` | Required. The fields in the Lodging that have been updated by Google. Repeated field items are not individually specified. |
| `lodging` | `object` | Lodging of a location that provides accomodations. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `locations_lodging_getGoogleUpdated` | `SELECT` | `locationsId` |
