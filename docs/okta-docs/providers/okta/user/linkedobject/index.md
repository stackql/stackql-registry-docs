---
title: linkedobject
hide_title: false
hide_table_of_contents: false
keywords:
  - linkedobject
  - user
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
<tr><td><b>Name</b></td><td><code>linkedobject</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.linkedobject</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete` | `DELETE` | `relationshipName, userId, subdomain` | Delete linked objects for a user, relationshipName can be ONLY a primary relationship name |
| `update` | `EXEC` | `associatedUserId, primaryRelationshipName, primaryUserId, subdomain` |  |
