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
| `totalSize` | `integer` | The total number of SecretVersions but 0 when the ListSecretsRequest.filter field is set. |
| `versions` | `array` | The list of SecretVersions sorted in reverse by create_time (newest first). |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in ListSecretVersionsRequest.page_token to retrieve the next page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, secretsId, versionsId` | Gets metadata for a SecretVersion. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion. |
| `list` | `SELECT` | `projectsId, secretsId` | Lists SecretVersions. This call does not return secret data. |
| `access` | `EXEC` | `projectsId, secretsId, versionsId` | Accesses a SecretVersion. This call returns the secret data. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion. |
| `destroy` | `EXEC` | `projectsId, secretsId, versionsId` | Destroys a SecretVersion. Sets the state of the SecretVersion to DESTROYED and irrevocably destroys the secret data. |
| `disable` | `EXEC` | `projectsId, secretsId, versionsId` | Disables a SecretVersion. Sets the state of the SecretVersion to DISABLED. |
| `enable` | `EXEC` | `projectsId, secretsId, versionsId` | Enables a SecretVersion. Sets the state of the SecretVersion to ENABLED. |
