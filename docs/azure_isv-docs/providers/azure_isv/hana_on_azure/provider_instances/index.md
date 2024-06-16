---
title: provider_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_instances
  - hana_on_azure
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
<tr><td><b>Name</b></td><td><code>provider_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.hana_on_azure.provider_instances" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapMonitorName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId" /> |
