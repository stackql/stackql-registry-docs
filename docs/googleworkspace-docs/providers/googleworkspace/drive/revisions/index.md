---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
  - drive
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the revision. |
| `publishAuto` | `boolean` | Whether subsequent revisions will be automatically republished. This is only applicable to Docs Editors files. |
| `originalFilename` | `string` | The original filename used to create this revision. This is only applicable to files with binary content in Drive. |
| `exportLinks` | `object` | Links for exporting Docs Editors files to specific formats. |
| `lastModifyingUser` | `object` | Information about a Drive user. |
| `published` | `boolean` | Whether this revision is published. This is only applicable to Docs Editors files. |
| `publishedLink` | `string` | A link to the published revision. This is only populated for Google Sites files. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#revision". |
| `mimeType` | `string` | The MIME type of the revision. |
| `size` | `string` | The size of the revision's content in bytes. This is only applicable to files with binary content in Drive. |
| `md5Checksum` | `string` | The MD5 checksum of the revision's content. This is only applicable to files with binary content in Drive. |
| `modifiedTime` | `string` | The last time the revision was modified (RFC 3339 date-time). |
| `keepForever` | `boolean` | Whether to keep this revision forever, even if it is no longer the head revision. If not set, the revision will be automatically purged 30 days after newer content is uploaded. This can be set on a maximum of 200 revisions for a file.<br />This field is only applicable to files with binary content in Drive. |
| `publishedOutsideDomain` | `boolean` | Whether this revision is published outside the domain. This is only applicable to Docs Editors files. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileId, revisionId` | Gets a revision's metadata or content by ID. |
| `list` | `SELECT` | `fileId` | Lists a file's revisions. |
| `delete` | `DELETE` | `fileId, revisionId` | Permanently deletes a file version. You can only delete revisions for files with binary content in Google Drive, like images or videos. Revisions for other files, like Google Docs or Sheets, and the last remaining file version can't be deleted. |
| `update` | `EXEC` | `fileId, revisionId` | Updates a revision with patch semantics. |
