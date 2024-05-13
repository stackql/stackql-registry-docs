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


Used to retrieve a list of <code>studio_components</code> in a region or to create or delete a <code>studio_components</code> resource, use <code>studio_component</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio component that connects a non-Nimble Studio resource in your account to your studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studio_components" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_component_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
studio_component_id,
studio_id
FROM aws.nimblestudio.studio_components
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

