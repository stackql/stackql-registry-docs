---
title: business_process_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - business_process_versions
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>business_process_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.business_process_versions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, businessProcessName, businessProcessVersion, resourceGroupName, spaceName, subscriptionId" /> | Get a BusinessProcessVersion |
| <CopyableCode code="list_by_business_process" /> | `SELECT` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | List BusinessProcessVersion resources by BusinessProcess |
| <CopyableCode code="_list_by_business_process" /> | `EXEC` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | List BusinessProcessVersion resources by BusinessProcess |
