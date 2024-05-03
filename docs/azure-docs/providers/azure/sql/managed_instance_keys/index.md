---
title: managed_instance_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_keys
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
<tr><td><b>Name</b></td><td><code>managed_instance_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="properties" /> | `object` | Properties for a key execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance key. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed instance keys. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates or updates a managed instance key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes the managed instance key with the given name. |
| <CopyableCode code="_list_by_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed instance keys. |
