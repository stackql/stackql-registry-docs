---
title: import_snapshot_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - import_snapshot_tasks
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
<tr><td><b>Name</b></td><td><code>import_snapshot_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.import_snapshot_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the import snapshot task. |
| `importTaskId` | `string` | The ID of the import snapshot task. |
| `snapshotTaskDetail` | `object` | Details about the import snapshot task. |
| `tagSet` | `array` | The tags for the import snapshot task. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `import_snapshot_tasks_Describe` | `SELECT` |  |
