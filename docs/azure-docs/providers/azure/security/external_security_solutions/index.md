---
title: external_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - external_security_solutions
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
<tr><td><b>Name</b></td><td><code>external_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.external_security_solutions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="kind" /> | `string` | The kind of the external solution |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, ascLocation, externalSecuritySolutionsName, resourceGroupName, subscriptionId" /> | Gets a specific external Security Solution. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of external security solutions for the subscription. |
| <CopyableCode code="list_by_home_region" /> | `SELECT` | <CopyableCode code="api-version, ascLocation, subscriptionId" /> | Gets a list of external Security Solutions for the subscription and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of external security solutions for the subscription. |
| <CopyableCode code="_list_by_home_region" /> | `EXEC` | <CopyableCode code="api-version, ascLocation, subscriptionId" /> | Gets a list of external Security Solutions for the subscription and location. |
