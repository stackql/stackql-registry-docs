---
title: resource_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy
  - secretsmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_policy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.secretsmanager.resource_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourcePolicy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BlockPublicPolicy</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>SecretId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.secretsmanager.resource_policy<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
