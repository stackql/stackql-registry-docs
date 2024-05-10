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


Used to retrieve a list of <code>themes</code> in a region or to create or delete a <code>themes</code> resource, use <code>theme</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>themes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Theme Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.themes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="theme_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
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
theme_id,
aws_account_id
FROM aws.quicksight.themes
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AwsAccountId": "{{ AwsAccountId }}",
 "BaseThemeId": "{{ BaseThemeId }}",
 "Configuration": {
  "DataColorPalette": {
   "Colors": [
    "{{ Colors[0] }}"
   ],
   "MinMaxGradient": [
    "{{ MinMaxGradient[0] }}"
   ],
   "EmptyFillColor": "{{ EmptyFillColor }}"
  },
  "UIColorPalette": {
   "PrimaryForeground": "{{ PrimaryForeground }}",
   "PrimaryBackground": "{{ PrimaryBackground }}",
   "SecondaryForeground": "{{ SecondaryForeground }}",
   "SecondaryBackground": "{{ SecondaryBackground }}",
   "Accent": "{{ Accent }}",
   "AccentForeground": "{{ AccentForeground }}",
   "Danger": "{{ Danger }}",
   "DangerForeground": "{{ DangerForeground }}",
   "Warning": "{{ Warning }}",
   "WarningForeground": "{{ WarningForeground }}",
   "Success": "{{ Success }}",
   "SuccessForeground": "{{ SuccessForeground }}",
   "Dimension": "{{ Dimension }}",
   "DimensionForeground": "{{ DimensionForeground }}",
   "Measure": "{{ Measure }}",
   "MeasureForeground": "{{ MeasureForeground }}"
  },
  "Sheet": {
   "Tile": {
    "Border": {
     "Show": "{{ Show }}"
    }
   },
   "TileLayout": {
    "Gutter": {
     "Show": "{{ Show }}"
    },
    "Margin": {
     "Show": "{{ Show }}"
    }
   }
  },
  "Typography": {
   "FontFamilies": [
    {
     "FontFamily": "{{ FontFamily }}"
    }
   ]
  }
 },
 "Name": "{{ Name }}",
 "ThemeId": "{{ ThemeId }}"
}
>>>
--required properties only
INSERT INTO aws.quicksight.themes (
 AwsAccountId,
 BaseThemeId,
 Configuration,
 Name,
 ThemeId,
 region
)
SELECT 
{{ .AwsAccountId }},
 {{ .BaseThemeId }},
 {{ .Configuration }},
 {{ .Name }},
 {{ .ThemeId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AwsAccountId": "{{ AwsAccountId }}",
 "BaseThemeId": "{{ BaseThemeId }}",
 "Configuration": {
  "DataColorPalette": {
   "Colors": [
    "{{ Colors[0] }}"
   ],
   "MinMaxGradient": [
    "{{ MinMaxGradient[0] }}"
   ],
   "EmptyFillColor": "{{ EmptyFillColor }}"
  },
  "UIColorPalette": {
   "PrimaryForeground": "{{ PrimaryForeground }}",
   "PrimaryBackground": "{{ PrimaryBackground }}",
   "SecondaryForeground": "{{ SecondaryForeground }}",
   "SecondaryBackground": "{{ SecondaryBackground }}",
   "Accent": "{{ Accent }}",
   "AccentForeground": "{{ AccentForeground }}",
   "Danger": "{{ Danger }}",
   "DangerForeground": "{{ DangerForeground }}",
   "Warning": "{{ Warning }}",
   "WarningForeground": "{{ WarningForeground }}",
   "Success": "{{ Success }}",
   "SuccessForeground": "{{ SuccessForeground }}",
   "Dimension": "{{ Dimension }}",
   "DimensionForeground": "{{ DimensionForeground }}",
   "Measure": "{{ Measure }}",
   "MeasureForeground": "{{ MeasureForeground }}"
  },
  "Sheet": {
   "Tile": {
    "Border": {
     "Show": "{{ Show }}"
    }
   },
   "TileLayout": {
    "Gutter": {
     "Show": "{{ Show }}"
    },
    "Margin": {
     "Show": "{{ Show }}"
    }
   }
  },
  "Typography": {
   "FontFamilies": [
    {
     "FontFamily": "{{ FontFamily }}"
    }
   ]
  }
 },
 "Name": "{{ Name }}",
 "Permissions": [
  {
   "Principal": "{{ Principal }}",
   "Actions": [
    "{{ Actions[0] }}"
   ]
  }
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "ThemeId": "{{ ThemeId }}",
 "VersionDescription": "{{ VersionDescription }}"
}
>>>
--all properties
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
 {{ .AwsAccountId }},
 {{ .BaseThemeId }},
 {{ .Configuration }},
 {{ .Name }},
 {{ .Permissions }},
 {{ .Tags }},
 {{ .ThemeId }},
 {{ .VersionDescription }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.quicksight.themes
WHERE data__Identifier = '<ThemeId|AwsAccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>themes</code> resource, the following permissions are required:

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

### Delete
```json
quicksight:DescribeTheme,
quicksight:DeleteTheme
```

