---
title: predefined_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - predefined_accelerators
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
<tr><td><b>Name</b></td><td><code>predefined_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.predefined_accelerators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Predefined accelerator properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Get the predefined accelerator. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all predefined accelerators. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all predefined accelerators. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Disable predefined accelerator. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Enable predefined accelerator. |
