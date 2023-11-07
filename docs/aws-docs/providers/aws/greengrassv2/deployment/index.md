---
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
  - greengrassv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>deployment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrassv2.deployment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>TargetArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ParentTargetArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DeploymentId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DeploymentName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Components</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>IotJobConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DeploymentPolicies</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.greengrassv2.deployment<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;DeploymentId&gt;'
</pre>
