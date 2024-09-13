
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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudshell.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The environment's identifier, unique among the user's environments. |
| <CopyableCode code="name" /> | `string` | Immutable. Full name of this resource, in the format `users/{owner_email}/environments/{environment_id}`. `{owner_email}` is the email address of the user to whom this environment belongs, and `{environment_id}` is the identifier of this environment. For example, `users/someone@example.com/environments/default`. |
| <CopyableCode code="dockerImage" /> | `string` | Required. Immutable. Full path to the Docker image used to run this environment, e.g. "gcr.io/dev-con/cloud-devshell:latest". |
| <CopyableCode code="publicKeys" /> | `array` | Output only. Public keys associated with the environment. Clients can connect to this environment via SSH only if they possess a private key corresponding to at least one of these public keys. Keys can be added to or removed from the environment using the AddPublicKey and RemovePublicKey methods. |
| <CopyableCode code="sshHost" /> | `string` | Output only. Host to which clients can connect to initiate SSH sessions with the environment. |
| <CopyableCode code="sshPort" /> | `integer` | Output only. Port to which clients can connect to initiate SSH sessions with the environment. |
| <CopyableCode code="sshUsername" /> | `string` | Output only. Username that clients should use when initiating SSH sessions with the environment. |
| <CopyableCode code="state" /> | `string` | Output only. Current execution state of this environment. |
| <CopyableCode code="webHost" /> | `string` | Output only. Host to which clients can connect to initiate HTTPS or WSS connections with the environment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentsId, usersId" /> | Gets an environment. Returns NOT_FOUND if the environment does not exist. |
| <CopyableCode code="authorize" /> | `EXEC` | <CopyableCode code="environmentsId, usersId" /> | Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="environmentsId, usersId" /> | Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field. |

## `SELECT` examples

Gets an environment. Returns NOT_FOUND if the environment does not exist.

```sql
SELECT
id,
name,
dockerImage,
publicKeys,
sshHost,
sshPort,
sshUsername,
state,
webHost
FROM google.cloudshell.environments
WHERE environmentsId = '{{ environmentsId }}'
AND usersId = '{{ usersId }}'; 
```
