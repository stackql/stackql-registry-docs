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
| `published` | `string` |
| `legacyEventType` | `string` |
| `displayMessage` | `string` |
| `actor` | `object` |
| `client` | `object` |
| `authenticationContext` | `object` |
| `target` | `array` |
| `request` | `object` |
| `debugContext` | `object` |
| `uuid` | `string` |
| `eventType` | `string` |
| `outcome` | `object` |
| `version` | `string` |
| `transaction` | `object` |
| `severity` | `string` |
| `securityContext` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
