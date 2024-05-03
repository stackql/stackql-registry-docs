---
title: credential
hide_title: false
hide_table_of_contents: false
keywords:
  - credential
  - automation
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
<tr><td><b>Name</b></td><td><code>credential</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.credential" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, credentialName, resourceGroupName, subscriptionId" /> | Retrieve the credential identified by credential name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of credentials. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, credentialName, resourceGroupName, subscriptionId, data__name, data__properties" /> | Create a credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, credentialName, resourceGroupName, subscriptionId" /> | Delete the credential. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of credentials. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, credentialName, resourceGroupName, subscriptionId" /> | Update a credential. |
