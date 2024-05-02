---
title: logging
hide_title: false
hide_table_of_contents: false
keywords:
  - logging
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
Gets an individual <code>logging</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Logging Options enable you to configure your IoT V2 logging role and default logging level so that you can monitor progress events logs as it passes from your devices through Iot core service.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.logging</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the role that allows IoT to write to Cloudwatch logs.</td></tr>
<tr><td><code>default_log_level</code></td><td><code>string</code></td><td>The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>
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
account_id,
role_arn,
default_log_level
FROM aws.iot.logging
WHERE data__Identifier = '<AccountId>';
```

## Permissions

To operate on the <code>logging</code> resource, the following permissions are required:

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

