---
title: workgroup
hide_title: false
hide_table_of_contents: false
keywords:
  - workgroup
  - redshiftserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workgroup</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.redshiftserverless.workgroup</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>WorkgroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NamespaceName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BaseCapacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>EnhancedVpcRouting</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ConfigParameters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SubnetIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Workgroup</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshiftserverless.workgroup
WHERE region = 'us-east-1' AND data__Identifier = '&lt;WorkgroupName&gt;'
</pre>
