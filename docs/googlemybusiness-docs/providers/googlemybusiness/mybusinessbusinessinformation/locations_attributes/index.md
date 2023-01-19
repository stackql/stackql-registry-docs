---
title: locations_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_attributes
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
<tr><td><b>Name</b></td><td><code>locations_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessbusinessinformation.locations_attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Google identifier for this location in the form of `locations/&#123;location_id&#125;/attributes`. |
| `attributes` | `array` | A collection of attributes that need to be updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `locations_getAttributes` | `SELECT` | `locationsId` |
