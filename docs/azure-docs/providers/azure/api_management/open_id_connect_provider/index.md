---
title: open_id_connect_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - open_id_connect_provider
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
<tr><td><b>Name</b></td><td><code>open_id_connect_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.open_id_connect_provider" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="opid, resourceGroupName, serviceName, subscriptionId" /> | Gets specific OpenID Connect Provider without secrets. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists of all the OpenId Connect Providers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="opid, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates the OpenID Connect Provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, opid, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific OpenID Connect Provider of the API Management service instance. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists of all the OpenId Connect Providers. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, opid, resourceGroupName, serviceName, subscriptionId" /> | Updates the specific OpenID Connect Provider. |
