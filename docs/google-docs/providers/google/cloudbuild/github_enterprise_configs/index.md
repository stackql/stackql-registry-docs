---
title: github_enterprise_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - github_enterprise_configs
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
<tr><td><b>Name</b></td><td><code>github_enterprise_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.github_enterprise_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. The full resource name for the GitHubEnterpriseConfig For example: "projects/&#123;$project_id&#125;/locations/&#123;$location_id&#125;/githubEnterpriseConfigs/&#123;$config_id&#125;" |
| `createTime` | `string` | Output only. Time when the installation was associated with the project. |
| `hostUrl` | `string` | The URL of the github enterprise host the configuration is for. |
| `appId` | `string` | Required. The GitHub app id of the Cloud Build app on the GitHub Enterprise server. |
| `peeredNetwork` | `string` | Optional. The network to be used when reaching out to the GitHub Enterprise server. The VPC network must be enabled for private service connection. This should be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the GitHub Enterprise server will be made over the public internet. Must be in the format `projects/&#123;project&#125;/global/networks/&#123;network&#125;`, where &#123;project&#125; is a project number or id and &#123;network&#125; is the name of a VPC network in the project. |
| `secrets` | `object` | GitHubEnterpriseSecrets represents the names of all necessary secrets in Secret Manager for a GitHub Enterprise server. Format is: projects//secrets/. |
| `webhookKey` | `string` | The key that should be attached to webhook calls to the ReceiveWebhook endpoint. |
| `sslCa` | `string` | Optional. SSL certificate to use for requests to GitHub Enterprise. |
| `displayName` | `string` | Name to display for this config. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_github_enterprise_configs_get` | `SELECT` | `githubEnterpriseConfigsId, projectsId` | Retrieve a GitHubEnterpriseConfig. |
| `projects_github_enterprise_configs_list` | `SELECT` | `projectsId` | List all GitHubEnterpriseConfigs for a given project. |
| `projects_locations_github_enterprise_configs_get` | `SELECT` | `githubEnterpriseConfigsId, locationsId, projectsId` | Retrieve a GitHubEnterpriseConfig. |
| `projects_locations_github_enterprise_configs_list` | `SELECT` | `locationsId, projectsId` | List all GitHubEnterpriseConfigs for a given project. |
| `projects_github_enterprise_configs_create` | `INSERT` | `projectsId` | Create an association between a GCP project and a GitHub Enterprise server. |
| `projects_locations_github_enterprise_configs_create` | `INSERT` | `locationsId, projectsId` | Create an association between a GCP project and a GitHub Enterprise server. |
| `projects_github_enterprise_configs_delete` | `DELETE` | `githubEnterpriseConfigsId, projectsId` | Delete an association between a GCP project and a GitHub Enterprise server. |
| `projects_locations_github_enterprise_configs_delete` | `DELETE` | `githubEnterpriseConfigsId, locationsId, projectsId` | Delete an association between a GCP project and a GitHub Enterprise server. |
| `projects_github_enterprise_configs_patch` | `EXEC` | `githubEnterpriseConfigsId, projectsId` | Update an association between a GCP project and a GitHub Enterprise server. |
| `projects_locations_github_enterprise_configs_patch` | `EXEC` | `githubEnterpriseConfigsId, locationsId, projectsId` | Update an association between a GCP project and a GitHub Enterprise server. |
