---
title: signal_r_replica_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_replica_skus
  - signalr
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
<tr><td><b>Name</b></td><td><code>signal_r_replica_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.signalr.signal_r_replica_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Describes scaling information of a sku. |
| <CopyableCode code="resourceType" /> | `string` | The resource type that this object applies to |
| <CopyableCode code="sku" /> | `object` | The billing information of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> |
