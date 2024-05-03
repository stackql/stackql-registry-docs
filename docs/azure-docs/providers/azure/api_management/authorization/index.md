---
title: authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization
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
<tr><td><b>Name</b></td><td><code>authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization specified by its identifier. |
| <CopyableCode code="list_by_authorization_provider" /> | `SELECT` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization providers defined within a authorization provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates authorization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific Authorization from the Authorization provider. |
| <CopyableCode code="_list_by_authorization_provider" /> | `EXEC` | <CopyableCode code="authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization providers defined within a authorization provider. |
| <CopyableCode code="confirm_consent_code" /> | `EXEC` | <CopyableCode code="authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId" /> | Confirm valid consent code to suppress Authorizations anti-phishing page. |
