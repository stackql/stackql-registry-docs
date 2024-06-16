---
title: contact_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_profiles
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
<tr><td><b>Name</b></td><td><code>contact_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.contact_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the contact profile resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId" /> | Gets the specified contact Profile in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns list of contact profiles by Resource Group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns list of contact profiles by Subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a contact profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId" /> | Deletes a specified contact profile resource. |
