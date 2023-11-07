---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - fms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policies</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fms.policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ExcludeMap</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ExcludeResourceTags</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>IncludeMap</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PolicyName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PolicyDescription</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RemediationEnabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ResourceTags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResourceType</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ResourceTypeList</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResourceSetIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SecurityServicePolicyData</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DeleteAllPolicyResources</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ResourcesCleanUp</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.fms.policies
WHERE region = 'us-east-1'
</pre>
