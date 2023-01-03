---
title: targetservers
hide_title: false
hide_table_of_contents: false
keywords:
  - targetservers
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>targetservers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.targetservers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource id of this target server. Values must match the regular expression  |
| `description` | `string` | Optional. A human-readable description of this TargetServer. |
| `sSLInfo` | `object` | TLS configuration information for virtual hosts and TargetServers. |
| `host` | `string` | Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123. |
| `isEnabled` | `boolean` | Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true. |
| `port` | `integer` | Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive. |
| `protocol` | `string` | Immutable. The protocol used by this TargetServer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_targetservers_get` | `SELECT` | `environmentsId, organizationsId, targetserversId` | Gets a TargetServer resource. |
| `organizations_environments_targetservers_create` | `INSERT` | `environmentsId, organizationsId` | Creates a TargetServer in the specified environment. |
| `organizations_environments_targetservers_delete` | `DELETE` | `environmentsId, organizationsId, targetserversId` | Deletes a TargetServer from an environment. Returns the deleted TargetServer resource. |
| `organizations_environments_targetservers_update` | `EXEC` | `environmentsId, organizationsId, targetserversId` | Updates an existing TargetServer. Note that this operation has PUT semantics; it will replace the entirety of the existing TargetServer with the resource in the request body. |
