---
title: interconnect_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - interconnect_locations
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
<tr><td><b>Name</b></td><td><code>interconnect_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.interconnect_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] An optional description of the resource. |
| `regionInfos` | `array` | [Output Only] A list of InterconnectLocation.RegionInfo objects, that describe parameters pertaining to the relation between this InterconnectLocation and various Google Cloud regions. |
| `status` | `string` | [Output Only] The status of this InterconnectLocation, which can take one of the following values: - CLOSED: The InterconnectLocation is closed and is unavailable for provisioning new Interconnects. - AVAILABLE: The InterconnectLocation is available for provisioning new Interconnects.  |
| `facilityProvider` | `string` | [Output Only] The name of the provider for this facility (e.g., EQUINIX). |
| `city` | `string` | [Output Only] Metropolitan area designator that indicates which city an interconnect is located. For example: "Chicago, IL", "Amsterdam, Netherlands". |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#interconnectLocation for interconnect locations. |
| `peeringdbFacilityId` | `string` | [Output Only] The peeringdb identifier for this facility (corresponding with a netfac type in peeringdb). |
| `address` | `string` | [Output Only] The postal address of the Point of Presence, each line in the address is separated by a newline character. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `continent` | `string` | [Output Only] Continent for this location, which can take one of the following values: - AFRICA - ASIA_PAC - EUROPE - NORTH_AMERICA - SOUTH_AMERICA  |
| `supportsPzs` | `boolean` | [Output Only] Set to true for locations that support physical zone separation. Defaults to false if the field is not present. |
| `facilityProviderFacilityId` | `string` | [Output Only] A provider-assigned Identifier for this facility (e.g., Ashburn-DC1). |
| `availabilityZone` | `string` | [Output Only] Availability zone for this InterconnectLocation. Within a metropolitan area (metro), maintenance will not be simultaneously scheduled in more than one availability zone. Example: "zone1" or "zone2". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `interconnectLocations_get` | `SELECT` | `interconnectLocation, project` | Returns the details for the specified interconnect location. Gets a list of available interconnect locations by making a list() request. |
| `interconnectLocations_list` | `SELECT` | `project` | Retrieves the list of interconnect locations available to the specified project. |
