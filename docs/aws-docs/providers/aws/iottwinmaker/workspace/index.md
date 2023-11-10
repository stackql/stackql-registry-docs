---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - iottwinmaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workspace</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.workspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the workspace.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the workspace.</td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td>The ARN of the execution role associated with the workspace.</td></tr>
<tr><td><code>s3_location</code></td><td><code>string</code></td><td>The ARN of the S3 bucket where resources associated with the workspace are stored.</td></tr>
<tr><td><code>creation_date_time</code></td><td><code>string</code></td><td>The date and time when the workspace was created.</td></tr>
<tr><td><code>update_date_time</code></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
workspace_id,
arn,
description,
role,
s3_location,
creation_date_time,
update_date_time,
tags
FROM aws.iottwinmaker.workspace
WHERE region = 'us-east-1'
AND data__Identifier = '<WorkspaceId>'
```
