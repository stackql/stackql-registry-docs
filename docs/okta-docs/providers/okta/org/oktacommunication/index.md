---
title: oktacommunication
hide_title: false
hide_table_of_contents: false
keywords:
  - oktacommunication
  - org
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
<tr><td><b>Name</b></td><td><code>oktacommunication</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.oktacommunication</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `_links` | `object` |
| `optOutEmailUsers` | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subdomain` | Gets Okta Communication Settings of your organization. |
| `optIn` | `EXEC` | `subdomain` | Opts in all users of this org to Okta Communication emails. |
| `optOut` | `EXEC` | `subdomain` | Opts out all users of this org from Okta Communication emails. |
