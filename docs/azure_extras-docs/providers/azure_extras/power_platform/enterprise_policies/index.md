---
title: enterprise_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_policies
  - power_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>enterprise_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.power_platform.enterprise_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity of the EnterprisePolicy. |
| <CopyableCode code="kind" /> | `string` | The Kind (type) of Enterprise Policy |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties that define configuration for the enterprise policy. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId" /> | Get information about an EnterprisePolicy |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve a list of EnterprisePolicies within a given resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve a list of EnterprisePolicies within a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId, data__kind" /> | Creates an EnterprisePolicy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId" /> | Delete an EnterprisePolicy |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId" /> | Updates an EnterprisePolicy |
