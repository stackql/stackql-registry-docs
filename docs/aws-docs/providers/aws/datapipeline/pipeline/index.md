---
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
  - datapipeline
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
<tr><td><b>Id</b></td><td><code>aws.datapipeline.pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Activate</code></td><td><code>boolean</code></td><td>Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to true.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the pipeline.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the pipeline.</td></tr>
<tr><td><code>ParameterObjects</code></td><td><code>array</code></td><td>The parameter objects used with the pipeline.</td></tr>
<tr><td><code>ParameterValues</code></td><td><code>array</code></td><td>The parameter values used with the pipeline.</td></tr>
<tr><td><code>PipelineObjects</code></td><td><code>array</code></td><td>The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see Editing Your Pipeline in the AWS Data Pipeline Developer Guide.</td></tr>
<tr><td><code>PipelineTags</code></td><td><code>array</code></td><td>A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see Controlling Access to Pipelines and Resources in the AWS Data Pipeline Developer Guide.</td></tr>
<tr><td><code>PipelineId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.datapipeline.pipeline<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;PipelineId&gt;'
</pre>
