---
title: log_analytics_log_analytics_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_resources
  - cdn
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
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.log_analytics_log_analytics_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `customDomains` | `array` |
| `endpoints` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `profileName, resourceGroupName, subscriptionId` |
