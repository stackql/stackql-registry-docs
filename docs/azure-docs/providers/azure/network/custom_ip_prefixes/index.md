---
title: custom_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_ip_prefixes
  - network
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
<tr><td><b>Name</b></td><td><code>custom_ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.custom_ip_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Custom IP prefix properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Gets the specified custom IP prefix in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all custom IP prefixes in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Creates or updates a custom IP prefix. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Deletes the specified custom IP prefix. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all custom IP prefixes in a resource group. |
