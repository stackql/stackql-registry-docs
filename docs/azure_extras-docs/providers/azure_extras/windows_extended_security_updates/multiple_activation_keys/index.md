---
title: multiple_activation_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - multiple_activation_keys
  - windows_extended_security_updates
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>multiple_activation_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.windows_extended_security_updates.multiple_activation_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MAK key specific properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Get a MAK key. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Multiple Activation Keys (MAK) created for a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Multiple Activation Keys (MAK) in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Create a MAK key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Delete a MAK key. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Update a MAK key. |
