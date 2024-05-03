---
title: bmc_key_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - bmc_key_sets
  - nexus
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
<tr><td><b>Name</b></td><td><code>bmc_key_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.bmc_key_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Get baseboard management controller key set of the provided cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a list of baseboard management controller key sets for the provided cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new baseboard management controller key set or update the existing one for the provided cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Delete the baseboard management controller key set of the provided cluster. |
| <CopyableCode code="_list_by_cluster" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a list of baseboard management controller key sets for the provided cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Patch properties of baseboard management controller key set for the provided cluster, or update the tags associated with it. Properties and tag updates can be done independently. |
