---
title: customized_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - customized_accelerators
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
<tr><td><b>Name</b></td><td><code>customized_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.customized_accelerators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Customized accelerator properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Get the customized accelerator. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all customized accelerators. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Create or update the customized accelerator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Delete the customized accelerator. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all customized accelerators. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId, data__gitRepository" /> | Check the customized accelerator are valid. |
