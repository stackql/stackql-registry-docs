---
title: contact_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flows
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>contact_flows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.connect.contact_flows</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance (ARN).</td></tr>
<tr><td><code>ContactFlowArn</code></td><td><code>string</code></td><td>The identifier of the contact flow (ARN).</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the contact flow.</td></tr>
<tr><td><code>Content</code></td><td><code>string</code></td><td>The content of the contact flow in JSON format.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the contact flow.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>The state of the contact flow.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The type of the contact flow.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.connect.contact_flows
WHERE region = 'us-east-1'
</pre>
