---
title: interconnect_remote_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - interconnect_remote_locations
  - compute
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
<tr><td><b>Name</b></td><td><code>interconnect_remote_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.interconnect_remote_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] An optional description of the resource. |
| `attachmentConfigurationConstraints` | `object` |  |
| `lacp` | `string` | [Output Only] Link Aggregation Control Protocol (LACP) constraints, which can take one of the following values: LACP_SUPPORTED, LACP_UNSUPPORTED |
| `facilityProviderFacilityId` | `string` | [Output Only] A provider-assigned Identifier for this facility (e.g., Ashburn-DC1). |
| `maxLagSize10Gbps` | `integer` | [Output Only] The maximum number of 10 Gbps ports supported in a link aggregation group (LAG). When linkType is 10 Gbps, requestedLinkCount cannot exceed max_lag_size_10_gbps. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#interconnectRemoteLocation for interconnect remote locations. |
| `city` | `string` | [Output Only] Metropolitan area designator that indicates which city an interconnect is located. For example: "Chicago, IL", "Amsterdam, Netherlands". |
| `peeringdbFacilityId` | `string` | [Output Only] The peeringdb identifier for this facility (corresponding with a netfac type in peeringdb). |
| `facilityProvider` | `string` | [Output Only] The name of the provider for this facility (e.g., EQUINIX). |
| `address` | `string` | [Output Only] The postal address of the Point of Presence, each line in the address is separated by a newline character. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `continent` | `string` | [Output Only] Continent for this location, which can take one of the following values: - AFRICA - ASIA_PAC - EUROPE - NORTH_AMERICA - SOUTH_AMERICA  |
| `constraints` | `object` |  |
| `maxLagSize100Gbps` | `integer` | [Output Only] The maximum number of 100 Gbps ports supported in a link aggregation group (LAG). When linkType is 100 Gbps, requestedLinkCount cannot exceed max_lag_size_100_gbps. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `remoteService` | `string` | [Output Only] Indicates the service provider present at the remote location. Example values: "Amazon Web Services", "Microsoft Azure". |
| `permittedConnections` | `array` | [Output Only] Permitted connections. |
| `status` | `string` | [Output Only] The status of this InterconnectRemoteLocation, which can take one of the following values: - CLOSED: The InterconnectRemoteLocation is closed and is unavailable for provisioning new Cross-Cloud Interconnects. - AVAILABLE: The InterconnectRemoteLocation is available for provisioning new Cross-Cloud Interconnects.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `interconnectRemoteLocation, project` | Returns the details for the specified interconnect remote location. Gets a list of available interconnect remote locations by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of interconnect remote locations available to the specified project. |
| `_list` | `EXEC` | `project` | Retrieves the list of interconnect remote locations available to the specified project. |
