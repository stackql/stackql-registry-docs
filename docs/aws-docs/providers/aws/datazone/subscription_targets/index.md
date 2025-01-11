---
title: subscription_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_targets
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

Creates, updates, deletes or gets a <code>subscription_target</code> resource or lists <code>subscription_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Subscription targets enables one to access the data to which you have subscribed in your projects.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.subscription_targets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="applicable_asset_types" /></td><td><code>array</code></td><td>The asset types that can be included in the subscription target.</td></tr>
<tr><td><CopyableCode code="authorized_principals" /></td><td><code>array</code></td><td>The authorized principals of the subscription target.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the subscription target was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created the subscription target.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target would be created.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target would be created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
<tr><td><CopyableCode code="manage_access_role" /></td><td><code>string</code></td><td>The manage access role that is used to create the subscription target.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the subscription target.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The identifier of the project specified in the subscription target.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the subscription target.</td></tr>
<tr><td><CopyableCode code="subscription_target_config" /></td><td><code>array</code></td><td>The configuration of the subscription target.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the subscription target.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when the subscription target was updated.</td></tr>
<tr><td><CopyableCode code="updated_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who updated the subscription target.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html"><code>AWS::DataZone::SubscriptionTarget</code></a>.

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
    <td><CopyableCode code="ApplicableAssetTypes, AuthorizedPrincipals, DomainIdentifier, EnvironmentIdentifier, Name, SubscriptionTargetConfig, Type, region" /></td>
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
Gets all <code>subscription_targets</code> in a region.
```sql
SELECT
region,
applicable_asset_types,
authorized_principals,
created_at,
created_by,
domain_id,
domain_identifier,
environment_id,
environment_identifier,
id,
manage_access_role,
name,
project_id,
provider,
subscription_target_config,
type,
updated_at,
updated_by
FROM aws.datazone.subscription_targets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>subscription_target</code>.
```sql
SELECT
region,
applicable_asset_types,
authorized_principals,
created_at,
created_by,
domain_id,
domain_identifier,
environment_id,
environment_identifier,
id,
manage_access_role,
name,
project_id,
provider,
subscription_target_config,
type,
updated_at,
updated_by
FROM aws.datazone.subscription_targets
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<EnvironmentId>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscription_target</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datazone.subscription_targets (
 ApplicableAssetTypes,
 AuthorizedPrincipals,
 DomainIdentifier,
 EnvironmentIdentifier,
 Name,
 SubscriptionTargetConfig,
 Type,
 region
)
SELECT 
'{{ ApplicableAssetTypes }}',
 '{{ AuthorizedPrincipals }}',
 '{{ DomainIdentifier }}',
 '{{ EnvironmentIdentifier }}',
 '{{ Name }}',
 '{{ SubscriptionTargetConfig }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.subscription_targets (
 ApplicableAssetTypes,
 AuthorizedPrincipals,
 DomainIdentifier,
 EnvironmentIdentifier,
 ManageAccessRole,
 Name,
 Provider,
 SubscriptionTargetConfig,
 Type,
 region
)
SELECT 
 '{{ ApplicableAssetTypes }}',
 '{{ AuthorizedPrincipals }}',
 '{{ DomainIdentifier }}',
 '{{ EnvironmentIdentifier }}',
 '{{ ManageAccessRole }}',
 '{{ Name }}',
 '{{ Provider }}',
 '{{ SubscriptionTargetConfig }}',
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
  - name: subscription_target
    props:
      - name: ApplicableAssetTypes
        value:
          - '{{ ApplicableAssetTypes[0] }}'
      - name: AuthorizedPrincipals
        value:
          - '{{ AuthorizedPrincipals[0] }}'
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: EnvironmentIdentifier
        value: '{{ EnvironmentIdentifier }}'
      - name: ManageAccessRole
        value: '{{ ManageAccessRole }}'
      - name: Name
        value: '{{ Name }}'
      - name: Provider
        value: '{{ Provider }}'
      - name: SubscriptionTargetConfig
        value:
          - FormName: '{{ FormName }}'
            Content: '{{ Content }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.subscription_targets
WHERE data__Identifier = '<DomainId|EnvironmentId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subscription_targets</code> resource, the following permissions are required:

### Create
```json
datazone:CreateSubscriptionTarget,
datazone:GetSubscriptionTarget,
iam:PassRole
```

### Read
```json
datazone:GetSubscriptionTarget
```

### Update
```json
datazone:UpdateSubscriptionTarget,
datazone:GetSubscriptionTarget,
iam:PassRole
```

### Delete
```json
datazone:DeleteSubscriptionTarget
```

### List
```json
datazone:ListSubscriptionTargets
```
