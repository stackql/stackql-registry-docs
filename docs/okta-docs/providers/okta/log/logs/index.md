---
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
  - log
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
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.log.logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `uuid` | `string` |
| `eventType` | `string` |
| `published` | `string` |
| `target` | `array` |
| `outcome` | `object` |
| `debugContext` | `object` |
| `securityContext` | `object` |
| `severity` | `string` |
| `transaction` | `object` |
| `authenticationContext` | `object` |
| `actor` | `object` |
| `client` | `object` |
| `request` | `object` |
| `version` | `string` |
| `displayMessage` | `string` |
| `legacyEventType` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `subdomain` |
