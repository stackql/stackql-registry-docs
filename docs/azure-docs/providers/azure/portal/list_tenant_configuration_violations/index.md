---
title: list_tenant_configuration_violations
hide_title: false
hide_table_of_contents: false
keywords:
  - list_tenant_configuration_violations
  - portal
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
<tr><td><b>Name</b></td><td><code>list_tenant_configuration_violations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.portal.list_tenant_configuration_violations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `array` | The array of violations. |
| `nextLink` | `string` | The URL to use for getting the next set of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ListTenantConfigurationViolations_List` | `SELECT` |  |
