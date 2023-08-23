---
title: bi_reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - bi_reservation
  - bigqueryreservation
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bi_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryreservation.bi_reservation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the singleton BI reservation. Reservation names have the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/biReservation`. |
| `size` | `string` | Size of a reservation, in bytes. |
| `updateTime` | `string` | Output only. The last update timestamp of a reservation. |
| `preferredTables` | `array` | Preferred tables to use BI capacity for. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_bi_reservation` | `SELECT` | `locationsId, projectsId` | Retrieves a BI reservation. |
| `update_bi_reservation` | `EXEC` | `locationsId, projectsId` | Updates a BI reservation. Only fields specified in the `field_mask` are updated. A singleton BI reservation always exists with default size 0. In order to reserve BI capacity it needs to be updated to an amount greater than 0. In order to release BI capacity reservation size must be set to 0. |
