---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - cloudshell
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudshell.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. The environment's identifier, unique among the user's environments. |
| `name` | `string` | Immutable. Full name of this resource, in the format `users/{owner_email}/environments/{environment_id}`. `{owner_email}` is the email address of the user to whom this environment belongs, and `{environment_id}` is the identifier of this environment. For example, `users/someone@example.com/environments/default`. |
| `sshHost` | `string` | Output only. Host to which clients can connect to initiate SSH sessions with the environment. |
| `publicKeys` | `array` | Output only. Public keys associated with the environment. Clients can connect to this environment via SSH only if they possess a private key corresponding to at least one of these public keys. Keys can be added to or removed from the environment using the AddPublicKey and RemovePublicKey methods. |
| `sshPort` | `integer` | Output only. Port to which clients can connect to initiate SSH sessions with the environment. |
| `dockerImage` | `string` | Required. Immutable. Full path to the Docker image used to run this environment, e.g. "gcr.io/dev-con/cloud-devshell:latest". |
| `webHost` | `string` | Output only. Host to which clients can connect to initiate HTTPS or WSS connections with the environment. |
| `sshUsername` | `string` | Output only. Username that clients should use when initiating SSH sessions with the environment. |
| `state` | `string` | Output only. Current execution state of this environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_environments_get` | `SELECT` | `environmentsId, usersId` | Gets an environment. Returns NOT_FOUND if the environment does not exist. |
| `users_environments_authorize` | `EXEC` | `environmentsId, usersId` | Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate. |
| `users_environments_start` | `EXEC` | `environmentsId, usersId` | Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field. |
