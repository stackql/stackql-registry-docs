---
title: resource_specific_logging
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_specific_logging
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
Gets an individual <code>resource_specific_logging</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_specific_logging</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource-specific logging allows you to specify a logging level for a specific thing group.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.resource_specific_logging</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_type</code></td><td><code>string</code></td><td>The target type. Value must be THING_GROUP, CLIENT_ID, SOURCE_IP, PRINCIPAL_ID, or EVENT_TYPE.</td></tr>
<tr><td><code>target_name</code></td><td><code>string</code></td><td>The target name.</td></tr>
<tr><td><code>log_level</code></td><td><code>string</code></td><td>The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>
<tr><td><code>target_id</code></td><td><code>string</code></td><td>Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
target_type,
target_name,
log_level,
target_id
FROM aws.iot.resource_specific_logging
WHERE data__Identifier = '<TargetId>';
```

## Permissions

To operate on the <code>resource_specific_logging</code> resource, the following permissions are required:

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

