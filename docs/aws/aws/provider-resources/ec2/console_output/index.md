---
title: console_output
hide_title: false
hide_table_of_contents: false
keywords:
  - console_output
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
<tr><td><b>Name</b></td><td><code>console_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.console_output</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceId` | `string` | The ID of the instance. |
| `output` | `string` | The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you. |
| `timestamp` | `string` | The time at which the output was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `console_output_Get` | `SELECT` | `InstanceId` |
