---
title: ddos_custom_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - ddos_custom_policies
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
<tr><td><b>Name</b></td><td><code>ddos_custom_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.ddos_custom_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | DDoS custom policy properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Gets information about the specified DDoS custom policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Creates or updates a DDoS custom policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified DDoS custom policy. |
