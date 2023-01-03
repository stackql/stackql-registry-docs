---
title: locations_bi_reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_bi_reservation
  - bigqueryreservation
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_bi_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryreservation.locations_bi_reservation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the singleton BI reservation. Reservation names have the form `projects/{project_id}/locations/{location_id}/biReservation`. |
| `size` | `string` | Size of a reservation, in bytes. |
| `updateTime` | `string` | Output only. The last update timestamp of a reservation. |
| `preferredTables` | `array` | Preferred tables to use BI capacity for. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_getBiReservation` | `SELECT` | `locationsId, projectsId` |
