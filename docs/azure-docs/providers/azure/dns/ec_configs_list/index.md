---
title: ec_configs_list
hide_title: false
hide_table_of_contents: false
keywords:
  - ec_configs_list
  - dns
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
<tr><td><b>Name</b></td><td><code>ec_configs_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns.ec_configs_list</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the DNSSEC configuration. |
| `name` | `string` | The name of the DNSSEC configuration. |
| `etag` | `string` | The etag of the DNSSEC configuration. |
| `properties` | `object` | Represents the DNSSEC properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the DNSSEC configuration. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_dns_zone` | `SELECT` | `resourceGroupName, subscriptionId, zoneName` |
| `_list_by_dns_zone` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` |
