---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
  - vmwareengine
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
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vmwareengine.subnets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this subnet. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet` |
| <CopyableCode code="gatewayIp" /> | `string` | The IP address of the gateway of this subnet. Must fall within the IP prefix defined above. |
| <CopyableCode code="ipCidrRange" /> | `string` | The IP address range of the subnet in CIDR format '10.0.0.0/24'. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the resource. |
| <CopyableCode code="type" /> | `string` | Output only. The type of the subnet. For example "management" or "userDefined". |
| <CopyableCode code="vlanId" /> | `integer` | Output only. VLAN ID of the VLAN on which the subnet is configured |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId, subnetsId" /> | Gets details of a single subnet. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists subnets in a given private cloud. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists subnets in a given private cloud. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId, subnetsId" /> | Updates the parameters of a single subnet. Only fields specified in `update_mask` are applied. *Note*: This API is synchronous and always returns a successful `google.longrunning.Operation` (LRO). The returned LRO will only have `done` and `response` fields. |
