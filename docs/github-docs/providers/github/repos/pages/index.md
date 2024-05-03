---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.pages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="build_type" /> | `string` | The process in which the Page will be built. |
| <CopyableCode code="cname" /> | `string` | The Pages site's custom domain |
| <CopyableCode code="custom_404" /> | `boolean` | Whether the Page has a custom 404 page. |
| <CopyableCode code="html_url" /> | `string` | The web address the Page can be accessed from. |
| <CopyableCode code="https_certificate" /> | `object` |  |
| <CopyableCode code="https_enforced" /> | `boolean` | Whether https is enabled on the domain |
| <CopyableCode code="pending_domain_unverified_at" /> | `string` | The timestamp when a pending domain becomes unverified. |
| <CopyableCode code="protected_domain_state" /> | `string` | The state if the domain is verified |
| <CopyableCode code="public" /> | `boolean` | Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. |
| <CopyableCode code="source" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | The status of the most recent build of the Page. |
| <CopyableCode code="url" /> | `string` | The API address for accessing this Page resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_pages" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Gets information about a GitHub Pages site.<br /><br />A token with the `repo` scope is required. GitHub Apps must have the `pages:read` permission. |
| <CopyableCode code="create_pages_site" /> | `INSERT` | <CopyableCode code="owner, repo" /> | Configures a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages)."<br /><br />To use this endpoint, you must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission. A token with the `repo` scope or Pages write permission is required. GitHub Apps must have the `administration:write` and `pages:write` permissions. |
| <CopyableCode code="delete_pages_site" /> | `DELETE` | <CopyableCode code="owner, repo" /> | Deletes a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).<br /><br />To use this endpoint, you must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission. A token with the `repo` scope or Pages write permission is required. GitHub Apps must have the `administration:write` and `pages:write` permissions. |
| <CopyableCode code="update_information_about_pages_site" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Updates information for a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).<br /><br />To use this endpoint, you must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission. A token with the `repo` scope or Pages write permission is required. GitHub Apps must have the `administration:write` and `pages:write` permissions. |
