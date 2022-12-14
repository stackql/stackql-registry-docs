---
title: cognitive_services_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - cognitive_services_accounts
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>cognitive_services_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.cognitive_services_accounts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CheckDomainAvailability` | `EXEC` | `subscriptionId, data__subdomainName, data__type` | Check whether a domain is available. |
| `CheckSkuAvailability` | `EXEC` | `location, subscriptionId, data__kind, data__skus, data__type` | Check available SKUs. |
