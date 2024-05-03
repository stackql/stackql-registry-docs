---
title: managed_ccf
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ccf
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
<tr><td><b>Name</b></td><td><code>managed_ccf</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger.managed_ccf" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Additional Managed CCF properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Retrieves the properties of a Managed CCF app. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the properties of all Managed CCF apps. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the properties of all Managed CCF. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Creates a Managed CCF with the specified Managed CCF parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Deletes an existing Managed CCF. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the properties of all Managed CCF apps. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieves the properties of all Managed CCF. |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, subscriptionId, data__uri" /> | Backs up a Managed CCF Resource. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, subscriptionId, data__fileShareName, data__restoreRegion, data__uri" /> | Restores a Managed CCF Resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Updates properties of Managed CCF |
