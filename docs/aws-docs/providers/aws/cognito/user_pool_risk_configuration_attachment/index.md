---
title: user_pool_risk_configuration_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_risk_configuration_attachment
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
Gets an individual <code>user_pool_risk_configuration_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_risk_configuration_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_risk_configuration_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_risk_configuration_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compromised_credentials_risk_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_takeover_risk_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>risk_exception_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
compromised_credentials_risk_configuration,
user_pool_id,
client_id,
account_takeover_risk_configuration,
risk_exception_configuration
FROM aws.cognito.user_pool_risk_configuration_attachment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
