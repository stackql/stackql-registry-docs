---
title: bitbucket_server_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - bitbucket_server_configs
  - cloudbuild
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
<tr><td><b>Name</b></td><td><code>bitbucket_server_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.bitbucket_server_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the config. |
| `sslCa` | `string` | Optional. SSL certificate to use for requests to Bitbucket Server. The format should be PEM format but the extension can be one of .pem, .cer, or .crt. |
| `hostUri` | `string` | Required. Immutable. The URI of the Bitbucket Server host. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig. |
| `peeredNetwork` | `string` | Optional. The network to be used when reaching out to the Bitbucket Server instance. The VPC network must be enabled for private service connection. This should be set if the Bitbucket Server instance is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the Bitbucket Server instance will be made over the public internet. Must be in the format `projects/&#123;project&#125;/global/networks/&#123;network&#125;`, where &#123;project&#125; is a project number or id and &#123;network&#125; is the name of a VPC network in the project. |
| `username` | `string` | Username of the account Cloud Build will use on Bitbucket Server. |
| `webhookKey` | `string` | Output only. UUID included in webhook requests. The UUID is used to look up the corresponding config. |
| `createTime` | `string` | Time when the config was created. |
| `secrets` | `object` | BitbucketServerSecrets represents the secrets in Secret Manager for a Bitbucket Server. |
| `connectedRepositories` | `array` | Output only. Connected Bitbucket Server repositories for this config. |
| `apiKey` | `string` | Required. Immutable. API Key that will be attached to webhook. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bitbucketServerConfigs_get` | `SELECT` | `bitbucketServerConfigsId, locationsId, projectsId` | Retrieve a `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_bitbucketServerConfigs_list` | `SELECT` | `locationsId, projectsId` | List all `BitbucketServerConfigs` for a given project. This API is experimental. |
| `projects_locations_bitbucketServerConfigs_create` | `INSERT` | `locationsId, projectsId` | Creates a new `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_bitbucketServerConfigs_delete` | `DELETE` | `bitbucketServerConfigsId, locationsId, projectsId` | Delete a `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_bitbucketServerConfigs_patch` | `EXEC` | `bitbucketServerConfigsId, locationsId, projectsId` | Updates an existing `BitbucketServerConfig`. This API is experimental. |
