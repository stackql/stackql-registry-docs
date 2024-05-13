---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - emr
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


Used to retrieve a list of <code>studios</code> in a region or to create or delete a <code>studios</code> resource, use <code>studio</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMR::Studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studios" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>The ID of the EMR Studio.</td></tr>
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
    <td><CopyableCode code="AuthMode, EngineSecurityGroupId, Name, ServiceRole, SubnetIds, VpcId, WorkspaceSecurityGroupId, DefaultS3Location, region" /></td>
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
studio_id
FROM aws.emr.studios
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>studio</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.emr.studios (
 AuthMode,
 DefaultS3Location,
 EngineSecurityGroupId,
 Name,
 ServiceRole,
 SubnetIds,
 VpcId,
 WorkspaceSecurityGroupId,
 region
)
SELECT 
'{{ AuthMode }}',
 '{{ DefaultS3Location }}',
 '{{ EngineSecurityGroupId }}',
 '{{ Name }}',
 '{{ ServiceRole }}',
 '{{ SubnetIds }}',
 '{{ VpcId }}',
 '{{ WorkspaceSecurityGroupId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.emr.studios (
 AuthMode,
 DefaultS3Location,
 Description,
 EngineSecurityGroupId,
 Name,
 ServiceRole,
 SubnetIds,
 Tags,
 UserRole,
 VpcId,
 WorkspaceSecurityGroupId,
 IdpAuthUrl,
 IdpRelayStateParameterName,
 TrustedIdentityPropagationEnabled,
 IdcUserAssignment,
 IdcInstanceArn,
 EncryptionKeyArn,
 region
)
SELECT 
 '{{ AuthMode }}',
 '{{ DefaultS3Location }}',
 '{{ Description }}',
 '{{ EngineSecurityGroupId }}',
 '{{ Name }}',
 '{{ ServiceRole }}',
 '{{ SubnetIds }}',
 '{{ Tags }}',
 '{{ UserRole }}',
 '{{ VpcId }}',
 '{{ WorkspaceSecurityGroupId }}',
 '{{ IdpAuthUrl }}',
 '{{ IdpRelayStateParameterName }}',
 '{{ TrustedIdentityPropagationEnabled }}',
 '{{ IdcUserAssignment }}',
 '{{ IdcInstanceArn }}',
 '{{ EncryptionKeyArn }}',
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
  - name: studio
    props:
      - name: AuthMode
        value: '{{ AuthMode }}'
      - name: DefaultS3Location
        value: '{{ DefaultS3Location }}'
      - name: Description
        value: '{{ Description }}'
      - name: EngineSecurityGroupId
        value: '{{ EngineSecurityGroupId }}'
      - name: Name
        value: '{{ Name }}'
      - name: ServiceRole
        value: '{{ ServiceRole }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UserRole
        value: null
      - name: VpcId
        value: '{{ VpcId }}'
      - name: WorkspaceSecurityGroupId
        value: '{{ WorkspaceSecurityGroupId }}'
      - name: IdpAuthUrl
        value: '{{ IdpAuthUrl }}'
      - name: IdpRelayStateParameterName
        value: '{{ IdpRelayStateParameterName }}'
      - name: TrustedIdentityPropagationEnabled
        value: '{{ TrustedIdentityPropagationEnabled }}'
      - name: IdcUserAssignment
        value: '{{ IdcUserAssignment }}'
      - name: IdcInstanceArn
        value: '{{ IdcInstanceArn }}'
      - name: EncryptionKeyArn
        value: null

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.emr.studios
WHERE data__Identifier = '<StudioId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>studios</code> resource, the following permissions are required:

### Create
```json
elasticmapreduce:CreateStudio,
elasticmapreduce:DescribeStudio,
elasticmapreduce:AddTags,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
iam:PassRole
```

### Delete
```json
elasticmapreduce:DeleteStudio,
elasticmapreduce:DescribeStudio,
sso:DeleteManagedApplicationInstance
```

### List
```json
elasticmapreduce:ListStudios
```

