---
title: keyspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - keyspaces
  - cassandra
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

Creates, updates, deletes or gets a <code>keyspace</code> resource or lists <code>keyspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keyspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Keyspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.keyspaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="replication_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="client_side_timestamps_enabled" /></td><td><code>boolean</code></td><td>Indicates whether client-side timestamps are enabled (true) or disabled (false) for all tables in the keyspace. To add a Region to a single-Region keyspace with at least one table, the value must be set to true. After you enabled client-side timestamps for a table, you can’t disable it again.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html"><code>AWS::Cassandra::Keyspace</code></a>.

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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>keyspaces</code> in a region.
```sql
SELECT
region,
keyspace_name,
tags,
replication_specification,
client_side_timestamps_enabled
FROM aws.cassandra.keyspaces
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>keyspace</code>.
```sql
SELECT
region,
keyspace_name,
tags,
replication_specification,
client_side_timestamps_enabled
FROM aws.cassandra.keyspaces
WHERE region = 'us-east-1' AND data__Identifier = '<KeyspaceName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keyspace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cassandra.keyspaces (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cassandra.keyspaces (
 KeyspaceName,
 Tags,
 ReplicationSpecification,
 ClientSideTimestampsEnabled,
 region
)
SELECT 
 '{{ KeyspaceName }}',
 '{{ Tags }}',
 '{{ ReplicationSpecification }}',
 '{{ ClientSideTimestampsEnabled }}',
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
  - name: keyspace
    props:
      - name: KeyspaceName
        value: '{{ KeyspaceName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ReplicationSpecification
        value:
          ReplicationStrategy: '{{ ReplicationStrategy }}'
          RegionList:
            - '{{ RegionList[0] }}'
      - name: ClientSideTimestampsEnabled
        value: '{{ ClientSideTimestampsEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cassandra.keyspaces
WHERE data__Identifier = '<KeyspaceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>keyspaces</code> resource, the following permissions are required:

### Create
```json
cassandra:Create,
cassandra:CreateMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
cassandra:TagResource,
cassandra:TagMultiRegionResource,
iam:CreateServiceLinkedRole
```

### Read
```json
cassandra:Select,
cassandra:SelectMultiRegionResource
```

### Update
```json
cassandra:Alter,
cassandra:AlterMultiRegionResource,
cassandra:Modify,
cassandra:ModifyMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
cassandra:TagResource,
cassandra:TagMultiRegionResource,
cassandra:UntagResource,
cassandra:UntagMultiRegionResource,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:PutMetricAlarm,
iam:CreateServiceLinkedRole
```

### Delete
```json
cassandra:Drop,
cassandra:DropMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource
```

### List
```json
cassandra:Select,
cassandra:SelectMultiRegionResource
```
