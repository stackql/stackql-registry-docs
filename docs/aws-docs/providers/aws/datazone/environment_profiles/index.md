---
title: environment_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_profiles
  - datazone
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

Creates, updates, deletes or gets an <code>environment_profile</code> resource or lists <code>environment_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Datazone Environment Profile is pre-configured set of resources and blueprints that provide reusable templates for creating environments.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>The AWS account in which the Amazon DataZone environment is created.</td></tr>
<tr><td><CopyableCode code="aws_account_region" /></td><td><code>string</code></td><td>The AWS region in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when this environment profile was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created this environment profile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="environment_blueprint_id" /></td><td><code>string</code></td><td>The ID of the blueprint with which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="environment_blueprint_identifier" /></td><td><code>string</code></td><td>The ID of the blueprint with which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The identifier of the project in which to create the environment profile.</td></tr>
<tr><td><CopyableCode code="project_identifier" /></td><td><code>string</code></td><td>The identifier of the project in which to create the environment profile.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when this environment profile was updated.</td></tr>
<tr><td><CopyableCode code="user_parameters" /></td><td><code>array</code></td><td>The user parameters of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html"><code>AWS::DataZone::EnvironmentProfile</code></a>.

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
    <td><CopyableCode code="EnvironmentBlueprintIdentifier, ProjectIdentifier, DomainIdentifier, AwsAccountId, AwsAccountRegion, Name, region" /></td>
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
Gets all <code>environment_profiles</code> in a region.
```sql
SELECT
region,
aws_account_id,
aws_account_region,
created_at,
created_by,
description,
domain_id,
domain_identifier,
environment_blueprint_id,
environment_blueprint_identifier,
id,
name,
project_id,
project_identifier,
updated_at,
user_parameters
FROM aws.datazone.environment_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment_profile</code>.
```sql
SELECT
region,
aws_account_id,
aws_account_region,
created_at,
created_by,
description,
domain_id,
domain_identifier,
environment_blueprint_id,
environment_blueprint_identifier,
id,
name,
project_id,
project_identifier,
updated_at,
user_parameters
FROM aws.datazone.environment_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datazone.environment_profiles (
 AwsAccountId,
 AwsAccountRegion,
 DomainIdentifier,
 EnvironmentBlueprintIdentifier,
 Name,
 ProjectIdentifier,
 region
)
SELECT 
'{{ AwsAccountId }}',
 '{{ AwsAccountRegion }}',
 '{{ DomainIdentifier }}',
 '{{ EnvironmentBlueprintIdentifier }}',
 '{{ Name }}',
 '{{ ProjectIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.environment_profiles (
 AwsAccountId,
 AwsAccountRegion,
 Description,
 DomainIdentifier,
 EnvironmentBlueprintIdentifier,
 Name,
 ProjectIdentifier,
 UserParameters,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ AwsAccountRegion }}',
 '{{ Description }}',
 '{{ DomainIdentifier }}',
 '{{ EnvironmentBlueprintIdentifier }}',
 '{{ Name }}',
 '{{ ProjectIdentifier }}',
 '{{ UserParameters }}',
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
  - name: environment_profile
    props:
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: AwsAccountRegion
        value: '{{ AwsAccountRegion }}'
      - name: Description
        value: '{{ Description }}'
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: EnvironmentBlueprintIdentifier
        value: '{{ EnvironmentBlueprintIdentifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: ProjectIdentifier
        value: '{{ ProjectIdentifier }}'
      - name: UserParameters
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.environment_profiles
WHERE data__Identifier = '<DomainId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environment_profiles</code> resource, the following permissions are required:

### Create
```json
datazone:CreateEnvironmentProfile,
datazone:GetEnvironmentProfile
```

### Read
```json
datazone:GetEnvironmentProfile
```

### Update
```json
datazone:UpdateEnvironmentProfile,
datazone:GetEnvironmentProfile
```

### Delete
```json
datazone:DeleteEnvironmentProfile,
datazone:GetEnvironmentProfile
```

### List
```json
datazone:ListEnvironmentProfiles
```
