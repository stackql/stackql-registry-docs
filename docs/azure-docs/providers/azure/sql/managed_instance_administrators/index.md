---
title: managed_instance_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_administrators
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_instance_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_administrators" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="administratorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance administrator. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed instance administrators. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="administratorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates or updates a managed instance administrator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="administratorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a managed instance administrator. |
| <CopyableCode code="_list_by_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed instance administrators. |
