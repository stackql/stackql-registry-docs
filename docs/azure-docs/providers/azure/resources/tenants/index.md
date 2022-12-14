---
title: tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - tenants
  - resources
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
<tr><td><b>Id</b></td><td><code>azure.resources.tenants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID of the tenant. For example, /tenants/00000000-0000-0000-0000-000000000000. |
| `displayName` | `string` | The display name of the tenant. |
| `defaultDomain` | `string` | The default domain for the tenant. |
| `country` | `string` | Country/region name of the address for the tenant. |
| `tenantType` | `string` | The tenant type. Only available for 'Home' tenant category. |
| `domains` | `array` | The list of domains for the tenant. |
| `tenantBrandingLogoUrl` | `string` | The tenant's branding logo URL. Only available for 'Home' tenant category. |
| `tenantCategory` | `string` | Category of the tenant. |
| `countryCode` | `string` | Country/region abbreviation for the tenant. |
| `tenantId` | `string` | The tenant ID. For example, 00000000-0000-0000-0000-000000000000. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tenants_List` | `SELECT` |  | Gets the tenants for your account. |
| `checkResourceName` | `EXEC` | `data__name, data__type` | A resource name is valid if it is not a reserved word, does not contains a reserved word and does not start with a reserved word |
