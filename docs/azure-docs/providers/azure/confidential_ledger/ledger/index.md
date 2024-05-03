---
title: ledger
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger
  - confidential_ledger
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
<tr><td><b>Name</b></td><td><code>ledger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger.ledger" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Additional Confidential Ledger properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Retrieves the properties of a Confidential Ledger. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the properties of all Confidential Ledgers. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the properties of all Confidential Ledgers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Creates a  Confidential Ledger with the specified ledger parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Deletes an existing Confidential Ledger. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the properties of all Confidential Ledgers. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieves the properties of all Confidential Ledgers. |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId, data__uri" /> | Backs up a Confidential Ledger Resource. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId, data__fileShareName, data__restoreRegion, data__uri" /> | Restores a Confidential Ledger Resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Updates properties of Confidential Ledger |
