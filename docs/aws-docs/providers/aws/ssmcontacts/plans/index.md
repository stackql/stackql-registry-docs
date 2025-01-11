---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
  - ssmcontacts
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

Creates, updates, deletes or gets a <code>plan</code> resource or lists <code>plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Engagement Plan for a SSM Incident Manager Contact.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="contact_id" /></td><td><code>string</code></td><td>Contact ID for the AWS SSM Incident Manager Contact to associate the plan.</td></tr>
<tr><td><CopyableCode code="stages" /></td><td><code>array</code></td><td>The stages that an escalation plan or engagement plan engages contacts and contact methods in.</td></tr>
<tr><td><CopyableCode code="rotation_ids" /></td><td><code>array</code></td><td>Rotation Ids to associate with Oncall Contact for engagement.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the contact.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html"><code>AWS::SSMContacts::Plan</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>plan</code>.
```sql
SELECT
region,
contact_id,
stages,
rotation_ids,
arn
FROM aws.ssmcontacts.plans
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>plan</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssmcontacts.plans (
 ContactId,
 Stages,
 RotationIds,
 region
)
SELECT 
'{{ ContactId }}',
 '{{ Stages }}',
 '{{ RotationIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssmcontacts.plans (
 ContactId,
 Stages,
 RotationIds,
 region
)
SELECT 
 '{{ ContactId }}',
 '{{ Stages }}',
 '{{ RotationIds }}',
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
  - name: plan
    props:
      - name: ContactId
        value: '{{ ContactId }}'
      - name: Stages
        value:
          - DurationInMinutes: '{{ DurationInMinutes }}'
            Targets:
              - ContactTargetInfo:
                  ContactId: '{{ ContactId }}'
                  IsEssential: '{{ IsEssential }}'
                ChannelTargetInfo:
                  ChannelId: '{{ ChannelId }}'
                  RetryIntervalInMinutes: '{{ RetryIntervalInMinutes }}'
      - name: RotationIds
        value:
          - '{{ RotationIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssmcontacts.plans
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>plans</code> resource, the following permissions are required:

### Create
```json
ssm-contacts:UpdateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### Read
```json
ssm-contacts:GetContact
```

### Update
```json
ssm-contacts:UpdateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### Delete
```json
ssm-contacts:UpdateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```
