---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - secretmanager
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.secretmanager.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the SecretVersion in the format `projects/*/secrets/*/versions/*`. SecretVersion IDs in a Secret start at 1 and are incremented for each subsequent version of the secret. |
| `replicationStatus` | `object` | The replication status of a SecretVersion. |
| `state` | `string` | Output only. The current state of the SecretVersion. |
| `clientSpecifiedPayloadChecksum` | `boolean` | Output only. True if payload checksum specified in SecretPayload object has been received by SecretManagerService on SecretManagerService.AddSecretVersion. |
| `createTime` | `string` | Output only. The time at which the SecretVersion was created. |
| `destroyTime` | `string` | Output only. The time this SecretVersion was destroyed. Only present if state is DESTROYED. |
| `etag` | `string` | Output only. Etag of the currently stored SecretVersion. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, secretsId, versionsId` | Gets metadata for a SecretVersion. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion. |
| `list` | `SELECT` | `projectsId, secretsId` | Lists SecretVersions. This call does not return secret data. |
| `_list` | `EXEC` | `projectsId, secretsId` | Lists SecretVersions. This call does not return secret data. |
| `access` | `EXEC` | `projectsId, secretsId, versionsId` | Accesses a SecretVersion. This call returns the secret data. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion. |
| `destroy` | `EXEC` | `projectsId, secretsId, versionsId` | Destroys a SecretVersion. Sets the state of the SecretVersion to DESTROYED and irrevocably destroys the secret data. |
| `disable` | `EXEC` | `projectsId, secretsId, versionsId` | Disables a SecretVersion. Sets the state of the SecretVersion to DISABLED. |
| `enable` | `EXEC` | `projectsId, secretsId, versionsId` | Enables a SecretVersion. Sets the state of the SecretVersion to ENABLED. |
