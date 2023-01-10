---
title: pages__thumbnail
hide_title: false
hide_table_of_contents: false
keywords:
  - pages__thumbnail
  - slides
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
<tr><td><b>Name</b></td><td><code>pages__thumbnail</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.slides.pages__thumbnail</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contentUrl` | `string` | The content URL of the thumbnail image. The URL to the image has a default lifetime of 30 minutes. This URL is tagged with the account of the requester. Anyone with the URL effectively accesses the image as the original requester. Access to the image may be lost if the presentation's sharing settings change. The mime type of the thumbnail image is the same as specified in the `GetPageThumbnailRequest`. |
| `height` | `integer` | The positive height in pixels of the thumbnail image. |
| `width` | `integer` | The positive width in pixels of the thumbnail image. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `presentations_pages_getThumbnail` | `SELECT` | `pageObjectId, presentationId` |
