---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - secretmanager
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.secretmanager.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Secret in the format `projects/*/secrets/*`. |
| `ttl` | `string` | Input only. The TTL for the Secret. |
| `versionAliases` | `object` | Optional. Mapping from version alias to version name. A version alias is a string with a maximum length of 63 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore ('_') characters. An alias string must start with a letter and cannot be the string 'latest' or 'NEW'. No more than 50 aliases can be assigned to a given secret. Version-Alias pairs will be viewable via GetSecret and modifiable via UpdateSecret. At launch Access by Allias will only be supported on GetSecretVersion and AccessSecretVersion. |
| `labels` | `object` | The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource. |
| `etag` | `string` | Optional. Etag of the currently stored Secret. |
| `createTime` | `string` | Output only. The time at which the Secret was created. |
| `expireTime` | `string` | Optional. Timestamp in UTC when the Secret is scheduled to expire. This is always provided on output, regardless of what was sent on input. |
| `replication` | `object` | A policy that defines the replication and encryption configuration of data. |
| `topics` | `array` | Optional. A list of up to 10 Pub/Sub topics to which messages are published when control plane operations are called on the secret or its versions. |
| `rotation` | `object` | The rotation time and period for a Secret. At next_rotation_time, Secret Manager will send a Pub/Sub notification to the topics configured on the Secret. Secret.topics must be set to configure rotation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_secrets_get` | `SELECT` | `projectsId, secretsId` | Gets metadata for a given Secret. |
| `projects_secrets_list` | `SELECT` | `projectsId` | Lists Secrets. |
| `projects_secrets_create` | `INSERT` | `projectsId` | Creates a new Secret containing no SecretVersions. |
| `projects_secrets_delete` | `DELETE` | `projectsId, secretsId` | Deletes a Secret. |
| `projects_secrets_patch` | `EXEC` | `projectsId, secretsId` | Updates metadata of an existing Secret. |
