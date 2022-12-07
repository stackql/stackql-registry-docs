---
title: export_image_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - export_image_tasks
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>export_image_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.export_image_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the image being exported. |
| `imageId` | `string` | The ID of the image. |
| `progress` | `string` | The percent complete of the export image task. |
| `s3ExportLocation` | `object` | Describes the destination for an export image task. |
| `status` | `string` | The status of the export image task. The possible values are &lt;code&gt;active&lt;/code&gt;, &lt;code&gt;completed&lt;/code&gt;, &lt;code&gt;deleting&lt;/code&gt;, and &lt;code&gt;deleted&lt;/code&gt;. |
| `statusMessage` | `string` | The status message for the export image task. |
| `tagSet` | `array` | Any tags assigned to the export image task. |
| `exportImageTaskId` | `string` | The ID of the export image task. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `export_image_tasks_Describe` | `SELECT` |  |
