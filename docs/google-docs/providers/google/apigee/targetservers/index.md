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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>targetservers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.targetservers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource id of this target server. Values must match the regular expression  |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description of this TargetServer. |
| <CopyableCode code="host" /> | `string` | Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123. |
| <CopyableCode code="isEnabled" /> | `boolean` | Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true. |
| <CopyableCode code="port" /> | `integer` | Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive. |
| <CopyableCode code="protocol" /> | `string` | Immutable. The protocol used by this TargetServer. |
| <CopyableCode code="sSLInfo" /> | `object` | TLS configuration information for virtual hosts and TargetServers. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_targetservers_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, targetserversId" /> | Gets a TargetServer resource. |
| <CopyableCode code="organizations_environments_targetservers_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a TargetServer in the specified environment. |
| <CopyableCode code="organizations_environments_targetservers_delete" /> | `DELETE` | <CopyableCode code="environmentsId, organizationsId, targetserversId" /> | Deletes a TargetServer from an environment. Returns the deleted TargetServer resource. |
| <CopyableCode code="organizations_environments_targetservers_update" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, targetserversId" /> | Updates an existing TargetServer. Note that this operation has PUT semantics; it will replace the entirety of the existing TargetServer with the resource in the request body. |
