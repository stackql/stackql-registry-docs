---
title: configuration_group_values
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_values
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>configuration_group_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.configuration_group_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Hybrid configuration group value properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Gets information about the specified hybrid configuration group values. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the hybrid network configurationGroupValues in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all sites in the configuration group value in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Creates or updates a hybrid configuration group value. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationGroupValueName, resourceGroupName, subscriptionId" /> | Deletes the specified hybrid configuration group value. |
