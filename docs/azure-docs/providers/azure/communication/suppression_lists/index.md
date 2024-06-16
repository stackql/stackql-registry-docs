---
title: suppression_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - suppression_lists
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
<tr><td><b>Name</b></td><td><code>suppression_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.suppression_lists" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Get a SuppressionList resource. |
| <CopyableCode code="list_by_domain" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | List all suppression lists for a domains resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Add a new SuppressionList resource under the parent Domains resource or update an existing SuppressionList resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Delete a SuppressionList. |
