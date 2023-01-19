---
title: locations_businesscallssettings
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_businesscallssettings
  - mybusinessbusinesscalls
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
<tr><td><b>Name</b></td><td><code>locations_businesscallssettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessbusinesscalls.locations_businesscallssettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the calls settings. Format: locations/&#123;location&#125;/businesscallssettings |
| `callsState` | `string` | Required. The state of this location's enrollment in Business calls. |
| `consentTime` | `string` | Input only. Time when the end user provided consent to the API user to enable business calls. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `locations_getBusinesscallssettings` | `SELECT` | `locationsId` |
