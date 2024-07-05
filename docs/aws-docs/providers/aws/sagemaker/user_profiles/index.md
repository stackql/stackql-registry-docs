---
title: user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles
  - sagemaker
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

Creates, updates, deletes or gets an <code>user_profile</code> resource or lists <code>user_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::UserProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.user_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_profile_arn" /></td><td><code>string</code></td><td>The user profile Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><CopyableCode code="single_sign_on_user_identifier" /></td><td><code>string</code></td><td>A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><CopyableCode code="single_sign_on_user_value" /></td><td><code>string</code></td><td>The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><CopyableCode code="user_profile_name" /></td><td><code>string</code></td><td>A name for the UserProfile.</td></tr>
<tr><td><CopyableCode code="user_settings" /></td><td><code>object</code></td><td>A collection of settings.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the user profile.</td></tr>
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
    <td><CopyableCode code="DomainId, UserProfileName, region" /></td>
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
Gets all <code>user_profiles</code> in a region.
```sql
SELECT
region,
user_profile_arn,
domain_id,
single_sign_on_user_identifier,
single_sign_on_user_value,
user_profile_name,
user_settings,
tags
FROM aws.sagemaker.user_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_profile</code>.
```sql
SELECT
region,
user_profile_arn,
domain_id,
single_sign_on_user_identifier,
single_sign_on_user_value,
user_profile_name,
user_settings,
tags
FROM aws.sagemaker.user_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<UserProfileName>|<DomainId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.user_profiles (
 DomainId,
 UserProfileName,
 region
)
SELECT 
'{{ DomainId }}',
 '{{ UserProfileName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.user_profiles (
 DomainId,
 SingleSignOnUserIdentifier,
 SingleSignOnUserValue,
 UserProfileName,
 UserSettings,
 Tags,
 region
)
SELECT 
 '{{ DomainId }}',
 '{{ SingleSignOnUserIdentifier }}',
 '{{ SingleSignOnUserValue }}',
 '{{ UserProfileName }}',
 '{{ UserSettings }}',
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
  - name: user_profile
    props:
      - name: DomainId
        value: '{{ DomainId }}'
      - name: SingleSignOnUserIdentifier
        value: '{{ SingleSignOnUserIdentifier }}'
      - name: SingleSignOnUserValue
        value: '{{ SingleSignOnUserValue }}'
      - name: UserProfileName
        value: '{{ UserProfileName }}'
      - name: UserSettings
        value:
          ExecutionRole: '{{ ExecutionRole }}'
          JupyterServerAppSettings:
            DefaultResourceSpec:
              InstanceType: '{{ InstanceType }}'
              SageMakerImageArn: '{{ SageMakerImageArn }}'
              SageMakerImageVersionArn: '{{ SageMakerImageVersionArn }}'
          KernelGatewayAppSettings:
            CustomImages:
              - AppImageConfigName: '{{ AppImageConfigName }}'
                ImageName: '{{ ImageName }}'
                ImageVersionNumber: '{{ ImageVersionNumber }}'
            DefaultResourceSpec: null
          RStudioServerProAppSettings:
            AccessStatus: '{{ AccessStatus }}'
            UserGroup: '{{ UserGroup }}'
          JupyterLabAppSettings:
            DefaultResourceSpec: null
            LifecycleConfigArns:
              - '{{ LifecycleConfigArns[0] }}'
            CodeRepositories:
              - RepositoryUrl: '{{ RepositoryUrl }}'
            CustomImages:
              - null
          SpaceStorageSettings:
            DefaultEbsStorageSettings:
              DefaultEbsVolumeSizeInGb: '{{ DefaultEbsVolumeSizeInGb }}'
              MaximumEbsVolumeSizeInGb: null
          CodeEditorAppSettings:
            DefaultResourceSpec: null
            LifecycleConfigArns:
              - null
            CustomImages:
              - null
          DefaultLandingUri: '{{ DefaultLandingUri }}'
          StudioWebPortal: '{{ StudioWebPortal }}'
          CustomPosixUserConfig:
            Uid: '{{ Uid }}'
            Gid: '{{ Gid }}'
          CustomFileSystemConfigs:
            - EFSFileSystemConfig:
                FileSystemPath: '{{ FileSystemPath }}'
                FileSystemId: '{{ FileSystemId }}'
          SecurityGroups:
            - '{{ SecurityGroups[0] }}'
          SharingSettings:
            NotebookOutputOption: '{{ NotebookOutputOption }}'
            S3KmsKeyId: '{{ S3KmsKeyId }}'
            S3OutputPath: '{{ S3OutputPath }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.user_profiles
WHERE data__Identifier = '<UserProfileName|DomainId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_profiles</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateUserProfile,
sagemaker:DescribeUserProfile,
sagemaker:DescribeImage,
sagemaker:DescribeImageVersion,
iam:PassRole
```

### Read
```json
sagemaker:DescribeUserProfile
```

### Update
```json
sagemaker:UpdateUserProfile,
sagemaker:DescribeUserProfile,
sagemaker:DescribeImage,
sagemaker:DescribeImageVersion,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteUserProfile,
sagemaker:DescribeUserProfile
```

### List
```json
sagemaker:ListUserProfiles
```

