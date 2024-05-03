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
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaserules.releases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Format: `projects/&#123;project_id&#125;/releases/&#123;release_id&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the release was created. |
| <CopyableCode code="rulesetName" /> | `string` | Required. Name of the `Ruleset` referred to by this `Release`. The `Ruleset` must exist for the `Release` to be created. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time the release was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_releases_get" /> | `SELECT` | <CopyableCode code="projectsId, releasesId" /> | Get a `Release` by name. |
| <CopyableCode code="projects_releases_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | List the `Release` values for a project. This list may optionally be filtered by `Release` name, `Ruleset` name, `TestSuite` name, or any combination thereof. |
| <CopyableCode code="projects_releases_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Create a `Release`. Release names should reflect the developer's deployment practices. For example, the release name may include the environment name, application name, application version, or any other name meaningful to the developer. Once a `Release` refers to a `Ruleset`, the rules can be enforced by Firebase Rules-enabled services. More than one `Release` may be 'live' concurrently. Consider the following three `Release` names for `projects/foo` and the `Ruleset` to which they refer. Release Name -&gt; Ruleset Name * projects/foo/releases/prod -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/beta -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/v23 -&gt; projects/foo/rulesets/uuid456 The relationships reflect a `Ruleset` rollout in progress. The `prod` and `prod/beta` releases refer to the same `Ruleset`. However, `prod/v23` refers to a new `Ruleset`. The `Ruleset` reference for a `Release` may be updated using the UpdateRelease method. |
| <CopyableCode code="projects_releases_delete" /> | `DELETE` | <CopyableCode code="projectsId, releasesId" /> | Delete a `Release` by resource name. |
| <CopyableCode code="projects_releases_patch" /> | `EXEC` | <CopyableCode code="projectsId, releasesId" /> | Update a `Release` via PATCH. Only updates to `ruleset_name` will be honored. `Release` rename is not supported. To create a `Release` use the CreateRelease method. |
