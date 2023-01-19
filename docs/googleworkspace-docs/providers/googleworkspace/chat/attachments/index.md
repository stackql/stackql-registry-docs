---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - attachments
  - chat
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
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chat.attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the attachment, in the form "spaces/*/messages/*/attachments/*". |
| `downloadUri` | `string` | Output only. The download URL which should be used to allow a human user to download the attachment. Chat apps should not use this URL to download attachment content. |
| `driveDataRef` | `object` | A reference to the data of a drive attachment. |
| `source` | `string` | The source of the attachment. |
| `thumbnailUri` | `string` | Output only. The thumbnail URL which should be used to preview the attachment to a human user. Chat apps should not use this URL to download attachment content. |
| `attachmentDataRef` | `object` |  |
| `contentName` | `string` | The original file name for the content, not the full path. |
| `contentType` | `string` | The content type (MIME type) of the file. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `spaces_messages_attachments_get` | `SELECT` | `attachmentsId, messagesId, spacesId` |
