---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.images</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `edits_images_list` | `SELECT` | `editId, imageType, language, packageName` | Lists all images. The response may be empty. |
| `edits_images_delete` | `DELETE` | `editId, imageId, imageType, language, packageName` | Deletes the image (specified by id) from the edit. |
| `edits_images_upload` | `EXEC` | `editId, imageType, language, packageName` | Uploads an image of the specified language and image type, and adds to the edit. |
