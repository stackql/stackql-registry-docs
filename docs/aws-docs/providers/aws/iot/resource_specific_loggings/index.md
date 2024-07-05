---
title: resource_specific_loggings
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_specific_loggings
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

Creates, updates, deletes or gets a <code>resource_specific_logging</code> resource or lists <code>resource_specific_loggings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_specific_loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource-specific logging allows you to specify a logging level for a specific thing group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.resource_specific_loggings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.</td></tr>
<tr><td><CopyableCode code="target_name" /></td><td><code>string</code></td><td>The target name.</td></tr>
<tr><td><CopyableCode code="log_level" /></td><td><code>string</code></td><td>The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td>Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.</td></tr>
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
    <td><CopyableCode code="TargetName, TargetType, LogLevel, region" /></td>
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
Gets all <code>resource_specific_loggings</code> in a region.
```sql
SELECT
region,
target_type,
target_name,
log_level,
target_id
FROM aws.iot.resource_specific_loggings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_specific_logging</code>.
```sql
SELECT
region,
target_type,
target_name,
log_level,
target_id
FROM aws.iot.resource_specific_loggings
WHERE region = 'us-east-1' AND data__Identifier = '<TargetId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_specific_logging</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.resource_specific_loggings (
 TargetType,
 TargetName,
 LogLevel,
 region
)
SELECT 
'{{ TargetType }}',
 '{{ TargetName }}',
 '{{ LogLevel }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.resource_specific_loggings (
 TargetType,
 TargetName,
 LogLevel,
 region
)
SELECT 
 '{{ TargetType }}',
 '{{ TargetName }}',
 '{{ LogLevel }}',
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
  - name: resource_specific_logging
    props:
      - name: TargetType
        value: '{{ TargetType }}'
      - name: TargetName
        value: '{{ TargetName }}'
      - name: LogLevel
        value: '{{ LogLevel }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.resource_specific_loggings
WHERE data__Identifier = '<TargetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_specific_loggings</code> resource, the following permissions are required:

### Create
```json
iot:ListV2LoggingLevels,
iot:SetV2LoggingLevel
```

### Read
```json
iot:ListV2LoggingLevels
```

### Update
```json
iot:ListV2LoggingLevels,
iot:SetV2LoggingLevel
```

### Delete
```json
iot:ListV2LoggingLevels,
iot:DeleteV2LoggingLevel
```

### List
```json
iot:ListV2LoggingLevels
```

