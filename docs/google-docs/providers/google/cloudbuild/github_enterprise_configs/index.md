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
