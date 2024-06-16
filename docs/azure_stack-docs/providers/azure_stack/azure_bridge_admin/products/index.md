---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_bridge_admin.products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for a product. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Return product name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Return product name. |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Downloads a product from azure marketplace. |
