---
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
  - firebaserules
  - firebase    
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
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebaserules.releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Format: `projects/{project_id}/releases/{release_id}` |
| `createTime` | `string` | Output only. Time the release was created. |
| `rulesetName` | `string` | Required. Name of the `Ruleset` referred to by this `Release`. The `Ruleset` must exist for the `Release` to be created. |
| `updateTime` | `string` | Output only. Time the release was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_releases_get` | `SELECT` | `projectsId, releasesId` | Get a `Release` by name. |
| `projects_releases_list` | `SELECT` | `projectsId` | List the `Release` values for a project. This list may optionally be filtered by `Release` name, `Ruleset` name, `TestSuite` name, or any combination thereof. |
| `projects_releases_create` | `INSERT` | `projectsId` | Create a `Release`. Release names should reflect the developer's deployment practices. For example, the release name may include the environment name, application name, application version, or any other name meaningful to the developer. Once a `Release` refers to a `Ruleset`, the rules can be enforced by Firebase Rules-enabled services. More than one `Release` may be 'live' concurrently. Consider the following three `Release` names for `projects/foo` and the `Ruleset` to which they refer. Release Name -&gt; Ruleset Name * projects/foo/releases/prod -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/beta -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/v23 -&gt; projects/foo/rulesets/uuid456 The relationships reflect a `Ruleset` rollout in progress. The `prod` and `prod/beta` releases refer to the same `Ruleset`. However, `prod/v23` refers to a new `Ruleset`. The `Ruleset` reference for a `Release` may be updated using the UpdateRelease method. |
| `projects_releases_delete` | `DELETE` | `projectsId, releasesId` | Delete a `Release` by resource name. |
| `projects_releases_patch` | `EXEC` | `projectsId, releasesId` | Update a `Release` via PATCH. Only updates to `ruleset_name` will be honored. `Release` rename is not supported. To create a `Release` use the CreateRelease method. |
