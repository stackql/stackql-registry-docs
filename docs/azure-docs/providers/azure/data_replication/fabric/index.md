---
title: fabric
hide_title: false
hide_table_of_contents: false
keywords:
  - fabric
  - data_replication
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
<tr><td><b>Name</b></td><td><code>fabric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.fabric" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location of the fabric. |
| <CopyableCode code="properties" /> | `object` | Fabric model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Gets the details of the fabric. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the list of fabrics in the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of fabrics in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Creates the fabric. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Removes the fabric. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Performs update on the fabric. |
