---
title: network_fabrics_topology
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics_topology
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_fabrics_topology</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabrics_topology" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationState" /> | `string` | Configuration state for the resource. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="url" /> | `string` | URL for the details of the response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> |
