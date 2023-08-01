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
| `bitbucketServerConfigs` | `array` | A list of BitbucketServerConfigs |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bitbucket_server_configs_get` | `SELECT` | `bitbucketServerConfigsId, locationsId, projectsId` | Retrieve a `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_bitbucket_server_configs_list` | `SELECT` | `locationsId, projectsId` | List all `BitbucketServerConfigs` for a given project. This API is experimental. |
| `projects_locations_bitbucket_server_configs_create` | `INSERT` | `locationsId, projectsId` | Creates a new `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_bitbucket_server_configs_delete` | `DELETE` | `bitbucketServerConfigsId, locationsId, projectsId` | Delete a `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_bitbucket_server_configs_patch` | `EXEC` | `bitbucketServerConfigsId, locationsId, projectsId` | Updates an existing `BitbucketServerConfig`. This API is experimental. |
