---
title: domain_registration_provider_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_registration_provider_operations
  - app_service
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
<tr><td><b>Name</b></td><td><code>domain_registration_provider_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.domain_registration_provider_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `display` | `object` | Meta data about operation used for display in portal. |
| `isDataAction` | `boolean` |  |
| `origin` | `string` |  |
| `properties` | `object` | Properties available for a Microsoft.Web resource provider operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
