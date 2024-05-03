---
title: professional_service_subscription_level
hide_title: false
hide_table_of_contents: false
keywords:
  - professional_service_subscription_level
  - professional_services
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
<tr><td><b>Name</b></td><td><code>professional_service_subscription_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.professional_services.professional_service_subscription_level" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource uri |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | professionalService properties |
| <CopyableCode code="tags" /> | `object` | the resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets information about the specified Subscription Level ProfessionalService. |
| <CopyableCode code="list_by_azure_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about all the Subscription Level ProfessionalService in a certain Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets information about all the Subscription Level ProfessionalService in a certain resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates or updates a ProfessionalService resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes the specified ProfessionalService. |
| <CopyableCode code="_list_by_azure_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets information about all the Subscription Level ProfessionalService in a certain Azure subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets information about all the Subscription Level ProfessionalService in a certain resource group. |
