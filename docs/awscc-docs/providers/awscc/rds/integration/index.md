---
title: integration
hide_title: false
hide_table_of_contents: false
keywords:
  - integration
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>integration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.integration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>integration_name</code></td><td><code>string</code></td><td>The name of the integration.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Aurora DB cluster to use as the source for replication.</td></tr>
<tr><td><code>target_arn</code></td><td><code>string</code></td><td>The ARN of the Redshift data warehouse to use as the target for replication.</td></tr>
<tr><td><code>integration_arn</code></td><td><code>string</code></td><td>The ARN of the integration.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>An optional AWS Key Management System (AWS KMS) key ARN for the key used to to encrypt the integration. The resource accepts the key ID and the key ARN forms. The key ID form can be used if the KMS key is owned by te same account. If the KMS key belongs to a different account than the calling account, the full key ARN must be specified. Do not use the key alias or the key alias ARN as this will cause a false drift of the resource.</td></tr>
<tr><td><code>additional_encryption_context</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
integration_name,
tags,
source_arn,
target_arn,
integration_arn,
k_ms_key_id,
additional_encryption_context,
create_time
FROM awscc.rds.integration
WHERE region = 'us-east-1'
AND data__Identifier = '{IntegrationArn}';
```

## Permissions

To operate on the <code>integration</code> resource, the following permissions are required:

### Read
```json
rds:DescribeIntegrations
```

### Update
```json
rds:DescribeIntegrations,
rds:AddTagsToResource,
rds:RemoveTagsFromResource
```

### Delete
```json
rds:DeleteIntegration,
rds:DescribeIntegrations
```

