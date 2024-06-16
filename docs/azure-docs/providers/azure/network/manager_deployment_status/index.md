---
title: manager_deployment_status
hide_title: false
hide_table_of_contents: false
keywords:
  - manager_deployment_status
  - network
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
<tr><td><b>Name</b></td><td><code>manager_deployment_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.manager_deployment_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commitTime" /> | `string` | Commit Time. |
| <CopyableCode code="configurationIds" /> | `array` | List of configuration ids. |
| <CopyableCode code="deploymentStatus" /> | `string` | Deployment Status. |
| <CopyableCode code="deploymentType" /> | `string` | Configuration Deployment Type. |
| <CopyableCode code="errorMessage" /> | `string` | Error Message. |
| <CopyableCode code="region" /> | `string` | Region Name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
