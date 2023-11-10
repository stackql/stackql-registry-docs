---
title: contact_flow
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flow
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
Gets an individual <code>contact_flow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>contact_flow</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.contact_flow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance (ARN).</td></tr>
<tr><td><code>contact_flow_arn</code></td><td><code>string</code></td><td>The identifier of the contact flow (ARN).</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the contact flow.</td></tr>
<tr><td><code>content</code></td><td><code>string</code></td><td>The content of the contact flow in JSON format.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the contact flow.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the contact flow.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the contact flow.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
contact_flow_arn,
name,
content,
description,
state,
type,
tags
FROM aws.connect.contact_flow
WHERE region = 'us-east-1'
AND data__Identifier = '<ContactFlowArn>'
```
