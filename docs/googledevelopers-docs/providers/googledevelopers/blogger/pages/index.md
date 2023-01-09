---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
  - blogger
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this resource. |
| `kind` | `string` | The kind of this entity. Always blogger#page. |
| `title` | `string` | The title of this entity. This is the name displayed in the Admin user interface. |
| `blog` | `object` | Data about the blog containing this Page. |
| `content` | `string` | The body content of this Page, in HTML. |
| `url` | `string` | The URL that this Page is displayed at. |
| `etag` | `string` | Etag of the resource. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `status` | `string` | The status of the page for admin resources (either LIVE or DRAFT). |
| `published` | `string` | RFC 3339 date-time when this Page was published. |
| `trashed` | `string` | RFC 3339 date-time when this Page was trashed. |
| `author` | `object` | The author of this Page. |
| `updated` | `string` | RFC 3339 date-time when this Page was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blogId, pageId` | Gets a page by blog id and page id. |
| `list` | `SELECT` | `blogId` | Lists pages. |
| `insert` | `INSERT` | `blogId` | Inserts a page. |
| `delete` | `DELETE` | `blogId, pageId` | Deletes a page by blog id and page id. |
| `patch` | `EXEC` | `blogId, pageId` | Patches a page. |
| `publish` | `EXEC` | `blogId, pageId` | Publishes a page. |
| `revert` | `EXEC` | `blogId, pageId` | Reverts a published or scheduled page to draft state. |
| `update` | `EXEC` | `blogId, pageId` | Updates a page by blog id and page id. |
