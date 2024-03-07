---
title: connection
hide_title: false
hide_table_of_contents: false
keywords:
  - connection
  - events
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.events.connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the connection.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The arn of the connection resource.</td></tr>
<tr><td><code>secret_arn</code></td><td><code>string</code></td><td>The arn of the secrets manager secret created in the customer account.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the connection.</td></tr>
<tr><td><code>authorization_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auth_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>connection</code> resource, the following permissions are required:

### Read
```json
events:DescribeConnection
```

### Update
```json
events:UpdateConnection,
events:DescribeConnection,
secretsmanager:CreateSecret,
secretsmanager:UpdateSecret,
secretsmanager:GetSecretValue,
secretsmanager:PutSecretValue
```

### Delete
```json
events:DeleteConnection,
events:DescribeConnection
```


## Example
```sql
SELECT
region,
name,
arn,
secret_arn,
description,
authorization_type,
auth_parameters
FROM awscc.events.connection
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
