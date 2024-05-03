---
title: afd_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_custom_domains
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_custom_domains" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor domains. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Creates a new domain within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile. |
| <CopyableCode code="_list_by_profile" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor domains. |
| <CopyableCode code="refresh_validation_token" /> | `EXEC` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Updates the domain validation token. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing domain within a profile. |
