---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
  - consumption
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
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.budgets" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="budgetName, scope" /> | Gets the budget for the scope by budget name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Lists all budgets for the defined scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="budgetName, scope" /> | The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="budgetName, scope" /> | The operation to delete a budget. |
