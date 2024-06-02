---
title: firewall_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_endpoints
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>firewall_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="networksecurity.firewall_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. name of resource |
| <CopyableCode code="description" /> | `string` | Optional. Description of the firewall endpoint. Max length 2048 characters. |
| <CopyableCode code="associatedNetworks" /> | `array` | Output only. List of networks that are associated with this endpoint in the local zone. This is a projection of the FirewallEndpointAssociations pointing at this endpoint. A network will only appear in this list after traffic routing is fully configured. Format: projects/&#123;project&#125;/global/networks/&#123;name&#125;. |
| <CopyableCode code="associations" /> | `array` | Output only. List of FirewallEndpointAssociations that are associated to this endpoint. An association will only appear in this list after traffic routing is fully configured. |
| <CopyableCode code="billingProjectId" /> | `string` | Required. Project to bill on endpoint uptime usage. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the endpoint. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_firewall_endpoints_get" /> | `SELECT` | <CopyableCode code="firewallEndpointsId, locationsId, organizationsId" /> | Gets details of a single Endpoint. |
| <CopyableCode code="organizations_locations_firewall_endpoints_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists FirewallEndpoints in a given project and location. |
| <CopyableCode code="organizations_locations_firewall_endpoints_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new FirewallEndpoint in a given project and location. |
| <CopyableCode code="organizations_locations_firewall_endpoints_delete" /> | `DELETE` | <CopyableCode code="firewallEndpointsId, locationsId, organizationsId" /> | Deletes a single Endpoint. |
| <CopyableCode code="_organizations_locations_firewall_endpoints_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists FirewallEndpoints in a given project and location. |
| <CopyableCode code="organizations_locations_firewall_endpoints_patch" /> | `EXEC` | <CopyableCode code="firewallEndpointsId, locationsId, organizationsId" /> | Update a single Endpoint. |
