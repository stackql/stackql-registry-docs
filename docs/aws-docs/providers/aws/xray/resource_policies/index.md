---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - xray
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
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay Resource Policy resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.resource_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the resource policy. Must be unique within a specific AWS account.</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>string</code></td><td>The resource policy document, which can be up to 5kb in size.</td></tr>
<tr><td><CopyableCode code="bypass_policy_lockout_check" /></td><td><code>boolean</code></td><td>A flag to indicate whether to bypass the resource policy lockout safety check</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html"><code>AWS::XRay::ResourcePolicy</code></a>.

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
    <td><CopyableCode code="PolicyName, PolicyDocument, region" /></td>
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
policy_name,
policy_document,
bypass_policy_lockout_check
FROM aws.xray.resource_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_policy</code>.
```sql
SELECT
region,
policy_name,
policy_document,
bypass_policy_lockout_check
FROM aws.xray.resource_policies
WHERE region = 'us-east-1' AND data__Identifier = '<PolicyName>';
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
INSERT INTO aws.xray.resource_policies (
 PolicyName,
 PolicyDocument,
 region
)
SELECT 
'{{ PolicyName }}',
 '{{ PolicyDocument }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.xray.resource_policies (
 PolicyName,
 PolicyDocument,
 BypassPolicyLockoutCheck,
 region
)
SELECT 
 '{{ PolicyName }}',
 '{{ PolicyDocument }}',
 '{{ BypassPolicyLockoutCheck }}',
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
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: PolicyDocument
        value: '{{ PolicyDocument }}'
      - name: BypassPolicyLockoutCheck
        value: '{{ BypassPolicyLockoutCheck }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.xray.resource_policies
WHERE data__Identifier = '<PolicyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
```json
xray:PutResourcePolicy,
xray:ListResourcePolicies
```

### Read
```json
xray:ListResourcePolicies
```

### Update
```json
xray:PutResourcePolicy,
xray:ListResourcePolicies
```

### Delete
```json
xray:DeleteResourcePolicy
```

### List
```json
xray:ListResourcePolicies
```
