---
title: apms
hide_title: false
hide_table_of_contents: false
keywords:
  - apms
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
<tr><td><b>Name</b></td><td><code>apms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.apms" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | Get the APM by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get collection of APMs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | Create or update an APM. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete an APM |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get collection of APMs. |
