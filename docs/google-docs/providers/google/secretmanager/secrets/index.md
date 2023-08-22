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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `replication` | `object` | A policy that defines the replication and encryption configuration of data. |
| `topics` | `array` | Optional. A list of up to 10 Pub/Sub topics to which messages are published when control plane operations are called on the secret or its versions. |
| `createTime` | `string` | Output only. The time at which the Secret was created. |
| `ttl` | `string` | Input only. The TTL for the Secret. |
| `expireTime` | `string` | Optional. Timestamp in UTC when the Secret is scheduled to expire. This is always provided on output, regardless of what was sent on input. |
| `annotations` | `object` | Optional. Custom metadata about the secret. Annotations are distinct from various forms of labels. Annotations exist to allow client tools to store their own state information without requiring a database. Annotation keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, begin and end with an alphanumeric character ([a-z0-9A-Z]), and may have dashes (-), underscores (_), dots (.), and alphanumerics in between these symbols. The total size of annotation keys and values must be less than 16KiB. |
| `labels` | `object` | The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p&#123;Ll&#125;\p&#123;Lo&#125;&#123;0,62&#125;` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p&#123;Ll&#125;\p&#123;Lo&#125;\p&#123;N&#125;_-]&#123;0,63&#125;` No more than 64 labels can be assigned to a given resource. |
| `versionAliases` | `object` | Optional. Mapping from version alias to version name. A version alias is a string with a maximum length of 63 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore ('_') characters. An alias string must start with a letter and cannot be the string 'latest' or 'NEW'. No more than 50 aliases can be assigned to a given secret. Version-Alias pairs will be viewable via GetSecret and modifiable via UpdateSecret. At launch Access by Allias will only be supported on GetSecretVersion and AccessSecretVersion. |
| `etag` | `string` | Optional. Etag of the currently stored Secret. |
| `rotation` | `object` | The rotation time and period for a Secret. At next_rotation_time, Secret Manager will send a Pub/Sub notification to the topics configured on the Secret. Secret.topics must be set to configure rotation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, secretsId` | Gets metadata for a given Secret. |
| `list` | `SELECT` | `projectsId` | Lists Secrets. |
| `create` | `INSERT` | `projectsId` | Creates a new Secret containing no SecretVersions. |
| `delete` | `DELETE` | `projectsId, secretsId` | Deletes a Secret. |
| `_list` | `EXEC` | `projectsId` | Lists Secrets. |
| `patch` | `EXEC` | `projectsId, secretsId` | Updates metadata of an existing Secret. |
