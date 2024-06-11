---
title: storage_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_systems
  - datasync
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

Creates, updates, deletes or gets a <code>storage_system</code> resource or lists <code>storage_systems</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::StorageSystem.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.storage_systems" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="server_configuration" /></td><td><code>The server name and network port required to connect with the management interface of the on-premises storage system.</code></td><td></td></tr>
<tr><td><CopyableCode code="server_credentials" /></td><td><code>The username and password for accessing your on-premises storage system's management interface.</code></td><td></td></tr>
<tr><td><CopyableCode code="secrets_manager_arn" /></td><td><code>string</code></td><td>The ARN of a secret stored by AWS Secrets Manager.</td></tr>
<tr><td><CopyableCode code="system_type" /></td><td><code>string</code></td><td>The type of on-premises storage system that DataSync Discovery will analyze.</td></tr>
<tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>The ARN of the DataSync agent that connects to and reads from the on-premises storage system's management interface.</td></tr>
<tr><td><CopyableCode code="cloud_watch_log_group_arn" /></td><td><code>string</code></td><td>The ARN of the Amazon CloudWatch log group used to monitor and log discovery job events.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A familiar name for the on-premises storage system.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="storage_system_arn" /></td><td><code>string</code></td><td>The ARN of the on-premises storage system added to DataSync Discovery.</td></tr>
<tr><td><CopyableCode code="connectivity_status" /></td><td><code>string</code></td><td>Indicates whether the DataSync agent can access the on-premises storage system.</td></tr>
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
    <td><CopyableCode code="ServerConfiguration, SystemType, AgentArns, region" /></td>
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
List all <code>storage_systems</code> in a region.
```sql
SELECT
region,
storage_system_arn
FROM aws.datasync.storage_systems
WHERE region = 'us-east-1';
```
Gets all properties from a <code>storage_system</code>.
```sql
SELECT
region,
server_configuration,
server_credentials,
secrets_manager_arn,
system_type,
agent_arns,
cloud_watch_log_group_arn,
name,
tags,
storage_system_arn,
connectivity_status
FROM aws.datasync.storage_systems
WHERE region = 'us-east-1' AND data__Identifier = '<StorageSystemArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_system</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datasync.storage_systems (
 ServerConfiguration,
 SystemType,
 AgentArns,
 region
)
SELECT 
'{{ ServerConfiguration }}',
 '{{ SystemType }}',
 '{{ AgentArns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.storage_systems (
 ServerConfiguration,
 ServerCredentials,
 SystemType,
 AgentArns,
 CloudWatchLogGroupArn,
 Name,
 Tags,
 region
)
SELECT 
 '{{ ServerConfiguration }}',
 '{{ ServerCredentials }}',
 '{{ SystemType }}',
 '{{ AgentArns }}',
 '{{ CloudWatchLogGroupArn }}',
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
  - name: storage_system
    props:
      - name: ServerConfiguration
        value:
          ServerHostname: '{{ ServerHostname }}'
          ServerPort: '{{ ServerPort }}'
      - name: ServerCredentials
        value:
          Username: '{{ Username }}'
          Password: '{{ Password }}'
      - name: SystemType
        value: '{{ SystemType }}'
      - name: AgentArns
        value:
          - '{{ AgentArns[0] }}'
      - name: CloudWatchLogGroupArn
        value: '{{ CloudWatchLogGroupArn }}'
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
DELETE FROM aws.datasync.storage_systems
WHERE data__Identifier = '<StorageSystemArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>storage_systems</code> resource, the following permissions are required:

### Create
```json
datasync:AddStorageSystem,
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
datasync:TagResource,
secretsmanager:CreateSecret,
secretsmanager:DescribeSecret,
iam:CreateServiceLinkedRole
```

### Read
```json
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
secretsmanager:DescribeSecret
```

### Update
```json
datasync:UpdateStorageSystem,
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
secretsmanager:DescribeSecret,
secretsmanager:PutSecretValue
```

### Delete
```json
datasync:DescribeStorageSystem,
datasync:RemoveStorageSystem,
secretsmanager:DescribeSecret,
secretsmanager:DeleteSecret
```

### List
```json
datasync:ListStorageSystems
```

