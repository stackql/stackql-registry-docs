---
title: azure_ad_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_ad_administrators
  - mysql
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
<tr><td><b>Name</b></td><td><code>azure_ad_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.azure_ad_administrators" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="administratorName, resourceGroupName, serverName, subscriptionId" /> | Gets information about an azure ad administrator. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the AAD administrators in a given server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="administratorName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an existing Azure Active Directory administrator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="administratorName, resourceGroupName, serverName, subscriptionId" /> | Deletes an Azure AD Administrator. |
