---
title: loggings
hide_title: false
hide_table_of_contents: false
keywords:
  - loggings
  - iot
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

Creates, updates, deletes or gets a <code>logging</code> resource or lists <code>loggings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.loggings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that allows IoT to write to Cloudwatch logs.</td></tr>
<tr><td><CopyableCode code="default_log_level" /></td><td><code>string</code></td><td>The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>
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
    <td><CopyableCode code="AccountId, RoleArn, DefaultLogLevel, region" /></td>
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
Gets all <code>loggings</code> in a region.
```sql
SELECT
region,
account_id,
role_arn,
default_log_level
FROM aws.iot.loggings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>logging</code>.
```sql
SELECT
region,
account_id,
role_arn,
default_log_level
FROM aws.iot.loggings
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logging</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.loggings (
 AccountId,
 RoleArn,
 DefaultLogLevel,
 region
)
SELECT 
'{{ AccountId }}',
 '{{ RoleArn }}',
 '{{ DefaultLogLevel }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.loggings (
 AccountId,
 RoleArn,
 DefaultLogLevel,
 region
)
SELECT 
 '{{ AccountId }}',
 '{{ RoleArn }}',
 '{{ DefaultLogLevel }}',
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
  - name: logging
    props:
      - name: AccountId
        value: '{{ AccountId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: DefaultLogLevel
        value: '{{ DefaultLogLevel }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.loggings
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>loggings</code> resource, the following permissions are required:

### Create
```json
iot:SetV2LoggingOptions,
iot:GetV2LoggingOptions,
iam:PassRole
```

### Read
```json
iot:GetV2LoggingOptions
```

### Update
```json
iot:SetV2LoggingOptions,
iot:GetV2LoggingOptions,
iam:PassRole
```

### Delete
```json
iot:SetV2LoggingOptions,
iot:GetV2LoggingOptions
```

### List
```json
iot:GetV2LoggingOptions
```

