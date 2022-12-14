---
title: spokes
hide_title: false
hide_table_of_contents: false
keywords:
  - spokes
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
<tr><td><b>Name</b></td><td><code>spokes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.spokes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of the spoke. Spoke names must be unique. They use the following form: `projects/&#123;project_number&#125;/locations/&#123;region&#125;/spokes/&#123;spoke_id&#125;` |
| `description` | `string` | An optional description of the spoke. |
| `updateTime` | `string` | Output only. The time the spoke was last updated. |
| `linkedRouterApplianceInstances` | `object` | A collection of router appliance instances. If you configure multiple router appliance instances to receive data from the same set of sites outside of Google Cloud, we recommend that you associate those instances with the same spoke. |
| `state` | `string` | Output only. The current lifecycle state of this spoke. |
| `hub` | `string` | Immutable. The name of the hub that this spoke is attached to. |
| `labels` | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| `linkedInterconnectAttachments` | `object` | A collection of VLAN attachment resources. These resources should be redundant attachments that all advertise the same prefixes to Google Cloud. Alternatively, in active/passive configurations, all attachments should be capable of advertising the same prefixes. |
| `uniqueId` | `string` | Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different unique_id. |
| `createTime` | `string` | Output only. The time the spoke was created. |
| `linkedVpnTunnels` | `object` | A collection of Cloud VPN tunnel resources. These resources should be redundant HA VPN tunnels that all advertise the same prefixes to Google Cloud. Alternatively, in a passive/active configuration, all tunnels should be capable of advertising the same prefixes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_spokes_get` | `SELECT` | `locationsId, projectsId, spokesId` | Gets details about a Network Connectivity Center spoke. |
| `projects_locations_spokes_list` | `SELECT` | `locationsId, projectsId` | Lists the Network Connectivity Center spokes in a specified project and location. |
| `projects_locations_spokes_create` | `INSERT` | `locationsId, projectsId` | Creates a Network Connectivity Center spoke. |
| `projects_locations_spokes_delete` | `DELETE` | `locationsId, projectsId, spokesId` | Deletes a Network Connectivity Center spoke. |
| `projects_locations_spokes_patch` | `EXEC` | `locationsId, projectsId, spokesId` | Updates the parameters of a Network Connectivity Center spoke. |
