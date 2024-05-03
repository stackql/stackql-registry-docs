---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
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
<tr><td><b>Name</b></td><td><code>private_clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.private_clouds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a private cloud resource |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId, data__location, data__sku" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_in_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="list_in_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="rotate_nsxt_password" /> | `EXEC` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="rotate_vcenter_password" /> | `EXEC` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
