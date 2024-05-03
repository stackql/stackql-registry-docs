---
title: workload_networks_port_mirroring
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_networks_port_mirroring
  - vmware
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>workload_networks_port_mirroring</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.workload_networks_port_mirroring" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="portMirroringId, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="portMirroringId, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="portMirroringId, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="portMirroringId, privateCloudName, resourceGroupName, subscriptionId" /> |
