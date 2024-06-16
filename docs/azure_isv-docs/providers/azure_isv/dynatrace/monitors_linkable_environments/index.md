---
title: monitors_linkable_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_linkable_environments
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>monitors_linkable_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_linkable_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="environmentId" /> | `string` | environment id for which user is an admin |
| <CopyableCode code="environmentName" /> | `string` | Name of the environment |
| <CopyableCode code="planData" /> | `object` | Billing plan information. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__region, data__tenantId, data__userPrincipal" /> |
