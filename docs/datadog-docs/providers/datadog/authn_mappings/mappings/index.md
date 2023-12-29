---
title: mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - mappings
  - authn_mappings
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.authn_mappings.mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the AuthN Mapping. |
| `attributes` | `object` | Attributes of AuthN Mapping. |
| `relationships` | `object` | All relationships associated with AuthN Mapping. |
| `type` | `string` | AuthN Mappings resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getauthn_mapping` | `SELECT` | `authn_mapping_id, dd_site` | Get an AuthN Mapping specified by the AuthN Mapping UUID. |
| `listauthn_mappings` | `SELECT` | `dd_site` | List all AuthN Mappings in the org. |
| `createauthn_mapping` | `INSERT` | `data__data, dd_site` | Create an AuthN Mapping. |
| `deleteauthn_mapping` | `DELETE` | `authn_mapping_id, dd_site` | Delete an AuthN Mapping specified by AuthN Mapping UUID. |
| `_getauthn_mapping` | `EXEC` | `authn_mapping_id, dd_site` | Get an AuthN Mapping specified by the AuthN Mapping UUID. |
| `_listauthn_mappings` | `EXEC` | `dd_site` | List all AuthN Mappings in the org. |
| `updateauthn_mapping` | `EXEC` | `authn_mapping_id, data__data, dd_site` | Edit an AuthN Mapping. |
