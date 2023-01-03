---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `conditions` | `object` |
| `priority` | `integer` |
| `actions` | `object` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `type` | `string` |
| `system` | `boolean` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authServerId, policyId, ruleId` | Returns a Policy Rule by ID that is defined in the specified Custom Authorization Server and Policy. |
| `list` | `SELECT` | `authServerId, policyId` | Enumerates all policy rules for the specified Custom Authorization Server and Policy. |
| `insert` | `INSERT` | `authServerId, policyId` | Creates a policy rule for the specified Custom Authorization Server and Policy. |
| `delete` | `DELETE` | `authServerId, policyId, ruleId` | Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy. |
| `activate` | `EXEC` | `authServerId, policyId, ruleId` | Activate Authorization Server Policy Rule |
| `deactivate` | `EXEC` | `authServerId, policyId, ruleId` | Deactivate Authorization Server Policy Rule |
| `update` | `EXEC` | `authServerId, policyId, ruleId` | Updates the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy. |
