---
title: access_log_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_log_subscriptions
  - vpclattice
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


Used to retrieve a list of <code>access_log_subscriptions</code> in a region or to create or delete a <code>access_log_subscriptions</code> resource, use <code>access_log_subscription</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_log_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.access_log_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.vpclattice.access_log_subscriptions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>access_log_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- access_log_subscription.iql (required properties only)
INSERT INTO aws.vpclattice.access_log_subscriptions (
 DestinationArn,
 region
)
SELECT 
'{{ DestinationArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- access_log_subscription.iql (all properties)
INSERT INTO aws.vpclattice.access_log_subscriptions (
 DestinationArn,
 ResourceIdentifier,
 Tags,
 region
)
SELECT 
 '{{ DestinationArn }}',
 '{{ ResourceIdentifier }}',
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
  - name: access_log_subscription
    props:
      - name: DestinationArn
        value: '{{ DestinationArn }}'
      - name: ResourceIdentifier
        value: '{{ ResourceIdentifier }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.vpclattice.access_log_subscriptions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_log_subscriptions</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateAccessLogSubscription,
vpc-lattice:TagResource,
vpc-lattice:GetAccessLogSubscription,
vpc-lattice:ListTagsForResource,
logs:CreateLogDelivery,
logs:CreateLogStream,
logs:PutDestination,
logs:PutDestinationPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
logs:GetLogDelivery,
s3:PutBucketLogging,
s3:GetBucketLogging,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
firehose:TagDeliveryStream,
firehose:CreateDeliveryStream,
firehose:DescribeDeliveryStream,
iam:CreateServiceLinkedRole
```

### Delete
```json
vpc-lattice:DeleteAccessLogSubscription,
vpc-lattice:UntagResource,
logs:DeleteLogDelivery,
logs:DeleteLogStream,
logs:GetLogDelivery,
logs:DeleteDestination,
s3:PutBucketLogging,
iam:GetServiceLinkedRoleDeletionStatus,
iam:DeleteServiceLinkedRole,
firehose:DeleteDeliveryStream,
firehose:UntagDeliveryStream
```

### List
```json
vpc-lattice:ListAccessLogSubscriptions
```

