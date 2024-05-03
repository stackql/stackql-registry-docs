---
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
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
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.releases" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_release" /> | `SELECT` | <CopyableCode code="owner, release_id, repo" /> | **Note:** This returns an `upload_url` key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/rest/overview/resources-in-the-rest-api#hypermedia). |
| <CopyableCode code="get_release_by_tag" /> | `SELECT` | <CopyableCode code="owner, repo, tag" /> | Get a published release with the specified tag. |
| <CopyableCode code="list_releases" /> | `SELECT` | <CopyableCode code="owner, repo" /> | This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/rest/repos/repos#list-repository-tags).<br /><br />Information about published releases are available to everyone. Only users with push access will receive listings for draft releases. |
| <CopyableCode code="create_release" /> | `INSERT` | <CopyableCode code="owner, repo, data__tag_name" /> | Users with push access to the repository can create a release.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| <CopyableCode code="delete_release" /> | `DELETE` | <CopyableCode code="owner, release_id, repo" /> | Users with push access to the repository can delete a release. |
| <CopyableCode code="generate_release_notes" /> | `EXEC` | <CopyableCode code="owner, repo, data__tag_name" /> | Generate a name and body describing a [release](https://docs.github.com/rest/releases/releases#get-a-release). The body content will be markdown formatted and contain information like the changes since last release and users who contributed. The generated release notes are not saved anywhere. They are intended to be generated and used when creating a new release. |
| <CopyableCode code="update_release" /> | `EXEC` | <CopyableCode code="owner, release_id, repo" /> | Users with push access to the repository can edit a release. |
