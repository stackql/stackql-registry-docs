---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - bot_service
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
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource |
| <CopyableCode code="name" /> | `string` | Name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of Network Security Perimeter configuration |
| <CopyableCode code="type" /> | `string` | Type of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkSecurityPerimeterConfigurationName, resourceGroupName, resourceName, subscriptionId" /> | Gets the specified Network Security Perimeter configuration associated with the Bot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List Network Security Perimeter configurations associated with the Bot. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List Network Security Perimeter configurations associated with the Bot. |
| <CopyableCode code="reconcile" /> | `EXEC` | <CopyableCode code="networkSecurityPerimeterConfigurationName, resourceGroupName, resourceName, subscriptionId" /> | Reconcile the specified Network Security Perimeter configuration associated with the Bot. |
