---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - organizations
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

Creates, updates, deletes or gets an <code>organization</code> resource or lists <code>organizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Organizations::Organization</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.organizations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier (ID) of an organization.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an organization.</td></tr>
<tr><td><CopyableCode code="feature_set" /></td><td><code>string</code></td><td>Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.</td></tr>
<tr><td><CopyableCode code="management_account_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.</td></tr>
<tr><td><CopyableCode code="management_account_id" /></td><td><code>string</code></td><td>The unique identifier (ID) of the management account of an organization.</td></tr>
<tr><td><CopyableCode code="management_account_email" /></td><td><code>string</code></td><td>The email address that is associated with the AWS account that is designated as the management account for the organization.</td></tr>
<tr><td><CopyableCode code="root_id" /></td><td><code>string</code></td><td>The unique identifier (ID) for the root.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html"><code>AWS::Organizations::Organization</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>organizations</code> in a region.
```sql
SELECT
region,
id,
arn,
feature_set,
management_account_arn,
management_account_id,
management_account_email,
root_id
FROM aws.organizations.organizations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>organization</code>.
```sql
SELECT
region,
id,
arn,
feature_set,
management_account_arn,
management_account_id,
management_account_email,
root_id
FROM aws.organizations.organizations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>organization</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.organizations.organizations (
 FeatureSet,
 region
)
SELECT 
'{{ FeatureSet }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.organizations.organizations (
 FeatureSet,
 region
)
SELECT 
 '{{ FeatureSet }}',
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
  - name: organization
    props:
      - name: FeatureSet
        value: '{{ FeatureSet }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.organizations.organizations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>organizations</code> resource, the following permissions are required:

### Create
```json
organizations:CreateOrganization,
organizations:DescribeOrganization,
iam:CreateServiceLinkedRole,
organizations:ListRoots
```

### Read
```json
organizations:DescribeOrganization,
organizations:ListRoots
```

### Delete
```json
organizations:DeleteOrganization,
organizations:DescribeOrganization
```

### List
```json
organizations:DescribeOrganization
```

### Update
```json
organizations:DescribeOrganization
```
