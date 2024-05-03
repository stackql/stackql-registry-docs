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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spokes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.spokes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the spoke. Spoke names must be unique. They use the following form: `projects/&#123;project_number&#125;/locations/&#123;region&#125;/spokes/&#123;spoke_id&#125;` |
| <CopyableCode code="description" /> | `string` | An optional description of the spoke. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the spoke was created. |
| <CopyableCode code="group" /> | `string` | The name of the group that this spoke is associated with. |
| <CopyableCode code="hub" /> | `string` | Immutable. The name of the hub that this spoke is attached to. |
| <CopyableCode code="labels" /> | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="linkedInterconnectAttachments" /> | `object` | A collection of VLAN attachment resources. These resources should be redundant attachments that all advertise the same prefixes to Google Cloud. Alternatively, in active/passive configurations, all attachments should be capable of advertising the same prefixes. |
| <CopyableCode code="linkedRouterApplianceInstances" /> | `object` | A collection of router appliance instances. If you configure multiple router appliance instances to receive data from the same set of sites outside of Google Cloud, we recommend that you associate those instances with the same spoke. |
| <CopyableCode code="linkedVpcNetwork" /> | `object` | An existing VPC network. |
| <CopyableCode code="linkedVpnTunnels" /> | `object` | A collection of Cloud VPN tunnel resources. These resources should be redundant HA VPN tunnels that all advertise the same prefixes to Google Cloud. Alternatively, in a passive/active configuration, all tunnels should be capable of advertising the same prefixes. |
| <CopyableCode code="reasons" /> | `array` | Output only. The reasons for current state of the spoke. Only present when the spoke is in the `INACTIVE` state. |
| <CopyableCode code="spokeType" /> | `string` | Output only. The type of resource associated with the spoke. |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of this spoke. |
| <CopyableCode code="uniqueId" /> | `string` | Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different `unique_id`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the spoke was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Gets details about a Network Connectivity Center spoke. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the Network Connectivity Center spokes in a specified project and location. |
| <CopyableCode code="list_spokes" /> | `SELECT` | <CopyableCode code="hubsId, projectsId" /> | Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Network Connectivity Center spoke. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Deletes a Network Connectivity Center spoke. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists the Network Connectivity Center spokes in a specified project and location. |
| <CopyableCode code="_list_spokes" /> | `EXEC` | <CopyableCode code="hubsId, projectsId" /> | Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted. |
| <CopyableCode code="accept" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Accepts a proposal to attach a Network Connectivity Center spoke to the hub. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Updates the parameters of a Network Connectivity Center spoke. |
| <CopyableCode code="reject" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, spokesId" /> | Rejects a Network Connectivity Center spoke from being attached to the hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub. |
