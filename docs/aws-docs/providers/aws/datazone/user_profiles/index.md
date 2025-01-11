---
title: user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles
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

Creates, updates, deletes or gets an <code>user_profile</code> resource or lists <code>user_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A user profile represents Amazon DataZone users. Amazon DataZone supports both IAM roles and SSO identities to interact with the Amazon DataZone Management Console and the data portal for different purposes. Domain administrators use IAM roles to perform the initial administrative domain-related work in the Amazon DataZone Management Console, including creating new Amazon DataZone domains, configuring metadata form types, and implementing policies. Data workers use their SSO corporate identities via Identity Center to log into the Amazon DataZone Data Portal and access projects where they have memberships.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.user_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="details" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the user profile is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the user profile would be created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone user profile.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the user profile.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the user profile.</td></tr>
<tr><td><CopyableCode code="user_identifier" /></td><td><code>string</code></td><td>The ID of the user.</td></tr>
<tr><td><CopyableCode code="user_type" /></td><td><code>string</code></td><td>The type of the user.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html"><code>AWS::DataZone::UserProfile</code></a>.

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
    <td><CopyableCode code="DomainIdentifier, UserIdentifier, region" /></td>
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
details,
domain_id,
domain_identifier,
id,
status,
type,
user_identifier,
user_type
FROM aws.datazone.user_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_profile</code>.
```sql
SELECT
region,
details,
domain_id,
domain_identifier,
id,
status,
type,
user_identifier,
user_type
FROM aws.datazone.user_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<Id>';
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
INSERT INTO aws.datazone.user_profiles (
 DomainIdentifier,
 UserIdentifier,
 region
)
SELECT 
'{{ DomainIdentifier }}',
 '{{ UserIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.user_profiles (
 DomainIdentifier,
 Status,
 UserIdentifier,
 UserType,
 region
)
SELECT 
 '{{ DomainIdentifier }}',
 '{{ Status }}',
 '{{ UserIdentifier }}',
 '{{ UserType }}',
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
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: Status
        value: '{{ Status }}'
      - name: UserIdentifier
        value: '{{ UserIdentifier }}'
      - name: UserType
        value: '{{ UserType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.user_profiles
WHERE data__Identifier = '<DomainId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_profiles</code> resource, the following permissions are required:

### Create
```json
datazone:CreateUserProfile,
datazone:GetUserProfile,
datazone:UpdateUserProfile,
datazone:GetDomain,
sso:ListProfiles,
sso:GetProfile,
sso:AssociateProfile,
sso:DisassociateProfile,
iam:GetRole,
iam:GetUser
```

### Read
```json
datazone:GetUserProfile
```

### Update
```json
datazone:UpdateUserProfile,
datazone:GetUserProfile,
datazone:UpdateUserProfile,
sso:ListProfiles,
sso:GetProfile,
sso:AssociateProfile,
sso:DisassociateProfile,
iam:GetRole,
iam:GetUser
```

### Delete
```json
datazone:DeleteUserProfile,
datazone:GetUserProfile,
datazone:UpdateUserProfile,
sso:ListProfiles,
sso:GetProfile,
sso:AssociateProfile,
sso:DisassociateProfile,
iam:GetRole,
iam:GetUser
```

### List
```json
datazone:SearchUserProfiles
```
