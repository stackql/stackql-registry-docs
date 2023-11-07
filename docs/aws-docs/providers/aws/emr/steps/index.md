---
title: steps
hide_title: false
hide_table_of_contents: false
keywords:
  - steps
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>steps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>steps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>steps</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.steps</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ActionOnFailure</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HadoopJarStep</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>JobFlowId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.emr.steps
WHERE region = 'us-east-1'
</pre>
