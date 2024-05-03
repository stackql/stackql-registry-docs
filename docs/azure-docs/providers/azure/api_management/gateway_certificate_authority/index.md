---
title: gateway_certificate_authority
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_certificate_authority
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
<tr><td><b>Name</b></td><td><code>gateway_certificate_authority</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway_certificate_authority" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Get assigned Gateway Certificate Authority details. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of Certificate Authorities for the specified Gateway entity. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Assign Certificate entity to Gateway entity as Certificate Authority. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Remove relationship between Certificate Authority and Gateway entity. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of Certificate Authorities for the specified Gateway entity. |
