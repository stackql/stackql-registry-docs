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
| `gateways` | `array` |
| `_links` | `object` |
| `proxies` | `array` |
| `locations` | `array` |
| `status` | `string` |
| `system` | `boolean` |
| `type` | `string` |
| `asns` | `array` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `usage` | `string` |
| `proxyType` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `zoneId, subdomain` | Fetches a network zone from your Okta organization by `id`. |
| `list` | `SELECT` | `subdomain` | Enumerates network zones added to your organization with pagination. A subset of zones can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` | `subdomain` | Adds a new network zone to your Okta organization. |
| `delete` | `DELETE` | `zoneId, subdomain` | Removes network zone. |
| `activate` | `EXEC` | `zoneId, subdomain` | Activate Network Zone |
| `deactivate` | `EXEC` | `zoneId, subdomain` | Deactivates a network zone. |
| `update` | `EXEC` | `zoneId, subdomain` | Updates a network zone in your organization. |
