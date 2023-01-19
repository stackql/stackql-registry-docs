---
title: notes
hide_title: false
hide_table_of_contents: false
keywords:
  - notes
  - keep
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
<tr><td><b>Name</b></td><td><code>notes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.keep.notes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of this note. See general note on identifiers in KeepService. |
| `permissions` | `array` | Output only. The list of permissions set on the note. Contains at least one entry for the note owner. |
| `trashed` | `boolean` | Output only. `true` if this note has been trashed. If trashed, the note is eventually deleted. |
| `attachments` | `array` | Output only. The attachments attached to this note. |
| `body` | `object` | The content of the note. |
| `createTime` | `string` | Output only. When this note was created. |
| `title` | `string` | The title of the note. Length must be less than 1,000 characters. |
| `updateTime` | `string` | Output only. When this note was last modified. |
| `trashTime` | `string` | Output only. When this note was trashed. If `trashed`, the note is eventually deleted. If the note is not trashed, this field is not set (and the trashed field is `false`). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `notesId` | Gets a note. |
| `list` | `SELECT` |  | Lists notes. Every list call returns a page of results with `page_size` as the upper bound of returned items. A `page_size` of zero allows the server to choose the upper bound. The ListNotesResponse contains at most `page_size` entries. If there are more things left to list, it provides a `next_page_token` value. (Page tokens are opaque values.) To get the next page of results, copy the result's `next_page_token` into the next request's `page_token`. Repeat until the `next_page_token` returned with a page of results is empty. ListNotes return consistent results in the face of concurrent changes, or signals that it cannot with an ABORTED error. |
| `create` | `INSERT` |  | Creates a new note. |
| `delete` | `DELETE` | `notesId` | Deletes a note. Caller must have the `OWNER` role on the note to delete. Deleting a note removes the resource immediately and cannot be undone. Any collaborators will lose access to the note. |
