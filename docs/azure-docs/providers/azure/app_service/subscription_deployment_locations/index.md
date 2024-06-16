---
title: subscription_deployment_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_deployment_locations
  - app_service
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
<tr><td><b>Name</b></td><td><code>subscription_deployment_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.subscription_deployment_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="hostingEnvironmentDeploymentInfos" /> | `array` | Available App Service Environments with basic information. |
| <CopyableCode code="hostingEnvironments" /> | `array` | Available App Service Environments with full descriptions of the environments. |
| <CopyableCode code="locations" /> | `array` | Available regions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
