---
title: studio_components
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_components
  - nimblestudio
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

Creates, updates, deletes or gets a <code>studio_component</code> resource or lists <code>studio_components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio component that connects a non-Nimble Studio resource in your account to your studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studio_components" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td><p>The configuration of the studio component, based on component type.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>The description.</p></td></tr>
<tr><td><CopyableCode code="ec2_security_group_ids" /></td><td><code>array</code></td><td><p>The EC2 security groups that control access to the studio component.</p></td></tr>
<tr><td><CopyableCode code="initialization_scripts" /></td><td><code>array</code></td><td><p>Initialization scripts for studio components.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td><p>The name for the studio component.</p></td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="script_parameters" /></td><td><code>array</code></td><td><p>Parameters for the studio component scripts.</p></td></tr>
<tr><td><CopyableCode code="secure_initialization_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_component_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td><p>The studio ID. </p></td></tr>
<tr><td><CopyableCode code="subtype" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="StudioId, Name, Type, region" /></td>
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
Gets all <code>studio_components</code> in a region.
```sql
SELECT
region,
configuration,
description,
ec2_security_group_ids,
initialization_scripts,
name,
runtime_role_arn,
script_parameters,
secure_initialization_role_arn,
studio_component_id,
studio_id,
subtype,
tags,
type
FROM aws.nimblestudio.studio_components
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>studio_component</code>.
```sql
SELECT
region,
configuration,
description,
ec2_security_group_ids,
initialization_scripts,
name,
runtime_role_arn,
script_parameters,
secure_initialization_role_arn,
studio_component_id,
studio_id,
subtype,
tags,
type
FROM aws.nimblestudio.studio_components
WHERE region = 'us-east-1' AND data__Identifier = '<StudioComponentId>|<StudioId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>studio_component</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.nimblestudio.studio_components (
 Name,
 StudioId,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ StudioId }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.nimblestudio.studio_components (
 Configuration,
 Description,
 Ec2SecurityGroupIds,
 InitializationScripts,
 Name,
 RuntimeRoleArn,
 ScriptParameters,
 SecureInitializationRoleArn,
 StudioId,
 Subtype,
 Tags,
 Type,
 region
)
SELECT 
 '{{ Configuration }}',
 '{{ Description }}',
 '{{ Ec2SecurityGroupIds }}',
 '{{ InitializationScripts }}',
 '{{ Name }}',
 '{{ RuntimeRoleArn }}',
 '{{ ScriptParameters }}',
 '{{ SecureInitializationRoleArn }}',
 '{{ StudioId }}',
 '{{ Subtype }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: studio_component
    props:
      - name: Configuration
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: Ec2SecurityGroupIds
        value:
          - '{{ Ec2SecurityGroupIds[0] }}'
      - name: InitializationScripts
        value:
          - LaunchProfileProtocolVersion: '{{ LaunchProfileProtocolVersion }}'
            Platform: '{{ Platform }}'
            RunContext: '{{ RunContext }}'
            Script: '{{ Script }}'
      - name: Name
        value: '{{ Name }}'
      - name: RuntimeRoleArn
        value: '{{ RuntimeRoleArn }}'
      - name: ScriptParameters
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: SecureInitializationRoleArn
        value: '{{ SecureInitializationRoleArn }}'
      - name: StudioId
        value: '{{ StudioId }}'
      - name: Subtype
        value: '{{ Subtype }}'
      - name: Tags
        value: {}
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.nimblestudio.studio_components
WHERE data__Identifier = '<StudioComponentId|StudioId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>studio_components</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
nimble:CreateStudioComponent,
nimble:GetStudioComponent,
nimble:TagResource,
ds:AuthorizeApplication,
ec2:DescribeSecurityGroups,
fsx:DescribeFilesystems,
ds:DescribeDirectories
```

### Read
```json
nimble:GetStudioComponent
```

### Update
```json
iam:PassRole,
nimble:UpdateStudioComponent,
nimble:GetStudioComponent,
ds:AuthorizeApplication,
ec2:DescribeSecurityGroups,
fsx:DescribeFilesystems,
ds:DescribeDirectories
```

### Delete
```json
nimble:DeleteStudioComponent,
nimble:GetStudioComponent,
nimble:UntagResource,
ds:UnauthorizeApplication
```

### List
```json
nimble:ListStudioComponents
```

