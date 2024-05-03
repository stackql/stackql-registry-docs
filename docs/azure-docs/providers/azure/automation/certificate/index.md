---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.certificate" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId" /> | Retrieve the certificate identified by certificate name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of certificates. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId, data__name, data__properties" /> | Create a certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId" /> | Delete the certificate. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of certificates. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId" /> | Update a certificate. |
