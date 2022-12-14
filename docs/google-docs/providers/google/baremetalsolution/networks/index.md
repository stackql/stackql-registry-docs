---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier for the `Network`, generated by the backend. |
| `name` | `string` | Output only. The resource name of this `Network`. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/networks/&#123;network&#125;` |
| `reservations` | `array` | List of IP address reservations in this network. When updating this field, an error will be generated if a reservation conflicts with an IP address already allocated to a physical server. |
| `macAddress` | `array` | List of physical interfaces. |
| `servicesCidr` | `string` | IP range for reserved for services (e.g. NFS). |
| `ipAddress` | `string` | IP address configured. |
| `mountPoints` | `array` | Input only. List of mount points to attach the network to. |
| `jumboFramesEnabled` | `boolean` | Whether network uses standard frames or jumbo ones. |
| `labels` | `object` | Labels as key value pairs. |
| `gatewayIp` | `string` | Output only. Gateway ip address. |
| `pod` | `string` | Output only. Pod name. |
| `state` | `string` | The Network state. |
| `vrf` | `object` | A network VRF. |
| `vlanId` | `string` | The vlan id of the Network. |
| `cidr` | `string` | The cidr of the Network. |
| `type` | `string` | The type of this network. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_networks_get` | `SELECT` | `locationsId, networksId, projectsId` | Get details of a single network. |
| `projects_locations_networks_list` | `SELECT` | `locationsId, projectsId` | List network in a given project and location. |
| `projects_locations_networks_patch` | `EXEC` | `locationsId, networksId, projectsId` | Update details of a single network. |
