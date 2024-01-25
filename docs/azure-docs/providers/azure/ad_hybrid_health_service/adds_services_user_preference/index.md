---
title: adds_services_user_preference
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_user_preference
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>adds_services_user_preference</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.adds_services_user_preference</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `featureName, serviceName` | Gets the user preferences for a given feature. |
| `add` | `INSERT` | `featureName, serviceName` | Adds the user preferences for a given feature. |
| `delete` | `DELETE` | `featureName, serviceName` | Deletes the user preferences for a given feature. |
