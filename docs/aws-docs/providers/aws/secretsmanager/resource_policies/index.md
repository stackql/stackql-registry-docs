---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - secretsmanager
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

Creates, updates, deletes or gets a <code>resource_policy</code> resource or lists <code>resource_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecretsManager::ResourcePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.secretsmanager.resource_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Arn of the secret.</td></tr>
<tr><td><CopyableCode code="secret_id" /></td><td><code>string</code></td><td>The ARN or name of the secret to attach the resource-based policy.</td></tr>
<tr><td><CopyableCode code="resource_policy" /></td><td><code>object</code></td><td>A JSON-formatted string for an AWS resource-based policy.</td></tr>
<tr><td><CopyableCode code="block_public_policy" /></td><td><code>boolean</code></td><td>Specifies whether to block resource-based policies that allow broad access to the secret.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html"><code>AWS::SecretsManager::ResourcePolicy</code></a>.

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
    <td><CopyableCode code="ResourcePolicy, SecretId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>resource_policies</code> in a region.
```sql
SELECT
region,
id,
secret_id,
resource_policy,
block_public_policy
FROM aws.secretsmanager.resource_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_policy</code>.
```sql
SELECT
region,
id,
secret_id,
resource_policy,
block_public_policy
FROM aws.secretsmanager.resource_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.secretsmanager.resource_policies (
 SecretId,
 ResourcePolicy,
 region
)
SELECT 
'{{ SecretId }}',
 '{{ ResourcePolicy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.secretsmanager.resource_policies (
 SecretId,
 ResourcePolicy,
 BlockPublicPolicy,
 region
)
SELECT 
 '{{ SecretId }}',
 '{{ ResourcePolicy }}',
 '{{ BlockPublicPolicy }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: resource_policy
    props:
      - name: SecretId
        value: '{{ SecretId }}'
      - name: ResourcePolicy
        value: {}
      - name: BlockPublicPolicy
        value: '{{ BlockPublicPolicy }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.secretsmanager.resource_policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
```json
secretsmanager:PutResourcePolicy,
secretsmanager:GetResourcePolicy
```

### Read
```json
secretsmanager:GetResourcePolicy
```

### Update
```json
secretsmanager:PutResourcePolicy,
secretsmanager:GetResourcePolicy
```

### Delete
```json
secretsmanager:DeleteResourcePolicy,
secretsmanager:GetResourcePolicy
```

### List
```json
secretsmanager:GetResourcePolicy,
secretsmanager:ListSecrets
```
