---
title: service_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - service_registries
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
<tr><td><b>Name</b></td><td><code>service_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.service_registries" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, serviceRegistryName, subscriptionId" /> | Get the Service Registry and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, serviceRegistryName, subscriptionId" /> | Create the default Service Registry or update the existing Service Registry. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, serviceRegistryName, subscriptionId" /> | Disable the default Service Registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
