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


Used to retrieve a list of <code>resource_specific_loggings</code> in a region or to create or delete a <code>resource_specific_loggings</code> resource, use <code>resource_specific_logging</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_specific_loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource-specific logging allows you to specify a logging level for a specific thing group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.resource_specific_loggings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
target_id
FROM aws.iot.resource_specific_loggings
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "TargetType": "{{ TargetType }}",
 "TargetName": "{{ TargetName }}",
 "LogLevel": "{{ LogLevel }}"
}
>>>
--required properties only
INSERT INTO aws.iot.resource_specific_loggings (
 TargetType,
 TargetName,
 LogLevel,
 region
)
SELECT 
{{ TargetType }},
 {{ TargetName }},
 {{ LogLevel }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "TargetType": "{{ TargetType }}",
 "TargetName": "{{ TargetName }}",
 "LogLevel": "{{ LogLevel }}"
}
>>>
--all properties
INSERT INTO aws.iot.resource_specific_loggings (
 TargetType,
 TargetName,
 LogLevel,
 region
)
SELECT 
 {{ TargetType }},
 {{ TargetName }},
 {{ LogLevel }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
iot:ListV2LoggingLevels,
iot:DeleteV2LoggingLevel
```

### List
```json
iot:ListV2LoggingLevels
```

