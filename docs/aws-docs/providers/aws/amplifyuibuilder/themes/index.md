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


Used to retrieve a list of <code>themes</code> in a region or to create or delete a <code>themes</code> resource, use <code>theme</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>themes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Theme Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.themes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
app_id,
environment_name,
id
FROM aws.amplifyuibuilder.themes
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>theme</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- theme.iql (required properties only)
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
-- theme.iql (all properties)
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

## `DELETE` Example

```sql
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

