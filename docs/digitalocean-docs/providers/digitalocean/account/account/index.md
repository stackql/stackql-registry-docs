---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - account
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.account.account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `floating_ip_limit` | `integer` | The total number of Floating IPs the current user or team may have. |
| `status` | `string` | This value is one of "active", "warning" or "locked". |
| `status_message` | `string` | A human-readable message giving more details about the status of the account. |
| `team` | `object` | When authorized in a team context, includes information about the current team. |
| `uuid` | `string` | The unique universal identifier for the current user. |
| `droplet_limit` | `integer` | The total number of Droplets current user or team may have active at one time. |
| `email` | `string` | The email address used by the current user to register for DigitalOcean. |
| `email_verified` | `boolean` | If true, the user has verified their account via email. False otherwise. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` |  |
| `_get` | `EXEC` |  |
