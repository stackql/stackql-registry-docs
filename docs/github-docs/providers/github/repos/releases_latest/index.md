---
title: releases_latest
hide_title: false
hide_table_of_contents: false
keywords:
  - releases_latest
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
<tr><td><b>Name</b></td><td><code>releases_latest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.releases_latest" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="assets" /> | `array` |  |
| <CopyableCode code="assets_url" /> | `string` |  |
| <CopyableCode code="author" /> | `object` | A GitHub user. |
| <CopyableCode code="body" /> | `string` |  |
| <CopyableCode code="body_html" /> | `string` |  |
| <CopyableCode code="body_text" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="discussion_url" /> | `string` | The URL of the release discussion. |
| <CopyableCode code="draft" /> | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="mentions_count" /> | `integer` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="prerelease" /> | `boolean` | Whether to identify the release as a prerelease or a full release. |
| <CopyableCode code="published_at" /> | `string` |  |
| <CopyableCode code="reactions" /> | `object` |  |
| <CopyableCode code="tag_name" /> | `string` | The name of the tag. |
| <CopyableCode code="tarball_url" /> | `string` |  |
| <CopyableCode code="target_commitish" /> | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| <CopyableCode code="upload_url" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="zipball_url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_latest_release" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
