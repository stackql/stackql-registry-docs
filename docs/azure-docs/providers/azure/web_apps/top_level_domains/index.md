---
title: top_level_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - top_level_domains
  - web_apps
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
<tr><td><b>Name</b></td><td><code>top_level_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.top_level_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | TopLevelDomain resource specific properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TopLevelDomains_Get` | `SELECT` | `name, subscriptionId` | Description for Get details of a top-level domain. |
| `TopLevelDomains_List` | `SELECT` | `subscriptionId` | Description for Get all top-level domains supported for registration. |
| `TopLevelDomains_ListAgreements` | `EXEC` | `name, subscriptionId` | Description for Gets all legal agreements that user needs to accept before purchasing a domain. |
