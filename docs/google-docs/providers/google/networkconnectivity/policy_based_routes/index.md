---
title: policy_based_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_based_routes
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
<tr><td><b>Name</b></td><td><code>policy_based_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.policy_based_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. A unique name of the resource in the form of `projects/&#123;project_number&#125;/locations/global/PolicyBasedRoutes/&#123;policy_based_route_id&#125;` |
| `description` | `string` | Optional. An optional description of this resource. Provide this field when you create the resource. |
| `virtualMachine` | `object` | VM instances to which this policy based route applies to. |
| `kind` | `string` | Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for Policy Based Route resources. |
| `createTime` | `string` | Output only. Time when the PolicyBasedRoute was created. |
| `updateTime` | `string` | Output only. Time when the PolicyBasedRoute was updated. |
| `interconnectAttachment` | `object` | InterconnectAttachment to which this route applies to. |
| `warnings` | `array` | Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages. |
| `priority` | `integer` | Optional. The priority of this policy based route. Priority is used to break ties in cases where there are more than one matching policy based routes found. In cases where multiple policy based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000. The priority value must be from 1 to 65535, inclusive. |
| `filter` | `object` | Filter matches L4 traffic. |
| `nextHopOtherRoutes` | `string` | Optional. Other routes that will be referenced to determine the next hop of the packet. |
| `network` | `string` | Required. Fully-qualified URL of the network that this route applies to. e.g. projects/my-project/global/networks/my-network. |
| `nextHopIlbIp` | `string` | Optional. The IP of a global access enabled L4 ILB that should be the next hop to handle matching packets. For this version, only next_hop_ilb_ip is supported. |
| `selfLink` | `string` | Output only. Server-defined fully-qualified URL for this resource. |
| `labels` | `object` | User-defined labels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyBasedRoutesId, projectsId` | Gets details of a single PolicyBasedRoute. |
| `list` | `SELECT` | `projectsId` | Lists PolicyBasedRoutes in a given project and location. |
| `create` | `INSERT` | `projectsId` | Creates a new PolicyBasedRoute in a given project and location. |
| `delete` | `DELETE` | `policyBasedRoutesId, projectsId` | Deletes a single PolicyBasedRoute. |
| `_list` | `EXEC` | `projectsId` | Lists PolicyBasedRoutes in a given project and location. |
