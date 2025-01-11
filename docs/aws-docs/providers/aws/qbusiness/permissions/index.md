---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - qbusiness
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

Creates, updates, deletes or gets a <code>permission</code> resource or lists <code>permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::Permission Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="statement_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="principal" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html"><code>AWS::QBusiness::Permission</code></a>.

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
    <td><CopyableCode code="ApplicationId, StatementId, Actions, Principal, region" /></td>
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
Gets all <code>permissions</code> in a region.
```sql
SELECT
region,
application_id,
statement_id,
actions,
principal
FROM aws.qbusiness.permissions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>permission</code>.
```sql
SELECT
region,
application_id,
statement_id,
actions,
principal
FROM aws.qbusiness.permissions
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<StatementId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>permission</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.permissions (
 ApplicationId,
 StatementId,
 Actions,
 Principal,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ StatementId }}',
 '{{ Actions }}',
 '{{ Principal }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.permissions (
 ApplicationId,
 StatementId,
 Actions,
 Principal,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ StatementId }}',
 '{{ Actions }}',
 '{{ Principal }}',
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
  - name: permission
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: StatementId
        value: '{{ StatementId }}'
      - name: Actions
        value:
          - '{{ Actions[0] }}'
      - name: Principal
        value: '{{ Principal }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.qbusiness.permissions
WHERE data__Identifier = '<ApplicationId|StatementId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>permissions</code> resource, the following permissions are required:

### Create
```json
qbusiness:AssociatePermission,
qbusiness:PutResourcePolicy
```

### Read
```json
qbusiness:GetPolicy
```

### Delete
```json
qbusiness:DisassociatePermission,
qbusiness:PutResourcePolicy
```

### List
```json
qbusiness:GetPolicy
```
