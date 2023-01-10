---
title: internal_ranges
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_ranges
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>internal_ranges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.internal_ranges</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of a InternalRange. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/internalRanges/&#123;internal_range&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| `description` | `string` | A description of this resource. |
| `peering` | `string` | The type of peering set for this InternalRange. |
| `prefixLength` | `integer` | An alternate to ip_cidr_range. Can be set when trying to create a reservation that automatically finds a free range of the given size. If both ip_cidr_range and prefix_length are set, it's an error if the range sizes don't match. Can also be used during updates to change the range size. |
| `updateTime` | `string` | Time when the InternalRange was updated. |
| `createTime` | `string` | Time when the InternalRange was created. |
| `usage` | `string` | The type of usage set for this InternalRange. |
| `targetCidrRange` | `array` | Optional. Can be set to narrow down or pick a different address space while searching for a free range. If not set, defaults to the "10.0.0.0/8" address space. This can be used to search in other rfc-1918 address spaces like "172.16.0.0/12" and "192.168.0.0/16" or non-rfc-1918 address spaces used in the VPC. |
| `users` | `array` | Output only. The list of resources that refer to this internal range. Resources that use the InternalRange for their range allocation are referred to as users of the range. Other resources mark themselves as users while doing so by creating a reference to this InternalRange. Having a user, based on this reference, prevents deletion of the InternalRange referred to. Can be empty. |
| `labels` | `object` | User-defined labels. |
| `network` | `string` | The URL or resource ID of the network in which to reserve the Internal Range. The network cannot be deleted if there are any reserved Internal Ranges referring to it. Legacy network is not supported. This can only be specified for a global internal address. Example: - URL: /compute/v1/projects/&#123;project&#125;/global/networks/&#123;resourceId&#125; - ID: network123 |
| `overlaps` | `array` | Optional. Types of resources that are allowed to overlap with the current InternalRange. |
| `ipCidrRange` | `string` | IP range that this InternalRange defines. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_internalRanges_get` | `SELECT` | `internalRangesId, locationsId, projectsId` | Gets details of a single InternalRange. |
| `projects_locations_internalRanges_list` | `SELECT` | `locationsId, projectsId` | Lists InternalRanges in a given project and location. |
| `projects_locations_internalRanges_create` | `INSERT` | `locationsId, projectsId` | Creates a new InternalRange in a given project and location. |
| `projects_locations_internalRanges_delete` | `DELETE` | `internalRangesId, locationsId, projectsId` | Deletes a single InternalRange. |
| `projects_locations_internalRanges_patch` | `EXEC` | `internalRangesId, locationsId, projectsId` | Updates the parameters of a single InternalRange. |
