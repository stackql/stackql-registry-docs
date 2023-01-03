---
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `node_id` | `string` |  |
| `reactions` | `object` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `html_url` | `string` |  |
| `tarball_url` | `string` |  |
| `assets` | `array` |  |
| `body` | `string` |  |
| `author` | `object` | Simple User |
| `body_html` | `string` |  |
| `created_at` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `tag_name` | `string` | The name of the tag. |
| `mentions_count` | `integer` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `zipball_url` | `string` |  |
| `body_text` | `string` |  |
| `published_at` | `string` |  |
| `url` | `string` |  |
| `upload_url` | `string` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `assets_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_release` | `SELECT` | `owner, release_id, repo` | **Note:** This returns an `upload_url` key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/rest/overview/resources-in-the-rest-api#hypermedia). |
| `get_release_by_tag` | `SELECT` | `owner, repo, tag` | Get a published release with the specified tag. |
| `list_releases` | `SELECT` | `owner, repo` | This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/rest/reference/repos#list-repository-tags).<br /><br />Information about published releases are available to everyone. Only users with push access will receive listings for draft releases. |
| `create_release` | `INSERT` | `owner, repo, data__tag_name` | Users with push access to the repository can create a release.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `delete_release` | `DELETE` | `owner, release_id, repo` | Users with push access to the repository can delete a release. |
| `generate_release_notes` | `EXEC` | `owner, repo, data__tag_name` | Generate a name and body describing a [release](https://docs.github.com/rest/reference/repos#releases). The body content will be markdown formatted and contain information like the changes since last release and users who contributed. The generated release notes are not saved anywhere. They are intended to be generated and used when creating a new release. |
| `update_release` | `EXEC` | `owner, release_id, repo` | Users with push access to the repository can edit a release. |
