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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_risk_configuration_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>risk_exception_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>compromised_credentials_risk_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>account_takeover_risk_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
user_pool_id,
client_id,
risk_exception_configuration,
compromised_credentials_risk_configuration,
account_takeover_risk_configuration
FROM aws.cognito.user_pool_risk_configuration_attachment
WHERE data__Identifier = '<UserPoolId>|<ClientId>';
```

## Permissions

To operate on the <code>user_pool_risk_configuration_attachment</code> resource, the following permissions are required:

### Read
```json
cognito-idp:DescribeRiskConfiguration
```

### Update
```json
cognito-idp:SetRiskConfiguration,
cognito-idp:DescribeRiskConfiguration,
iam:PassRole
```

### Delete
```json
cognito-idp:SetRiskConfiguration,
cognito-idp:DescribeRiskConfiguration
```

