---
title: export_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - export_tasks
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
<tr><td><b>Name</b></td><td><code>export_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.export_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the resource being exported. |
| `instanceExport` | `object` | Describes an instance to export. |
| `state` | `string` | The state of the export task. |
| `statusMessage` | `string` | The status message related to the export task. |
| `tagSet` | `array` | The tags for the export task. |
| `exportTaskId` | `string` | The ID of the export task. |
| `exportToS3` | `object` | Describes the format and location for the export task. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `export_tasks_Describe` | `SELECT` |  | Describes the specified export instance tasks or all of your export instance tasks. |
| `export_task_Cancel` | `EXEC` | `ExportTaskId` | Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error. |
