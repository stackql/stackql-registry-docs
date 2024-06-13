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

Creates, updates, deletes or gets a <code>flow_entitlement</code> resource or lists <code>flow_entitlements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowEntitlement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_entitlements" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The ARN of the flow.</td></tr>
<tr><td><CopyableCode code="entitlement_arn" /></td><td><code>string</code></td><td>The ARN of the entitlement.</td></tr>
<tr><td><CopyableCode code="data_transfer_subscriber_fee_percent" /></td><td><code>integer</code></td><td>Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the entitlement.</td></tr>
<tr><td><CopyableCode code="encryption" /></td><td><code>object</code></td><td>The type of encryption that will be used on the output that is associated with this entitlement.</td></tr>
<tr><td><CopyableCode code="entitlement_status" /></td><td><code>string</code></td><td>An indication of whether the entitlement is enabled.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the entitlement.</td></tr>
<tr><td><CopyableCode code="subscribers" /></td><td><code>array</code></td><td>The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</td></tr>
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
    <td><CopyableCode code="FlowArn, Name, Subscribers, Description, region" /></td>
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
List all <code>flow_entitlements</code> in a region.
```sql
SELECT
region,
entitlement_arn
FROM aws.mediaconnect.flow_entitlements
WHERE region = 'us-east-1';
```
Gets all properties from a <code>flow_entitlement</code>.
```sql
SELECT
region,
flow_arn,
entitlement_arn,
data_transfer_subscriber_fee_percent,
description,
encryption,
entitlement_status,
name,
subscribers
FROM aws.mediaconnect.flow_entitlements
WHERE region = 'us-east-1' AND data__Identifier = '<EntitlementArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_entitlement</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
mediaconnect:DescribeFlow
```

### Update
```json
mediaconnect:DescribeFlow,
mediaconnect:UpdateFlowEntitlement
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

