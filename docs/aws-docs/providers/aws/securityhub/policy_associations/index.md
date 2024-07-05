---
title: policy_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_associations
  - securityhub
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

Creates, updates, deletes or gets a <code>policy_association</code> resource or lists <code>policy_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::PolicyAssociation resource represents the AWS Security Hub Central Configuration Policy associations in your Target. Only the AWS Security Hub delegated administrator can create the resouce from the home region.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.policy_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration_policy_id" /></td><td><code>string</code></td><td>The universally unique identifier (UUID) of the configuration policy or a value of SELF_MANAGED_SECURITY_HUB for a self-managed configuration</td></tr>
<tr><td><CopyableCode code="association_status" /></td><td><code>string</code></td><td>The current status of the association between the specified target and the configuration</td></tr>
<tr><td><CopyableCode code="association_type" /></td><td><code>string</code></td><td>Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub delegated administrator or inherited from a parent</td></tr>
<tr><td><CopyableCode code="association_status_message" /></td><td><code>string</code></td><td>An explanation for a FAILED value for AssociationStatus</td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td>The identifier of the target account, organizational unit, or the root</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>Indicates whether the target is an AWS account, organizational unit, or the organization root</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated</td></tr>
<tr><td><CopyableCode code="association_identifier" /></td><td><code>string</code></td><td>A unique identifier to indicates if the target has an association</td></tr>
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
    <td><CopyableCode code="TargetId, TargetType, ConfigurationPolicyId, region" /></td>
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
Gets all <code>policy_associations</code> in a region.
```sql
SELECT
region,
configuration_policy_id,
association_status,
association_type,
association_status_message,
target_id,
target_type,
updated_at,
association_identifier
FROM aws.securityhub.policy_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>policy_association</code>.
```sql
SELECT
region,
configuration_policy_id,
association_status,
association_type,
association_status_message,
target_id,
target_type,
updated_at,
association_identifier
FROM aws.securityhub.policy_associations
WHERE region = 'us-east-1' AND data__Identifier = '<AssociationIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.policy_associations (
 ConfigurationPolicyId,
 TargetId,
 TargetType,
 region
)
SELECT 
'{{ ConfigurationPolicyId }}',
 '{{ TargetId }}',
 '{{ TargetType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.policy_associations (
 ConfigurationPolicyId,
 TargetId,
 TargetType,
 region
)
SELECT 
 '{{ ConfigurationPolicyId }}',
 '{{ TargetId }}',
 '{{ TargetType }}',
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
  - name: policy_association
    props:
      - name: ConfigurationPolicyId
        value: '{{ ConfigurationPolicyId }}'
      - name: TargetId
        value: '{{ TargetId }}'
      - name: TargetType
        value: '{{ TargetType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.policy_associations
WHERE data__Identifier = '<AssociationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policy_associations</code> resource, the following permissions are required:

### Create
```json
securityhub:StartConfigurationPolicyAssociation,
securityhub:GetConfigurationPolicyAssociation
```

### Read
```json
securityhub:GetConfigurationPolicyAssociation,
securityhub:GetConfigurationPolicyAssociation
```

### Update
```json
securityhub:StartConfigurationPolicyAssociation,
securityhub:GetConfigurationPolicyAssociation
```

### Delete
```json
securityhub:StartConfigurationPolicyDisassociation,
securityhub:GetConfigurationPolicyAssociation
```

### List
```json
securityhub:ListConfigurationPolicyAssociations
```

