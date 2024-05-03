---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.offers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Represents an offering of services against which a subscription can be created. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Get the specified offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get the list of offers under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Create or update the offer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Delete the specified offer. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get the list of offers under a resource group. |
| <CopyableCode code="link" /> | `EXEC` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Links a plan to an offer. |
| <CopyableCode code="unlink" /> | `EXEC` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Unlink a plan from an offer. |
