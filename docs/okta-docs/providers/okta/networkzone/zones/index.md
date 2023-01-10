---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - networkzone
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.networkzone.zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `asns` | `array` |
| `status` | `string` |
| `created` | `string` |
| `system` | `boolean` |
| `proxies` | `array` |
| `lastUpdated` | `string` |
| `proxyType` | `string` |
| `usage` | `string` |
| `gateways` | `array` |
| `_links` | `object` |
| `locations` | `array` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `zoneId` | Fetches a network zone from your Okta organization by `id`. |
| `list` | `SELECT` |  | Enumerates network zones added to your organization with pagination. A subset of zones can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` |  | Adds a new network zone to your Okta organization. |
| `delete` | `DELETE` | `zoneId` | Removes network zone. |
| `activate` | `EXEC` | `zoneId` | Activate Network Zone |
| `deactivate` | `EXEC` | `zoneId` | Deactivates a network zone. |
| `update` | `EXEC` | `zoneId` | Updates a network zone in your organization. |
