---
title: parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - parameters
  - ssm
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

Creates, updates, deletes or gets a <code>parameter</code> resource or lists <code>parameters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SSM::Parameter</code> resource creates an SSM parameter in SYSlong Parameter Store.<br/>  To create an SSM parameter, you must have the IAMlong (IAM) permissions <code>ssm:PutParameter</code> and <code>ssm:AddTagsToResource</code>. On stack creation, CFNlong adds the following three tags to the parameter: <code>aws:cloudformation:stack-name</code>, <code>aws:cloudformation:logical-id</code>, and <code>aws:cloudformation:stack-id</code>, in addition to any custom tags you specify.<br/> To add, update, or remove tags during stack update, you must have IAM permissions for both <code>ssm:AddTagsToResource</code> and <code>ssm:RemoveTagsFromResource</code>. For more information, see &#91;Managing Access Using Policies&#93;(https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html#security_iam_access-manage) in the *User Guide*.<br/>  For information about valid values for parameters, see &#91;About requirements and constraints for parameter names&#93;(https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html#sysman-parameter-name-constraints) in the *User Guide* and &#91;PutParameter&#93;(https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html) in the *API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.parameters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of parameter.</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>The parameter value.<br/>  If type is <code>StringList</code>, the system returns a comma-separated string with no spaces between commas in the <code>Value</code> field.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Information about the parameter.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>string</code></td><td>Information about the policies assigned to a parameter.<br/>  &#91;Assigning parameter policies&#93;(https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="allowed_pattern" /></td><td><code>string</code></td><td>A regular expression used to validate the parameter value. For example, for <code>String</code> types with values restricted to numbers, you can specify the following: <code>AllowedPattern=^\d+$</code></td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>The parameter tier.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a SYS parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.</td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>string</code></td><td>The data type of the parameter, such as <code>text</code> or <code>aws:ec2:image</code>. The default is <code>text</code>.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the parameter.<br/>  The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: <code>arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName</code></td></tr>
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
    <td><CopyableCode code="Value, Type, region" /></td>
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
List all <code>parameters</code> in a region.
```sql
SELECT
region,
name
FROM aws.ssm.parameters
WHERE region = 'us-east-1';
```
Gets all properties from a <code>parameter</code>.
```sql
SELECT
region,
type,
value,
description,
policies,
allowed_pattern,
tier,
tags,
data_type,
name
FROM aws.ssm.parameters
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>parameter</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssm.parameters (
 Type,
 Value,
 region
)
SELECT 
'{{ Type }}',
 '{{ Value }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssm.parameters (
 Type,
 Value,
 Description,
 Policies,
 AllowedPattern,
 Tier,
 Tags,
 DataType,
 Name,
 region
)
SELECT 
 '{{ Type }}',
 '{{ Value }}',
 '{{ Description }}',
 '{{ Policies }}',
 '{{ AllowedPattern }}',
 '{{ Tier }}',
 '{{ Tags }}',
 '{{ DataType }}',
 '{{ Name }}',
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
  - name: parameter
    props:
      - name: Type
        value: '{{ Type }}'
      - name: Value
        value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'
      - name: Policies
        value: '{{ Policies }}'
      - name: AllowedPattern
        value: '{{ AllowedPattern }}'
      - name: Tier
        value: '{{ Tier }}'
      - name: Tags
        value: {}
      - name: DataType
        value: '{{ DataType }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssm.parameters
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>parameters</code> resource, the following permissions are required:

### Create
```json
ssm:PutParameter,
ssm:AddTagsToResource,
ssm:GetParameters
```

### Read
```json
ssm:GetParameters
```

### Update
```json
ssm:PutParameter,
ssm:AddTagsToResource,
ssm:RemoveTagsFromResource,
ssm:GetParameters
```

### Delete
```json
ssm:DeleteParameter
```

### List
```json
ssm:DescribeParameters
```

