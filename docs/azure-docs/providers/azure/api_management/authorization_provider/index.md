---
title: authorization_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_provider
  - api_management
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
<tr><td><b>Name</b></td><td><code>authorization_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_provider" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization provider specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization providers defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates authorization provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific authorization provider from the API Management service instance. |
