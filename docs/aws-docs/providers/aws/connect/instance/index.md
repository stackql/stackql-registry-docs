---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
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
Gets an individual <code>instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>An instanceId is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>An instanceArn is automatically generated on creation based on instanceId.</td></tr>
<tr><td><code>identity_management_type</code></td><td><code>string</code></td><td>Specifies the type of directory integration for new instance.</td></tr>
<tr><td><code>instance_alias</code></td><td><code>string</code></td><td>Alias of the new directory created as part of new instance creation.</td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>Timestamp of instance creation logged as part of instance creation.</td></tr>
<tr><td><code>service_role</code></td><td><code>string</code></td><td>Service linked role created as part of instance creation.</td></tr>
<tr><td><code>instance_status</code></td><td><code>string</code></td><td>Specifies the creation status of new instance.</td></tr>
<tr><td><code>directory_id</code></td><td><code>string</code></td><td>Existing directoryId user wants to map to the new Connect instance.</td></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td>The attributes for the instance.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
identity_management_type,
instance_alias,
created_time,
service_role,
instance_status,
directory_id,
attributes
FROM aws.connect.instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
