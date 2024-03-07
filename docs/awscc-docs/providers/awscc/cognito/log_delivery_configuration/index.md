---
title: log_delivery_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - log_delivery_configuration
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>log_delivery_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_delivery_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>log_delivery_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.log_delivery_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>log_delivery_configuration</code> resource, the following permissions are required:

### Read
<pre>
cognito-idp:GetLogDeliveryConfiguration</pre>

### Update
<pre>
cognito-idp:GetLogDeliveryConfiguration,
cognito-idp:SetLogDeliveryConfiguration,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups</pre>

### Delete
<pre>
cognito-idp:GetLogDeliveryConfiguration,
cognito-idp:SetLogDeliveryConfiguration,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups</pre>


## Example
```sql
SELECT
region,
id,
user_pool_id,
log_configurations
FROM awscc.cognito.log_delivery_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
