---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - search
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID of the quota usage SKU endpoint for Microsoft.Search provider. |
| <CopyableCode code="name" /> | `object` | The name of the SKU supported by Azure AI Search. |
| <CopyableCode code="currentValue" /> | `integer` | The currently used up value for the particular search SKU. |
| <CopyableCode code="limit" /> | `integer` | The quota limit for the particular search SKU. |
| <CopyableCode code="unit" /> | `string` | The unit of measurement for the search SKU. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get a list of all Azure AI Search quota usages across the subscription. |
| <CopyableCode code="usages" /> | `EXEC` | <CopyableCode code="location, skuName, subscriptionId" /> | Gets the quota usage for a search sku in the given subscription. |
