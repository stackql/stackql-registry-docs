---
title: media
hide_title: false
hide_table_of_contents: false
keywords:
  - media
  - displayvideo
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
<tr><td><b>Name</b></td><td><code>media</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.media</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `download` | `EXEC` | `resourceName` | Downloads media. Download is supported on the URI `/download/&#123;resource_name=**&#125;?alt=media.` **Note**: Download requests will not be successful without including `alt=media` query string. |
| `upload` | `EXEC` | `resourceName` | Uploads media. Upload is supported on the URI `/upload/media/&#123;resource_name=**&#125;?upload_type=media.` **Note**: Upload requests will not be successful without including `upload_type=media` query string. |
