---
title: registry_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policy
  - ecr
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

Gets or operates on an individual <code>registry_policy</code> resource, use <code>registry_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ECR::RegistryPolicy`` resource creates or updates the permissions policy for a private registry.&lt;br&#x2F;&gt; A private registry policy is used to specify permissions for another AWS-account and is used when configuring cross-account replication. For more information, see &#91;Registry permissions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;registry-permissions.html) in the *Amazon Elastic Container Registry User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.registry_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="registry_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_text" /></td><td><code>object</code></td><td>The JSON policy text for your registry.</td></tr>
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
registry_id,
policy_text
FROM aws.ecr.registry_policy
WHERE data__Identifier = '<RegistryId>';
```

## Permissions

To operate on the <code>registry_policy</code> resource, the following permissions are required:

### Read
```json
ecr:GetRegistryPolicy
```

### Update
```json
ecr:GetRegistryPolicy,
ecr:PutRegistryPolicy
```

### Delete
```json
ecr:DeleteRegistryPolicy
```

