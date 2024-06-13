---
title: themes
hide_title: false
hide_table_of_contents: false
keywords:
  - themes
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

Creates, updates, deletes or gets a <code>theme</code> resource or lists <code>themes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>themes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Theme Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.themes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="overrides" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="values" /></td><td><code>array</code></td><td></td></tr>
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
List all <code>themes</code> in a region.
```sql
SELECT
region,
app_id,
environment_name,
id
FROM aws.amplifyuibuilder.themes
WHERE region = 'us-east-1';
```
Gets all properties from a <code>theme</code>.
```sql
SELECT
region,
app_id,
created_at,
environment_name,
id,
modified_at,
name,
overrides,
tags,
values
FROM aws.amplifyuibuilder.themes
WHERE region = 'us-east-1' AND data__Identifier = '<AppId>|<EnvironmentName>|<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>theme</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.amplifyuibuilder.themes (
 AppId,
 EnvironmentName,
 Name,
 Overrides,
 Tags,
 Values,
 region
)
SELECT 
'{{ AppId }}',
 '{{ EnvironmentName }}',
 '{{ Name }}',
 '{{ Overrides }}',
 '{{ Tags }}',
 '{{ Values }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.amplifyuibuilder.themes (
 AppId,
 EnvironmentName,
 Name,
 Overrides,
 Tags,
 Values,
 region
)
SELECT 
 '{{ AppId }}',
 '{{ EnvironmentName }}',
 '{{ Name }}',
 '{{ Overrides }}',
 '{{ Tags }}',
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
  - name: theme
    props:
      - name: AppId
        value: '{{ AppId }}'
      - name: EnvironmentName
        value: '{{ EnvironmentName }}'
      - name: Name
        value: '{{ Name }}'
      - name: Overrides
        value:
          - Key: '{{ Key }}'
            Value:
              Value: '{{ Value }}'
              Children:
                - null
      - name: Tags
        value: {}
      - name: Values
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.amplifyuibuilder.themes
WHERE data__Identifier = '<AppId|EnvironmentName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>themes</code> resource, the following permissions are required:

### Create
```json
amplify:GetApp,
amplifyuibuilder:CreateTheme,
amplifyuibuilder:GetTheme,
amplifyuibuilder:TagResource
```

### Read
```json
amplify:GetApp,
amplifyuibuilder:GetTheme
```

### Update
```json
amplify:GetApp,
amplifyuibuilder:GetTheme,
amplifyuibuilder:TagResource,
amplifyuibuilder:UntagResource,
amplifyuibuilder:UpdateTheme
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteTheme,
amplifyuibuilder:UntagResource
```

### List
```json
amplify:GetApp,
amplifyuibuilder:ListThemes
```

