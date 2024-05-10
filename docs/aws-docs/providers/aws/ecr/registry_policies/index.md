---
title: registry_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policies
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>registry_policies</code> in a region or to create or delete a <code>registry_policies</code> resource, use <code>registry_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ECR::RegistryPolicy`` resource creates or updates the permissions policy for a private registry.&lt;br&#x2F;&gt; A private registry policy is used to specify permissions for another AWS-account and is used when configuring cross-account replication. For more information, see &#91;Registry permissions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;registry-permissions.html) in the *Amazon Elastic Container Registry User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.registry_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="registry_id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
registry_id
FROM aws.ecr.registry_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "PolicyText": {}
}
>>>
--required properties only
INSERT INTO aws.ecr.registry_policies (
 PolicyText,
 region
)
SELECT 
{{ PolicyText }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PolicyText": {}
}
>>>
--all properties
INSERT INTO aws.ecr.registry_policies (
 PolicyText,
 region
)
SELECT 
 {{ PolicyText }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ecr.registry_policies
WHERE data__Identifier = '<RegistryId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>registry_policies</code> resource, the following permissions are required:

### Create
```json
ecr:GetRegistryPolicy,
ecr:PutRegistryPolicy
```

### List
```json
ecr:GetRegistryPolicy
```

### Delete
```json
ecr:DeleteRegistryPolicy
```

