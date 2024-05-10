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


Used to retrieve a list of <code>subscription_targets</code> in a region or to create or delete a <code>subscription_targets</code> resource, use <code>subscription_target</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Subscription targets enables one to access the data to which you have subscribed in your projects.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.subscription_targets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
domain_id,
environment_id,
id
FROM aws.datazone.subscription_targets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>subscription_target</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- subscription_target.iql (required properties only)
INSERT INTO aws.datazone.subscription_targets (
 ApplicableAssetTypes,
 AuthorizedPrincipals,
 DomainIdentifier,
 EnvironmentIdentifier,
 ManageAccessRole,
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
 '{{ ManageAccessRole }}',
 '{{ Name }}',
 '{{ SubscriptionTargetConfig }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- subscription_target.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
datazone:DeleteSubscriptionTarget
```

### List
```json
datazone:ListSubscriptionTargets
```

