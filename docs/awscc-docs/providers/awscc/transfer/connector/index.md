---
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connector</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.transfer.connector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_role</code></td><td><code>string</code></td><td>Specifies the access role for the connector.</td></tr>
<tr><td><code>as2_config</code></td><td><code>object</code></td><td>Configuration for an AS2 connector.</td></tr>
<tr><td><code>sftp_config</code></td><td><code>object</code></td><td>Configuration for an SFTP connector.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the connector.</td></tr>
<tr><td><code>connector_id</code></td><td><code>string</code></td><td>A unique identifier for the connector.</td></tr>
<tr><td><code>logging_role</code></td><td><code>string</code></td><td>Specifies the logging role for the connector.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td>URL for Connector</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_role,
as2_config,
sftp_config,
arn,
connector_id,
logging_role,
tags,
url
FROM awscc.transfer.connector
WHERE data__Identifier = '<ConnectorId>';
```

## Permissions

To operate on the <code>connector</code> resource, the following permissions are required:

### Read
```json
transfer:DescribeConnector
```

### Update
```json
transfer:UpdateConnector,
transfer:UnTagResource,
transfer:TagResource,
iam:PassRole
```

### Delete
```json
transfer:DeleteConnector
```

