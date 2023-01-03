---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
  - compute
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
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `specificReservationRequired` | `boolean` | Indicates whether the reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from this reservation. |
| `zone` | `string` | Zone in which the reservation resides. A zone must be provided if the reservation is created within a commitment. |
| `commitment` | `string` | [Output Only] Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment. |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `specificReservation` | `object` | This reservation type allows to pre allocate specific instance configuration. Next ID: 6 |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#reservations for reservations. |
| `status` | `string` | [Output Only] The status of the reservation. |
| `selfLink` | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| `shareSettings` | `object` | The share setting for reservations and sole tenancy node groups. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of reservations. |
| `get` | `SELECT` | `project, reservation, zone` | Retrieves information about the specified reservation. |
| `list` | `SELECT` | `project, zone` | A list of all the reservations that have been configured for the specified project in specified zone. |
| `insert` | `INSERT` | `project, zone` | Creates a new reservation. For more information, read Reserving zonal resources. |
| `delete` | `DELETE` | `project, reservation, zone` | Deletes the specified reservation. |
| `resize` | `EXEC` | `project, reservation, zone` | Resizes the reservation (applicable to standalone reservations only). For more information, read Modifying reservations. |
| `update` | `EXEC` | `project, reservation, zone` | Update share settings of the reservation. |
