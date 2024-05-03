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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>connector</code> resource, use <code>connectors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.connector" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_role" /></td><td><code>string</code></td><td>Specifies the access role for the connector.</td></tr>
<tr><td><CopyableCode code="as2_config" /></td><td><code>object</code></td><td>Configuration for an AS2 connector.</td></tr>
<tr><td><CopyableCode code="sftp_config" /></td><td><code>object</code></td><td>Configuration for an SFTP connector.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the connector.</td></tr>
<tr><td><CopyableCode code="connector_id" /></td><td><code>string</code></td><td>A unique identifier for the connector.</td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td>Specifies the logging role for the connector.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>URL for Connector</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.transfer.connector
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

