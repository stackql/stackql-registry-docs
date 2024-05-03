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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>connection</code> resource, use <code>connections</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Connection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.connection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the connection.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The arn of the connection resource.</td></tr>
<tr><td><CopyableCode code="secret_arn" /></td><td><code>string</code></td><td>The arn of the secrets manager secret created in the customer account.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the connection.</td></tr>
<tr><td><CopyableCode code="authorization_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
arn,
secret_arn,
description,
authorization_type,
auth_parameters
FROM aws.events.connection
WHERE data__Identifier = '<Name>';
```

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

