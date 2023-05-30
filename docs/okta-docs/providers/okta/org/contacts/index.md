---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.contacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `_links` | `object` |
| `contactType` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contactType, subdomain` | Retrieves the URL of the User associated with the specified Contact Type. |
| `list` | `SELECT` | `subdomain` | Gets Contact Types of your organization. |
| `update` | `EXEC` | `contactType, subdomain` | Updates the User associated with the specified Contact Type. |
