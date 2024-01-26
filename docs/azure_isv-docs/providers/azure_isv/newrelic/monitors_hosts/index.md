---
title: monitors_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_hosts
  - newrelic
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.newrelic.monitors_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The link to the next page of items |
| `value` | `array` | The VMInfo items on this page |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId, data__userEmail` |
