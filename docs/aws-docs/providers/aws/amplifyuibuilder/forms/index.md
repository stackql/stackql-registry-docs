---
title: forms
hide_title: false
hide_table_of_contents: false
keywords:
  - forms
  - amplifyuibuilder
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

Creates, updates, deletes or gets a <code>form</code> resource or lists <code>forms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Form Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.forms" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cta" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="form_action_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="label_decorator" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sectional_elements" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="style" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>forms</code> in a region.
```sql
SELECT
region,
app_id,
environment_name,
id
FROM aws.amplifyuibuilder.forms
WHERE region = 'us-east-1';
```
Gets all properties from a <code>form</code>.
```sql
SELECT
region,
app_id,
cta,
data_type,
environment_name,
fields,
form_action_type,
id,
label_decorator,
name,
schema_version,
sectional_elements,
style,
tags
FROM aws.amplifyuibuilder.forms
WHERE region = 'us-east-1' AND data__Identifier = '<AppId>|<EnvironmentName>|<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>form</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.amplifyuibuilder.forms (
 AppId,
 Cta,
 DataType,
 EnvironmentName,
 Fields,
 FormActionType,
 LabelDecorator,
 Name,
 SchemaVersion,
 SectionalElements,
 Style,
 Tags,
 region
)
SELECT 
'{{ AppId }}',
 '{{ Cta }}',
 '{{ DataType }}',
 '{{ EnvironmentName }}',
 '{{ Fields }}',
 '{{ FormActionType }}',
 '{{ LabelDecorator }}',
 '{{ Name }}',
 '{{ SchemaVersion }}',
 '{{ SectionalElements }}',
 '{{ Style }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.amplifyuibuilder.forms (
 AppId,
 Cta,
 DataType,
 EnvironmentName,
 Fields,
 FormActionType,
 LabelDecorator,
 Name,
 SchemaVersion,
 SectionalElements,
 Style,
 Tags,
 region
)
SELECT 
 '{{ AppId }}',
 '{{ Cta }}',
 '{{ DataType }}',
 '{{ EnvironmentName }}',
 '{{ Fields }}',
 '{{ FormActionType }}',
 '{{ LabelDecorator }}',
 '{{ Name }}',
 '{{ SchemaVersion }}',
 '{{ SectionalElements }}',
 '{{ Style }}',
 '{{ Tags }}',
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
  - name: form
    props:
      - name: AppId
        value: '{{ AppId }}'
      - name: Cta
        value:
          Position: '{{ Position }}'
          Clear:
            Excluded: '{{ Excluded }}'
            Children: '{{ Children }}'
            Position: null
          Cancel: null
          Submit: null
      - name: DataType
        value:
          DataSourceType: '{{ DataSourceType }}'
          DataTypeName: '{{ DataTypeName }}'
      - name: EnvironmentName
        value: '{{ EnvironmentName }}'
      - name: Fields
        value: {}
      - name: FormActionType
        value: '{{ FormActionType }}'
      - name: LabelDecorator
        value: '{{ LabelDecorator }}'
      - name: Name
        value: '{{ Name }}'
      - name: SchemaVersion
        value: '{{ SchemaVersion }}'
      - name: SectionalElements
        value: {}
      - name: Style
        value:
          HorizontalGap: null
          VerticalGap: null
          OuterPadding: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.amplifyuibuilder.forms
WHERE data__Identifier = '<AppId|EnvironmentName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>forms</code> resource, the following permissions are required:

### Create
```json
amplify:GetApp,
amplifyuibuilder:CreateForm,
amplifyuibuilder:GetForm,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource
```

### Read
```json
amplify:GetApp,
amplifyuibuilder:GetForm,
amplifyuibuilder:TagResource
```

### Update
```json
amplify:GetApp,
amplifyuibuilder:GetForm,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource,
amplifyuibuilder:UpdateForm
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteForm,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource
```

### List
```json
amplify:GetApp,
amplifyuibuilder:ListForms
```

