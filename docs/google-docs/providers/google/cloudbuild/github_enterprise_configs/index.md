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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Optional. The full resource name for the GitHubEnterpriseConfig For example: "projects/{$project_id}/githubEnterpriseConfigs/{$config_id}" |
| `webhookKey` | `string` | The key that should be attached to webhook calls to the ReceiveWebhook endpoint. |
| `sslCa` | `string` | Optional. SSL certificate to use for requests to GitHub Enterprise. |
| `secrets` | `object` | GitHubEnterpriseSecrets represents the names of all necessary secrets in Secret Manager for a GitHub Enterprise server. Format is: projects//secrets/. |
| `hostUrl` | `string` | The URL of the github enterprise host the configuration is for. |
| `appId` | `string` | Required. The GitHub app id of the Cloud Build app on the GitHub Enterprise server. |
| `createTime` | `string` | Output only. Time when the installation was associated with the project. |
| `displayName` | `string` | Name to display for this config. |
| `peeredNetwork` | `string` | Optional. The network to be used when reaching out to the GitHub Enterprise server. The VPC network must be enabled for private service connection. This should be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the GitHub Enterprise server will be made over the public internet. Must be in the format `projects/{project}/global/networks/{network}`, where {project} is a project number or id and {network} is the name of a VPC network in the project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_githubEnterpriseConfigs_get` | `SELECT` | `githubEnterpriseConfigsId, projectsId` | Retrieve a GitHubEnterpriseConfig. |
| `projects_githubEnterpriseConfigs_list` | `SELECT` | `projectsId` | List all GitHubEnterpriseConfigs for a given project. |
| `projects_locations_githubEnterpriseConfigs_get` | `SELECT` | `githubEnterpriseConfigsId, locationsId, projectsId` | Retrieve a GitHubEnterpriseConfig. |
| `projects_locations_githubEnterpriseConfigs_list` | `SELECT` | `locationsId, projectsId` | List all GitHubEnterpriseConfigs for a given project. |
| `projects_githubEnterpriseConfigs_create` | `INSERT` | `projectsId` | Create an association between a GCP project and a GitHub Enterprise server. |
| `projects_locations_githubEnterpriseConfigs_create` | `INSERT` | `locationsId, projectsId` | Create an association between a GCP project and a GitHub Enterprise server. |
| `projects_githubEnterpriseConfigs_delete` | `DELETE` | `githubEnterpriseConfigsId, projectsId` | Delete an association between a GCP project and a GitHub Enterprise server. |
| `projects_locations_githubEnterpriseConfigs_delete` | `DELETE` | `githubEnterpriseConfigsId, locationsId, projectsId` | Delete an association between a GCP project and a GitHub Enterprise server. |
| `projects_githubEnterpriseConfigs_patch` | `EXEC` | `githubEnterpriseConfigsId, projectsId` | Update an association between a GCP project and a GitHub Enterprise server. |
| `projects_locations_githubEnterpriseConfigs_patch` | `EXEC` | `githubEnterpriseConfigsId, locationsId, projectsId` | Update an association between a GCP project and a GitHub Enterprise server. |
