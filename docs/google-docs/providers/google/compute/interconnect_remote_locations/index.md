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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interconnect_remote_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="compute.interconnect_remote_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional description of the resource. |
| <CopyableCode code="address" /> | `string` | [Output Only] The postal address of the Point of Presence, each line in the address is separated by a newline character. |
| <CopyableCode code="attachmentConfigurationConstraints" /> | `object` |  |
| <CopyableCode code="city" /> | `string` | [Output Only] Metropolitan area designator that indicates which city an interconnect is located. For example: "Chicago, IL", "Amsterdam, Netherlands". |
| <CopyableCode code="constraints" /> | `object` |  |
| <CopyableCode code="continent" /> | `string` | [Output Only] Continent for this location, which can take one of the following values: - AFRICA - ASIA_PAC - EUROPE - NORTH_AMERICA - SOUTH_AMERICA  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="facilityProvider" /> | `string` | [Output Only] The name of the provider for this facility (e.g., EQUINIX). |
| <CopyableCode code="facilityProviderFacilityId" /> | `string` | [Output Only] A provider-assigned Identifier for this facility (e.g., Ashburn-DC1). |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#interconnectRemoteLocation for interconnect remote locations. |
| <CopyableCode code="lacp" /> | `string` | [Output Only] Link Aggregation Control Protocol (LACP) constraints, which can take one of the following values: LACP_SUPPORTED, LACP_UNSUPPORTED |
| <CopyableCode code="maxLagSize100Gbps" /> | `integer` | [Output Only] The maximum number of 100 Gbps ports supported in a link aggregation group (LAG). When linkType is 100 Gbps, requestedLinkCount cannot exceed max_lag_size_100_gbps. |
| <CopyableCode code="maxLagSize10Gbps" /> | `integer` | [Output Only] The maximum number of 10 Gbps ports supported in a link aggregation group (LAG). When linkType is 10 Gbps, requestedLinkCount cannot exceed max_lag_size_10_gbps. |
| <CopyableCode code="peeringdbFacilityId" /> | `string` | [Output Only] The peeringdb identifier for this facility (corresponding with a netfac type in peeringdb). |
| <CopyableCode code="permittedConnections" /> | `array` | [Output Only] Permitted connections. |
| <CopyableCode code="remoteService" /> | `string` | [Output Only] Indicates the service provider present at the remote location. Example values: "Amazon Web Services", "Microsoft Azure". |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of this InterconnectRemoteLocation, which can take one of the following values: - CLOSED: The InterconnectRemoteLocation is closed and is unavailable for provisioning new Cross-Cloud Interconnects. - AVAILABLE: The InterconnectRemoteLocation is available for provisioning new Cross-Cloud Interconnects.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="interconnectRemoteLocation, project" /> | Returns the details for the specified interconnect remote location. Gets a list of available interconnect remote locations by making a list() request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of interconnect remote locations available to the specified project. |
