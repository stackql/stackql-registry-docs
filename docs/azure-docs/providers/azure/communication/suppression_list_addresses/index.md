---
title: suppression_list_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - suppression_list_addresses
  - communication
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
<tr><td><b>Name</b></td><td><code>suppression_list_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.suppression_list_addresses" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Get a SuppressionListAddress. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Get all the addresses in a suppression list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Create or update a SuppressionListAddress. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Operation to delete a single address from a suppression list. |
