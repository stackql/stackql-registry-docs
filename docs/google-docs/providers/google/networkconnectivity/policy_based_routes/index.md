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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_based_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="networkconnectivity.policy_based_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. A unique name of the resource in the form of `projects/&#123;project_number&#125;/locations/global/PolicyBasedRoutes/&#123;policy_based_route_id&#125;` |
| <CopyableCode code="description" /> | `string` | Optional. An optional description of this resource. Provide this field when you create the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the policy-based route was created. |
| <CopyableCode code="filter" /> | `object` | Filter matches L4 traffic. |
| <CopyableCode code="interconnectAttachment" /> | `object` | InterconnectAttachment that this route applies to. |
| <CopyableCode code="kind" /> | `string` | Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="network" /> | `string` | Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network. |
| <CopyableCode code="nextHopIlbIp" /> | `string` | Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported. |
| <CopyableCode code="nextHopOtherRoutes" /> | `string` | Optional. Other routes that will be referenced to determine the next hop of the packet. |
| <CopyableCode code="priority" /> | `integer` | Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000. The priority value must be from 1 to 65535, inclusive. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined fully-qualified URL for this resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the policy-based route was updated. |
| <CopyableCode code="virtualMachine" /> | `object` | VM instances to which this policy-based route applies to. |
| <CopyableCode code="warnings" /> | `array` | Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyBasedRoutesId, projectsId" /> | Gets details of a single policy-based route. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists policy-based routes in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new policy-based route in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyBasedRoutesId, projectsId" /> | Deletes a single policy-based route. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists policy-based routes in a given project and location. |
