---
title: monitors_app_services
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_app_services
  - newrelic
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_app_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelic.monitors_app_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agentStatus" /> | `string` | Status of the NewRelic agent installed on the App service. |
| <CopyableCode code="agentVersion" /> | `string` | Version of the NewRelic agent installed on the App service. |
| <CopyableCode code="azureResourceId" /> | `string` | Azure App service resource ID |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__userEmail" /> |
