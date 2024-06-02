---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - dns
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dns.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the resource; defined by the server (output only). |
| <CopyableCode code="name" /> | `string` | User-assigned name for this policy. |
| <CopyableCode code="description" /> | `string` | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the policy's function. |
| <CopyableCode code="alternativeNameServerConfig" /> | `object` |  |
| <CopyableCode code="enableInboundForwarding" /> | `boolean` | Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address is allocated from each of the subnetworks that are bound to this policy. |
| <CopyableCode code="enableLogging" /> | `boolean` | Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="networks" /> | `array` | List of network names specifying networks to which this policy is applied. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policy, project" /> | Fetches the representation of an existing Policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Enumerates all Policies associated with a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="project" /> | Creates a new Policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policy, project" /> | Deletes a previously created Policy. Fails if the policy is still being referenced by a network. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="project" /> | Enumerates all Policies associated with a project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="policy, project" /> | Applies a partial update to an existing Policy. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="policy, project" /> | Updates an existing Policy. |
