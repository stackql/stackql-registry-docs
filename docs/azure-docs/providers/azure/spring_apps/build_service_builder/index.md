---
title: build_service_builder
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_builder
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>build_service_builder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_builder" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Get a KPack builder. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | List KPack builders result. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a KPack builder. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId" /> | Delete a KPack builder. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | List KPack builders result. |
