---
title: cloud_hsm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_clusters
  - hardware_security_modules
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
<tr><td><b>Name</b></td><td><code>cloud_hsm_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.cloud_hsm_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="properties" /> | `object` | Properties of a Cloud HSM Cluster. |
| <CopyableCode code="sku" /> | `object` | Cloud Hsm Cluster SKU information |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Gets the specified Cloud HSM Cluster |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the Cloud HSM Clusters associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the Cloud HSM Clusters associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Create or Update a Cloud HSM Cluster in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Deletes the specified Cloud HSM Cluster |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Update a Cloud HSM Cluster in the specified subscription. |
