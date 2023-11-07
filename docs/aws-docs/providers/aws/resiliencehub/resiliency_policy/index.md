---
title: resiliency_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resiliency_policy
  - resiliencehub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resiliency_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resiliency_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resiliency_policy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.resiliencehub.resiliency_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PolicyName</code></td><td><code>string</code></td><td>Name of Resiliency Policy.</td></tr>
<tr><td><code>PolicyDescription</code></td><td><code>string</code></td><td>Description of Resiliency Policy.</td></tr>
<tr><td><code>DataLocationConstraint</code></td><td><code>string</code></td><td>Data Location Constraint of the Policy.</td></tr>
<tr><td><code>Tier</code></td><td><code>string</code></td><td>Resiliency Policy Tier.</td></tr>
<tr><td><code>Policy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>PolicyArn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.resiliencehub.resiliency_policy
WHERE region = 'us-east-1' AND data__Identifier = '&lt;PolicyArn&gt;'
</pre>
