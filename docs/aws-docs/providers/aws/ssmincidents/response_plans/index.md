---
title: response_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plans
  - ssmincidents
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>response_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ssmincidents.response_plans</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the response plan.</td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td>The display name of the response plan.</td></tr>
<tr><td><code>ChatChannel</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Engagements</code></td><td><code>array</code></td><td>The list of engagements to use.</td></tr>
<tr><td><code>Actions</code></td><td><code>array</code></td><td>The list of actions.</td></tr>
<tr><td><code>Integrations</code></td><td><code>array</code></td><td>The list of integrations.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags to apply to the response plan.</td></tr>
<tr><td><code>IncidentTemplate</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssmincidents.response_plans
WHERE region = 'us-east-1'
</pre>
