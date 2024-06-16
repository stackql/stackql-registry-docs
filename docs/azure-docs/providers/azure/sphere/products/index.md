---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - sphere
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.products" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Get a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Product resources by Catalog |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Create a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Delete a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name' |
| <CopyableCode code="count_devices" /> | `EXEC` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Counts devices in product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="generate_default_device_groups" /> | `EXEC` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Generates default device groups for the product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Update a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
