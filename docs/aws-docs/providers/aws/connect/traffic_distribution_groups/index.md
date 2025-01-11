---
title: traffic_distribution_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_distribution_groups
  - connect
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

Creates, updates, deletes or gets a <code>traffic_distribution_group</code> resource or lists <code>traffic_distribution_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_distribution_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TrafficDistributionGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.traffic_distribution_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance that has been replicated.</td></tr>
<tr><td><CopyableCode code="traffic_distribution_group_arn" /></td><td><code>string</code></td><td>The identifier of the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>If this is the default traffic distribution group.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html"><code>AWS::Connect::TrafficDistributionGroup</code></a>.

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
    <td><CopyableCode code="InstanceArn, Name, region" /></td>
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
Gets all <code>traffic_distribution_groups</code> in a region.
```sql
SELECT
region,
instance_arn,
traffic_distribution_group_arn,
description,
name,
status,
tags,
is_default
FROM aws.connect.traffic_distribution_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>traffic_distribution_group</code>.
```sql
SELECT
region,
instance_arn,
traffic_distribution_group_arn,
description,
name,
status,
tags,
is_default
FROM aws.connect.traffic_distribution_groups
WHERE region = 'us-east-1' AND data__Identifier = '<TrafficDistributionGroupArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>traffic_distribution_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.traffic_distribution_groups (
 InstanceArn,
 Name,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.traffic_distribution_groups (
 InstanceArn,
 Description,
 Name,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Description }}',
 '{{ Name }}',
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
  - name: traffic_distribution_group
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.traffic_distribution_groups
WHERE data__Identifier = '<TrafficDistributionGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>traffic_distribution_groups</code> resource, the following permissions are required:

### Create
```json
connect:CreateTrafficDistributionGroup,
connect:DescribeTrafficDistributionGroup,
connect:TagResource
```

### Read
```json
connect:DescribeTrafficDistributionGroup
```

### Update
```json
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeleteTrafficDistributionGroup,
connect:DescribeTrafficDistributionGroup,
connect:UntagResource
```

### List
```json
connect:ListTrafficDistributionGroups
```
