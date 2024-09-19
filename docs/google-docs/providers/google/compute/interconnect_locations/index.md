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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>interconnect_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interconnect_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.interconnect_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional description of the resource. |
| <CopyableCode code="address" /> | `string` | [Output Only] The postal address of the Point of Presence, each line in the address is separated by a newline character. |
| <CopyableCode code="availabilityZone" /> | `string` | [Output Only] Availability zone for this InterconnectLocation. Within a metropolitan area (metro), maintenance will not be simultaneously scheduled in more than one availability zone. Example: "zone1" or "zone2". |
| <CopyableCode code="availableFeatures" /> | `array` | [Output only] List of features available at this InterconnectLocation, which can take one of the following values: - MACSEC  |
| <CopyableCode code="availableLinkTypes" /> | `array` | [Output only] List of link types available at this InterconnectLocation, which can take one of the following values: - LINK_TYPE_ETHERNET_10G_LR - LINK_TYPE_ETHERNET_100G_LR  |
| <CopyableCode code="city" /> | `string` | [Output Only] Metropolitan area designator that indicates which city an interconnect is located. For example: "Chicago, IL", "Amsterdam, Netherlands". |
| <CopyableCode code="continent" /> | `string` | [Output Only] Continent for this location, which can take one of the following values: - AFRICA - ASIA_PAC - EUROPE - NORTH_AMERICA - SOUTH_AMERICA  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="facilityProvider" /> | `string` | [Output Only] The name of the provider for this facility (e.g., EQUINIX). |
| <CopyableCode code="facilityProviderFacilityId" /> | `string` | [Output Only] A provider-assigned Identifier for this facility (e.g., Ashburn-DC1). |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#interconnectLocation for interconnect locations. |
| <CopyableCode code="peeringdbFacilityId" /> | `string` | [Output Only] The peeringdb identifier for this facility (corresponding with a netfac type in peeringdb). |
| <CopyableCode code="regionInfos" /> | `array` | [Output Only] A list of InterconnectLocation.RegionInfo objects, that describe parameters pertaining to the relation between this InterconnectLocation and various Google Cloud regions. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of this InterconnectLocation, which can take one of the following values: - CLOSED: The InterconnectLocation is closed and is unavailable for provisioning new Interconnects. - AVAILABLE: The InterconnectLocation is available for provisioning new Interconnects.  |
| <CopyableCode code="supportsPzs" /> | `boolean` | [Output Only] Reserved for future use. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="interconnectLocation, project" /> | Returns the details for the specified interconnect location. Gets a list of available interconnect locations by making a list() request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of interconnect locations available to the specified project. |

## `SELECT` examples

Retrieves the list of interconnect locations available to the specified project.

```sql
SELECT
id,
name,
description,
address,
availabilityZone,
availableFeatures,
availableLinkTypes,
city,
continent,
creationTimestamp,
facilityProvider,
facilityProviderFacilityId,
kind,
peeringdbFacilityId,
regionInfos,
selfLink,
status,
supportsPzs
FROM google.compute.interconnect_locations
WHERE project = '{{ project }}';
```
