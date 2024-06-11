---
title: configuration_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles
  - appconfig
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

Creates, updates, deletes or gets a <code>configuration_profile</code> resource or lists <code>configuration_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.configuration_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>A URI to locate the configuration. You can specify the AWS AppConfig hosted configuration store, Systems Manager (SSM) document, an SSM Parameter Store parameter, or an Amazon S3 object.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of configurations contained in the profile. When calling this API, enter one of the following values for Type: AWS.AppConfig.FeatureFlags, AWS.Freeform</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the configuration profile.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for hosted configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.</td></tr>
<tr><td><CopyableCode code="validators" /></td><td><code>array</code></td><td>A list of methods for validating the configuration.</td></tr>
<tr><td><CopyableCode code="retrieval_role_arn" /></td><td><code>string</code></td><td>The ARN of an IAM role with permission to access the configuration at the specified LocationUri.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the configuration profile.</td></tr>
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
    <td><CopyableCode code="LocationUri, ApplicationId, Name, region" /></td>
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
List all <code>configuration_profiles</code> in a region.
```sql
SELECT
region,
application_id,
configuration_profile_id
FROM aws.appconfig.configuration_profiles
WHERE region = 'us-east-1';
```
Gets all properties from a <code>configuration_profile</code>.
```sql
SELECT
region,
configuration_profile_id,
location_uri,
type,
kms_key_identifier,
description,
kms_key_arn,
validators,
retrieval_role_arn,
application_id,
tags,
name
FROM aws.appconfig.configuration_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<ConfigurationProfileId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appconfig.configuration_profiles (
 LocationUri,
 ApplicationId,
 Name,
 region
)
SELECT 
'{{ LocationUri }}',
 '{{ ApplicationId }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appconfig.configuration_profiles (
 LocationUri,
 Type,
 KmsKeyIdentifier,
 Description,
 Validators,
 RetrievalRoleArn,
 ApplicationId,
 Tags,
 Name,
 region
)
SELECT 
 '{{ LocationUri }}',
 '{{ Type }}',
 '{{ KmsKeyIdentifier }}',
 '{{ Description }}',
 '{{ Validators }}',
 '{{ RetrievalRoleArn }}',
 '{{ ApplicationId }}',
 '{{ Tags }}',
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
  - name: configuration_profile
    props:
      - name: LocationUri
        value: '{{ LocationUri }}'
      - name: Type
        value: '{{ Type }}'
      - name: KmsKeyIdentifier
        value: '{{ KmsKeyIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: Validators
        value:
          - Type: '{{ Type }}'
            Content: '{{ Content }}'
      - name: RetrievalRoleArn
        value: '{{ RetrievalRoleArn }}'
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appconfig.configuration_profiles
WHERE data__Identifier = '<ApplicationId|ConfigurationProfileId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_profiles</code> resource, the following permissions are required:

### Read
```json
appconfig:GetConfigurationProfile,
appconfig:ListTagsForResource
```

### Create
```json
appconfig:CreateConfigurationProfile,
appconfig:GetConfigurationProfile,
appconfig:TagResource,
appconfig:ListTagsForResource,
iam:PassRole
```

### Update
```json
appconfig:UpdateConfigurationProfile,
appconfig:TagResource,
appconfig:UntagResource,
iam:PassRole
```

### List
```json
appconfig:ListConfigurationProfiles
```

### Delete
```json
appconfig:DeleteConfigurationProfile
```

