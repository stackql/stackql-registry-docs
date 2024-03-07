---
title: log_delivery_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - log_delivery_configurations
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
Retrieves a list of <code>log_delivery_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_delivery_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>log_delivery_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.log_delivery_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>log_delivery_configurations</code> resource, the following permissions are required:

### Create
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
id
FROM awscc.cognito.log_delivery_configurations
WHERE region = 'us-east-1'
```
