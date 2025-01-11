---
title: organization_admins
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_admins
  - detective
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

Creates, updates, deletes or gets an <code>organization_admin</code> resource or lists <code>organization_admins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Detective::OrganizationAdmin</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.detective.organization_admins" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The account ID of the account that should be registered as your Organization's delegated administrator for Detective</td></tr>
<tr><td><CopyableCode code="graph_arn" /></td><td><code>string</code></td><td>The Detective graph ARN</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html"><code>AWS::Detective::OrganizationAdmin</code></a>.

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
    <td><CopyableCode code="AccountId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>organization_admins</code> in a region.
```sql
SELECT
region,
account_id,
graph_arn
FROM aws.detective.organization_admins
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>organization_admin</code>.
```sql
SELECT
region,
account_id,
graph_arn
FROM aws.detective.organization_admins
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>organization_admin</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.detective.organization_admins (
 AccountId,
 region
)
SELECT 
'{{ AccountId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.detective.organization_admins (
 AccountId,
 region
)
SELECT 
 '{{ AccountId }}',
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
  - name: organization_admin
    props:
      - name: AccountId
        value: '{{ AccountId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.detective.organization_admins
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>organization_admins</code> resource, the following permissions are required:

### Create
```json
detective:EnableOrganizationAdminAccount,
detective:ListOrganizationAdminAccount,
iam:CreateServiceLinkedRole,
organizations:RegisterDelegatedAdministrator,
organizations:DescribeOrganization,
organizations:EnableAWSServiceAccess,
organizations:ListAccounts
```

### Read
```json
detective:ListOrganizationAdminAccount,
organizations:DescribeOrganization
```

### Delete
```json
detective:DisableOrganizationAdminAccount,
detective:ListOrganizationAdminAccount,
organizations:DescribeOrganization
```

### List
```json
detective:ListOrganizationAdminAccount,
organizations:DescribeOrganization
```
