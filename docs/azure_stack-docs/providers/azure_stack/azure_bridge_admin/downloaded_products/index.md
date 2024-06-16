---
title: downloaded_products
hide_title: false
hide_table_of_contents: false
keywords:
  - downloaded_products
  - azure_bridge_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>downloaded_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_bridge_admin.downloaded_products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for aggregate usage. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Get a downloaded product. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Get a list of downloaded products. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Creates a downloaded product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Delete a downloaded product. |
