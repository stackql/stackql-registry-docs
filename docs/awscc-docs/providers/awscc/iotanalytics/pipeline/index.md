---
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
  - iotanalytics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>pipeline</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipeline</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotanalytics.pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pipeline_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>pipeline_activities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
pipeline_name,
tags,
pipeline_activities
FROM awscc.iotanalytics.pipeline
WHERE region = 'us-east-1'
AND data__Identifier = '{PipelineName}';
```

## Permissions

To operate on the <code>pipeline</code> resource, the following permissions are required:

### Read
```json
iotanalytics:DescribePipeline,
iotanalytics:ListTagsForResource
```

### Update
```json
iotanalytics:UpdatePipeline,
iotanalytics:TagResource,
iotanalytics:UntagResource
```

### Delete
```json
iotanalytics:DeletePipeline
```

