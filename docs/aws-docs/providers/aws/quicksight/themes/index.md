---
title: themes
hide_title: false
hide_table_of_contents: false
keywords:
  - themes
  - quicksight
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
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Theme Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.themes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the theme.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="base_theme_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code><p>The theme configuration. This configuration contains all of the display properties for
            a theme.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The date and time that the theme was created.</p></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The date and time that the theme was last updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="theme_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code><p>A version of a theme.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="AwsAccountId, ThemeId, BaseThemeId, Configuration, Name, region" /></td>
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
theme_id,
aws_account_id
FROM aws.quicksight.themes
WHERE region = 'us-east-1';
```
Gets all properties from a <code>theme</code>.
```sql
SELECT
region,
arn,
aws_account_id,
base_theme_id,
configuration,
created_time,
last_updated_time,
name,
permissions,
tags,
theme_id,
type,
version,
version_description
FROM aws.quicksight.themes
WHERE region = 'us-east-1' AND data__Identifier = '<ThemeId>|<AwsAccountId>';
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
INSERT INTO aws.quicksight.themes (
 AwsAccountId,
 BaseThemeId,
 Configuration,
 Name,
 ThemeId,
 region
)
SELECT 
'{{ AwsAccountId }}',
 '{{ BaseThemeId }}',
 '{{ Configuration }}',
 '{{ Name }}',
 '{{ ThemeId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.themes (
 AwsAccountId,
 BaseThemeId,
 Configuration,
 Name,
 Permissions,
 Tags,
 ThemeId,
 VersionDescription,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ BaseThemeId }}',
 '{{ Configuration }}',
 '{{ Name }}',
 '{{ Permissions }}',
 '{{ Tags }}',
 '{{ ThemeId }}',
 '{{ VersionDescription }}',
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
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: BaseThemeId
        value: '{{ BaseThemeId }}'
      - name: Configuration
        value:
          DataColorPalette:
            Colors:
              - '{{ Colors[0] }}'
            MinMaxGradient:
              - '{{ MinMaxGradient[0] }}'
            EmptyFillColor: '{{ EmptyFillColor }}'
          UIColorPalette:
            PrimaryForeground: '{{ PrimaryForeground }}'
            PrimaryBackground: '{{ PrimaryBackground }}'
            SecondaryForeground: '{{ SecondaryForeground }}'
            SecondaryBackground: '{{ SecondaryBackground }}'
            Accent: '{{ Accent }}'
            AccentForeground: '{{ AccentForeground }}'
            Danger: '{{ Danger }}'
            DangerForeground: '{{ DangerForeground }}'
            Warning: '{{ Warning }}'
            WarningForeground: '{{ WarningForeground }}'
            Success: '{{ Success }}'
            SuccessForeground: '{{ SuccessForeground }}'
            Dimension: '{{ Dimension }}'
            DimensionForeground: '{{ DimensionForeground }}'
            Measure: '{{ Measure }}'
            MeasureForeground: '{{ MeasureForeground }}'
          Sheet:
            Tile:
              Border:
                Show: '{{ Show }}'
            TileLayout:
              Gutter:
                Show: '{{ Show }}'
              Margin:
                Show: '{{ Show }}'
          Typography:
            FontFamilies:
              - FontFamily: '{{ FontFamily }}'
      - name: Name
        value: '{{ Name }}'
      - name: Permissions
        value:
          - Principal: '{{ Principal }}'
            Actions:
              - '{{ Actions[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ThemeId
        value: '{{ ThemeId }}'
      - name: VersionDescription
        value: '{{ VersionDescription }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.quicksight.themes
WHERE data__Identifier = '<ThemeId|AwsAccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>themes</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeTheme,
quicksight:DescribeThemePermissions,
quicksight:ListTagsForResource
```

### Create
```json
quicksight:DescribeTheme,
quicksight:DescribeThemePermissions,
quicksight:CreateTheme,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### List
```json
quicksight:ListThemes
```

### Update
```json
quicksight:DescribeTheme,
quicksight:DescribeThemePermissions,
quicksight:UpdateTheme,
quicksight:UpdateThemePermissions,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DescribeTheme,
quicksight:DeleteTheme
```

