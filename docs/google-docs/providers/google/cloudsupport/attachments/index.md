---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - attachments
  - cloudsupport
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsupport.attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the attachment. |
| `sizeBytes` | `string` | Output only. The size of the attachment in bytes. |
| `createTime` | `string` | Output only. The time at which the attachment was created. |
| `creator` | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
| `filename` | `string` | The filename of the attachment (e.g. `"graph.jpg"`). |
| `mimeType` | `string` | Output only. The MIME type of the attachment (e.g. text/plain). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `parent, parentType` |
| `_list` | `EXEC` | `parent, parentType` |
