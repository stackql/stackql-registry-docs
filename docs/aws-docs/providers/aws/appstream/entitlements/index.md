---
title: entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlements
  - appstream
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

Creates, updates, deletes or gets an <code>entitlement</code> resource or lists <code>entitlements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::Entitlement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.entitlements" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_visibility" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html"><code>AWS::AppStream::Entitlement</code></a>.

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
    <td><CopyableCode code="Name, StackName, AppVisibility, Attributes, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>entitlement</code>.
```sql
SELECT
region,
name,
stack_name,
description,
app_visibility,
attributes,
created_time,
last_modified_time
FROM aws.appstream.entitlements
WHERE region = 'us-east-1' AND data__Identifier = '<StackName>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entitlement</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appstream.entitlements (
 Name,
 StackName,
 AppVisibility,
 Attributes,
 region
)
SELECT 
'{{ Name }}',
 '{{ StackName }}',
 '{{ AppVisibility }}',
 '{{ Attributes }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appstream.entitlements (
 Name,
 StackName,
 Description,
 AppVisibility,
 Attributes,
 region
)
SELECT 
 '{{ Name }}',
 '{{ StackName }}',
 '{{ Description }}',
 '{{ AppVisibility }}',
 '{{ Attributes }}',
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
  - name: entitlement
    props:
      - name: Name
        value: '{{ Name }}'
      - name: StackName
        value: '{{ StackName }}'
      - name: Description
        value: '{{ Description }}'
      - name: AppVisibility
        value: '{{ AppVisibility }}'
      - name: Attributes
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appstream.entitlements
WHERE data__Identifier = '<StackName|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>entitlements</code> resource, the following permissions are required:

### Create
```json
appstream:CreateEntitlement
```

### Read
```json
appstream:DescribeEntitlements
```

### Update
```json
appstream:UpdateEntitlement
```

### Delete
```json
appstream:DeleteEntitlement
```
