---
title: user_pool_risk_configuration_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_risk_configuration_attachments
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
Retrieves a list of <code>user_pool_risk_configuration_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_risk_configuration_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_risk_configuration_attachments</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.user_pool_risk_configuration_attachments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>user_pool_risk_configuration_attachments</code> resource, the following permissions are required:

### Create
<pre>
cognito-idp:SetRiskConfiguration,
cognito-idp:DescribeRiskConfiguration,
iam:PassRole</pre>


## Example
```sql
SELECT
region,
user_pool_id,
client_id
FROM awscc.cognito.user_pool_risk_configuration_attachments
WHERE region = 'us-east-1'
```
