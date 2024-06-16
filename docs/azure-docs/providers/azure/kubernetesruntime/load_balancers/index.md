---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - kubernetesruntime
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesruntime.load_balancers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceUri" /> | Get a LoadBalancer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List LoadBalancer resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loadBalancerName, resourceUri" /> | Create a LoadBalancer |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="loadBalancerName, resourceUri" /> | Delete a LoadBalancer |
