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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscription.tenants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID of the tenant. For example, /tenants/00000000-0000-0000-0000-000000000000. |
| `domains` | `string` | The list of domains for the tenant. |
| `countryCode` | `string` | The Country/region abbreviation for the tenant. |
| `tenantCategory` | `string` | The category of the tenant. Possible values are TenantCategoryHome,TenantCategoryProjectedBy,TenantCategoryManagedBy |
| `tenantId` | `string` | The tenant ID. For example, 00000000-0000-0000-0000-000000000000. |
| `tenantType` | `string` | The tenant type. Only available for Home tenant category. |
| `displayName` | `string` | The display name of the tenant. |
| `country` | `string` | The country/region name of the address for the tenant. |
| `defaultDomain` | `string` | The default domain for the tenant. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Tenants_List` | `SELECT` |  |
