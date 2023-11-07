---
title: notebook_instance_lifecycle_config
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_instance_lifecycle_config
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
Gets an individual <code>notebook_instance_lifecycle_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_instance_lifecycle_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notebook_instance_lifecycle_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.notebook_instance_lifecycle_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NotebookInstanceLifecycleConfigName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>OnStart</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>OnCreate</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sagemaker.notebook_instance_lifecycle_config<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
