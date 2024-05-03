---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
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
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the hub. Hub names must be unique. They use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub_id&#125;` |
| <CopyableCode code="description" /> | `string` | An optional description of the hub. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the hub was created. |
| <CopyableCode code="labels" /> | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="routeTables" /> | `array` | Output only. The route tables that belong to this hub. They use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub_id&#125;/routeTables/&#123;route_table_id&#125;` This field is read-only. Network Connectivity Center automatically populates it based on the route tables nested under the hub. |
| <CopyableCode code="routingVpcs" /> | `array` | The VPC networks associated with this hub's spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub. |
| <CopyableCode code="spokeSummary" /> | `object` | Summarizes information about the spokes associated with a hub. The summary includes a count of spokes according to type and according to state. If any spokes are inactive, the summary also lists the reasons they are inactive, including a count for each reason. |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of this hub. |
| <CopyableCode code="uniqueId" /> | `string` | Output only. The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the hub was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubsId, projectsId" /> | Gets details about a Network Connectivity Center hub. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the Network Connectivity Center hubs associated with a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new Network Connectivity Center hub in the specified project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubsId, projectsId" /> | Deletes a Network Connectivity Center hub. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists the Network Connectivity Center hubs associated with a given project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="hubsId, projectsId" /> | Updates the description and/or labels of a Network Connectivity Center hub. |
