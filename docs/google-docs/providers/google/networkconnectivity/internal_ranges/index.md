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
| `name` | `string` | Immutable. The name of an internal range. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/internalRanges/&#123;internal_range&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| `description` | `string` | A description of this resource. |
| `prefixLength` | `integer` | An alternate to ip_cidr_range. Can be set when trying to create a reservation that automatically finds a free range of the given size. If both ip_cidr_range and prefix_length are set, there is an error if the range sizes do not match. Can also be used during updates to change the range size. |
| `overlaps` | `array` | Optional. Types of resources that are allowed to overlap with the current internal range. |
| `labels` | `object` | User-defined labels. |
| `updateTime` | `string` | Time when the internal range was updated. |
| `usage` | `string` | The type of usage set for this InternalRange. |
| `createTime` | `string` | Time when the internal range was created. |
| `ipCidrRange` | `string` | The IP range that this internal range defines. |
| `users` | `array` | Output only. The list of resources that refer to this internal range. Resources that use the internal range for their range allocation are referred to as users of the range. Other resources mark themselves as users while doing so by creating a reference to this internal range. Having a user, based on this reference, prevents deletion of the internal range referred to. Can be empty. |
| `peering` | `string` | The type of peering set for this internal range. |
| `network` | `string` | The URL or resource ID of the network in which to reserve the internal range. The network cannot be deleted if there are any reserved internal ranges referring to it. Legacy networks are not supported. This can only be specified for a global internal address. Example: - URL: /compute/v1/projects/&#123;project&#125;/global/networks/&#123;resourceId&#125; - ID: network123 |
| `targetCidrRange` | `array` | Optional. Can be set to narrow down or pick a different address space while searching for a free range. If not set, defaults to the "10.0.0.0/8" address space. This can be used to search in other rfc-1918 address spaces like "172.16.0.0/12" and "192.168.0.0/16" or non-rfc-1918 address spaces used in the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `internalRangesId, locationsId, projectsId` | Gets details of a single internal range. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists internal ranges in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new internal range in a given project and location. |
| `delete` | `DELETE` | `internalRangesId, locationsId, projectsId` | Deletes a single internal range. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists internal ranges in a given project and location. |
| `patch` | `EXEC` | `internalRangesId, locationsId, projectsId` | Updates the parameters of a single internal range. |
