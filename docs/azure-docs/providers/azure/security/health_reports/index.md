---
title: health_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - health_reports
  - security
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
<tr><td><b>Name</b></td><td><code>health_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.health_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Describes properties of the health report |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="healthReportName, resourceId" /> | Get health report of resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of all health reports inside a scope. Valid scopes are: subscription (format: 'subscriptions/&#123;subscriptionId&#125;'), or security connector (format: 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Security/securityConnectors/&#123;securityConnectorName&#125;)' |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> | Get a list of all health reports inside a scope. Valid scopes are: subscription (format: 'subscriptions/&#123;subscriptionId&#125;'), or security connector (format: 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Security/securityConnectors/&#123;securityConnectorName&#125;)' |
