---
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
  - sagemaker
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
null
<tr><td><b>Id</b></td><td><code>aws.sagemaker.pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PipelineName</code></td><td><code>string</code></td><td>The name of the Pipeline.</td></tr><tr><td><code>PipelineDisplayName</code></td><td><code>string</code></td><td>The display name of the Pipeline.</td></tr><tr><td><code>PipelineDescription</code></td><td><code>string</code></td><td>The description of the Pipeline.</td></tr><tr><td><code>PipelineDefinition</code></td><td><code>object</code></td><td></td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>Role Arn</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ParallelismConfiguration</code></td><td><code>object</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.pipeline
WHERE region = 'us-east-1' AND data__Identifier = '{PipelineName}'
</pre>
