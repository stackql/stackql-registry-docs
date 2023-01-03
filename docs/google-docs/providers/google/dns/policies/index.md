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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the resource; defined by the server (output only). |
| `name` | `string` | User-assigned name for this policy. |
| `description` | `string` | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the policy's function. |
| `alternativeNameServerConfig` | `object` |  |
| `enableInboundForwarding` | `boolean` | Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address is allocated from each of the subnetworks that are bound to this policy. |
| `enableLogging` | `boolean` | Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set. |
| `kind` | `string` |  |
| `networks` | `array` | List of network names specifying networks to which this policy is applied. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policy, project` | Fetches the representation of an existing Policy. |
| `list` | `SELECT` | `project` | Enumerates all Policies associated with a project. |
| `create` | `INSERT` | `project` | Creates a new Policy. |
| `delete` | `DELETE` | `policy, project` | Deletes a previously created Policy. Fails if the policy is still being referenced by a network. |
| `patch` | `EXEC` | `policy, project` | Applies a partial update to an existing Policy. |
| `update` | `EXEC` | `policy, project` | Updates an existing Policy. |
