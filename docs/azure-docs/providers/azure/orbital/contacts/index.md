---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - orbital
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.contacts" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactName, resourceGroupName, spacecraftName, subscriptionId" /> | Gets the specified contact in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId" /> | Returns list of contacts by spacecraftName. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="contactName, resourceGroupName, spacecraftName, subscriptionId, data__properties" /> | Creates a contact. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contactName, resourceGroupName, spacecraftName, subscriptionId" /> | Deletes a specified contact. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId" /> | Returns list of contacts by spacecraftName. |
