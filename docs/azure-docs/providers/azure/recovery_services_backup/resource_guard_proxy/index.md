---
title: resource_guard_proxy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guard_proxy
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>resource_guard_proxy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.resource_guard_proxy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="eTag" /> | `string` | Optional ETag. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Returns ResourceGuardProxy under vault and with the name referenced in request |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Delete ResourceGuardProxy under vault |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Add or Update ResourceGuardProxy under vault<br />Secures vault critical operations |
| <CopyableCode code="unlock_delete" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Secures delete ResourceGuardProxy operations. |
