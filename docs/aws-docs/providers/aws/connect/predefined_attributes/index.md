---
title: predefined_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - predefined_attributes
  - connect
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

Creates, updates, deletes or gets a <code>predefined_attribute</code> resource or lists <code>predefined_attributes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predefined_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::PredefinedAttribute</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.predefined_attributes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the predefined attribute.</td></tr>
<tr><td><CopyableCode code="values" /></td><td><code>object</code></td><td>The values of a predefined attribute.</td></tr>
<tr><td><CopyableCode code="last_modified_region" /></td><td><code>string</code></td><td>Last modified region.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>number</code></td><td>Last modified time.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html"><code>AWS::Connect::PredefinedAttribute</code></a>.

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
    <td><CopyableCode code="InstanceArn, Name, Values, region" /></td>
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
Gets all <code>predefined_attributes</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
values,
last_modified_region,
last_modified_time
FROM aws.connect.predefined_attributes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>predefined_attribute</code>.
```sql
SELECT
region,
instance_arn,
name,
values,
last_modified_region,
last_modified_time
FROM aws.connect.predefined_attributes
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceArn>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>predefined_attribute</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.predefined_attributes (
 InstanceArn,
 Name,
 Values,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Values }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.predefined_attributes (
 InstanceArn,
 Name,
 Values,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Values }}',
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
  - name: predefined_attribute
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Values
        value:
          StringList:
            - '{{ StringList[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.predefined_attributes
WHERE data__Identifier = '<InstanceArn|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>predefined_attributes</code> resource, the following permissions are required:

### Create
```json
connect:CreatePredefinedAttribute
```

### Read
```json
connect:DescribePredefinedAttribute
```

### Delete
```json
connect:DeletePredefinedAttribute
```

### Update
```json
connect:UpdatePredefinedAttribute
```

### List
```json
connect:ListPredefinedAttributes
```
