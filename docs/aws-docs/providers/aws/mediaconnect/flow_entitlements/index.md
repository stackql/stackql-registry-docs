---
title: flow_entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_entitlements
  - mediaconnect
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


Used to retrieve a list of <code>flow_entitlements</code> in a region or to create or delete a <code>flow_entitlements</code> resource, use <code>flow_entitlement</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowEntitlement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_entitlements" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="entitlement_arn" /></td><td><code>string</code></td><td>The ARN of the entitlement.</td></tr>
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
entitlement_arn
FROM aws.mediaconnect.flow_entitlements
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>flow_entitlement</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- flow_entitlement.iql (required properties only)
INSERT INTO aws.mediaconnect.flow_entitlements (
 FlowArn,
 Description,
 Name,
 Subscribers,
 region
)
SELECT 
'{{ FlowArn }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ Subscribers }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- flow_entitlement.iql (all properties)
INSERT INTO aws.mediaconnect.flow_entitlements (
 FlowArn,
 DataTransferSubscriberFeePercent,
 Description,
 Encryption,
 EntitlementStatus,
 Name,
 Subscribers,
 region
)
SELECT 
 '{{ FlowArn }}',
 '{{ DataTransferSubscriberFeePercent }}',
 '{{ Description }}',
 '{{ Encryption }}',
 '{{ EntitlementStatus }}',
 '{{ Name }}',
 '{{ Subscribers }}',
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
  - name: flow_entitlement
    props:
      - name: FlowArn
        value: '{{ FlowArn }}'
      - name: DataTransferSubscriberFeePercent
        value: '{{ DataTransferSubscriberFeePercent }}'
      - name: Description
        value: '{{ Description }}'
      - name: Encryption
        value:
          Algorithm: '{{ Algorithm }}'
          ConstantInitializationVector: '{{ ConstantInitializationVector }}'
          DeviceId: '{{ DeviceId }}'
          KeyType: '{{ KeyType }}'
          Region: '{{ Region }}'
          ResourceId: '{{ ResourceId }}'
          RoleArn: '{{ RoleArn }}'
          SecretArn: '{{ SecretArn }}'
          Url: '{{ Url }}'
      - name: EntitlementStatus
        value: '{{ EntitlementStatus }}'
      - name: Name
        value: '{{ Name }}'
      - name: Subscribers
        value:
          - '{{ Subscribers[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediaconnect.flow_entitlements
WHERE data__Identifier = '<EntitlementArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_entitlements</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
mediaconnect:GrantFlowEntitlements
```

### Delete
```json
mediaconnect:DescribeFlow,
mediaconnect:RevokeFlowEntitlement
```

### List
```json
mediaconnect:DescribeFlow
```

