---
title: option_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - option_groups
  - rds
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


Used to retrieve a list of <code>option_groups</code> in a region or to create or delete a <code>option_groups</code> resource, use <code>option_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>option_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.option_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="option_group_name" /></td><td><code>string</code></td><td>Specifies the name of the option group.</td></tr>
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
    <td><CopyableCode code="EngineName, MajorEngineVersion, OptionGroupDescription, region" /></td>
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
option_group_name
FROM aws.rds.option_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>option_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.option_groups (
 OptionGroupDescription,
 EngineName,
 MajorEngineVersion,
 region
)
SELECT 
'{{ OptionGroupDescription }}',
 '{{ EngineName }}',
 '{{ MajorEngineVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.option_groups (
 OptionGroupName,
 OptionGroupDescription,
 EngineName,
 MajorEngineVersion,
 OptionConfigurations,
 Tags,
 region
)
SELECT 
 '{{ OptionGroupName }}',
 '{{ OptionGroupDescription }}',
 '{{ EngineName }}',
 '{{ MajorEngineVersion }}',
 '{{ OptionConfigurations }}',
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
  - name: option_group
    props:
      - name: OptionGroupName
        value: '{{ OptionGroupName }}'
      - name: OptionGroupDescription
        value: '{{ OptionGroupDescription }}'
      - name: EngineName
        value: '{{ EngineName }}'
      - name: MajorEngineVersion
        value: '{{ MajorEngineVersion }}'
      - name: OptionConfigurations
        value:
          - DBSecurityGroupMemberships:
              - '{{ DBSecurityGroupMemberships[0] }}'
            OptionName: '{{ OptionName }}'
            OptionSettings:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
            OptionVersion: '{{ OptionVersion }}'
            Port: '{{ Port }}'
            VpcSecurityGroupMemberships:
              - '{{ VpcSecurityGroupMemberships[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.rds.option_groups
WHERE data__Identifier = '<OptionGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>option_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:AddTagsToResource,
rds:CreateOptionGroup,
rds:DescribeOptionGroups,
rds:ListTagsForResource,
rds:ModifyOptionGroup,
rds:RemoveTagsFromResource
```

### Delete
```json
rds:DeleteOptionGroup,
rds:DescribeOptionGroups,
rds:ListTagsForResource,
rds:RemoveTagsFromResource
```

### List
```json
rds:DescribeOptionGroups
```

