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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bitbucket_server_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.bitbucket_server_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the config. |
| <CopyableCode code="apiKey" /> | `string` | Required. Immutable. API Key that will be attached to webhook. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig. |
| <CopyableCode code="connectedRepositories" /> | `array` | Output only. Connected Bitbucket Server repositories for this config. |
| <CopyableCode code="createTime" /> | `string` | Time when the config was created. |
| <CopyableCode code="hostUri" /> | `string` | Required. Immutable. The URI of the Bitbucket Server host. Once this field has been set, it cannot be changed. If you need to change it, please create another BitbucketServerConfig. |
| <CopyableCode code="peeredNetwork" /> | `string` | Optional. The network to be used when reaching out to the Bitbucket Server instance. The VPC network must be enabled for private service connection. This should be set if the Bitbucket Server instance is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the Bitbucket Server instance will be made over the public internet. Must be in the format `projects/&#123;project&#125;/global/networks/&#123;network&#125;`, where &#123;project&#125; is a project number or id and &#123;network&#125; is the name of a VPC network in the project. |
| <CopyableCode code="secrets" /> | `object` | BitbucketServerSecrets represents the secrets in Secret Manager for a Bitbucket Server. |
| <CopyableCode code="sslCa" /> | `string` | Optional. SSL certificate to use for requests to Bitbucket Server. The format should be PEM format but the extension can be one of .pem, .cer, or .crt. |
| <CopyableCode code="username" /> | `string` | Username of the account Cloud Build will use on Bitbucket Server. |
| <CopyableCode code="webhookKey" /> | `string` | Output only. UUID included in webhook requests. The UUID is used to look up the corresponding config. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_bitbucket_server_configs_get" /> | `SELECT` | <CopyableCode code="bitbucketServerConfigsId, locationsId, projectsId" /> | Retrieve a `BitbucketServerConfig`. This API is experimental. |
| <CopyableCode code="projects_locations_bitbucket_server_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all `BitbucketServerConfigs` for a given project. This API is experimental. |
| <CopyableCode code="projects_locations_bitbucket_server_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new `BitbucketServerConfig`. This API is experimental. |
| <CopyableCode code="projects_locations_bitbucket_server_configs_delete" /> | `DELETE` | <CopyableCode code="bitbucketServerConfigsId, locationsId, projectsId" /> | Delete a `BitbucketServerConfig`. This API is experimental. |
| <CopyableCode code="_projects_locations_bitbucket_server_configs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List all `BitbucketServerConfigs` for a given project. This API is experimental. |
| <CopyableCode code="projects_locations_bitbucket_server_configs_patch" /> | `EXEC` | <CopyableCode code="bitbucketServerConfigsId, locationsId, projectsId" /> | Updates an existing `BitbucketServerConfig`. This API is experimental. |
