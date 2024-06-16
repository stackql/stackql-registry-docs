---
title: db_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_nodes
  - oracle
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
<tr><td><b>Name</b></td><td><code>db_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.db_nodes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudvmclustername, dbnodeocid, resourceGroupName, subscriptionId" /> | Get a DbNode |
| <CopyableCode code="list_by_cloud_vm_cluster" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | List DbNode resources by CloudVmCluster |
| <CopyableCode code="action" /> | `EXEC` | <CopyableCode code="cloudvmclustername, dbnodeocid, resourceGroupName, subscriptionId, data__action" /> | VM actions on DbNode of VM Cluster by the provided filter |
