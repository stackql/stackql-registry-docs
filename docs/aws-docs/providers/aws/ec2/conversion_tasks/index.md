---
title: conversion_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - conversion_tasks
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
<tr><td><b>Name</b></td><td><code>conversion_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.conversion_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `importInstance` | `object` | Describes an import instance task. |
| `importVolume` | `object` | Describes an import volume task. |
| `state` | `string` | The state of the conversion task. |
| `statusMessage` | `string` | The status message related to the conversion task. |
| `tagSet` | `array` | Any tags assigned to the task. |
| `conversionTaskId` | `string` | The ID of the conversion task. |
| `expirationTime` | `string` | The time when the task expires. If the upload isn't complete before the expiration time, we automatically cancel the task. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `conversion_tasks_Describe` | `SELECT` |  | &lt;p&gt;Describes the specified conversion tasks or all your conversion tasks. For more information, see the &lt;a href="https://docs.aws.amazon.com/vm-import/latest/userguide/"&gt;VM Import/Export User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For information about the import manifest referenced by this API action, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html"&gt;VM Import Manifest&lt;/a&gt;.&lt;/p&gt; |
| `conversion_task_Cancel` | `EXEC` | `ConversionTaskId` | &lt;p&gt;Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the conversion is complete or is in the process of transferring the final disk image, the command fails and returns an exception.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/ec2-cli-vmimport-export.html"&gt;Importing a Virtual Machine Using the Amazon EC2 CLI&lt;/a&gt;.&lt;/p&gt; |
