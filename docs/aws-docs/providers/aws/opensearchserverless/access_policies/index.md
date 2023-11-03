---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>access_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.access_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the policy</td></tr><tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the policy</td></tr><tr><td><code>Policy</code></td><td><code>string</code></td><td>The JSON policy document that is the content for the policy</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opensearchserverless.access_policies
WHERE region = 'us-east-1'
</pre>
