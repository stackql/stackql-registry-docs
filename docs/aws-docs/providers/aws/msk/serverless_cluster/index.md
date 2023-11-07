---
title: serverless_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_cluster
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>serverless_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>serverless_cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.msk.serverless_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ClusterName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VpcConfigs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ClientAuthentication</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.msk.serverless_cluster<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
