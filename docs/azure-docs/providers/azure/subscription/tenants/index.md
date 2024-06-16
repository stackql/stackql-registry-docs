---
title: tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - tenants
  - subscription
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
<tr><td><b>Name</b></td><td><code>tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.tenants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID of the tenant. For example, /tenants/00000000-0000-0000-0000-000000000000. |
| <CopyableCode code="country" /> | `string` | The country/region name of the address for the tenant. |
| <CopyableCode code="countryCode" /> | `string` | The Country/region abbreviation for the tenant. |
| <CopyableCode code="defaultDomain" /> | `string` | The default domain for the tenant. |
| <CopyableCode code="displayName" /> | `string` | The display name of the tenant. |
| <CopyableCode code="domains" /> | `string` | The list of domains for the tenant. |
| <CopyableCode code="tenantCategory" /> | `string` | The category of the tenant. Possible values are TenantCategoryHome,TenantCategoryProjectedBy,TenantCategoryManagedBy |
| <CopyableCode code="tenantId" /> | `string` | The tenant ID. For example, 00000000-0000-0000-0000-000000000000. |
| <CopyableCode code="tenantType" /> | `string` | The tenant type. Only available for Home tenant category. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
