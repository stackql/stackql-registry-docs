---
title: connection
hide_title: false
hide_table_of_contents: false
keywords:
  - connection
  - codeconnections
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeConnections::Connection resource which can be used to connect external source providers with other AWS services (i.e. AWS CodePipeline)</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codeconnections.connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connection_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the  connection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr>
<tr><td><code>connection_name</code></td><td><code>string</code></td><td>The name of the connection. Connection names must be unique in an AWS user account.</td></tr>
<tr><td><code>connection_status</code></td><td><code>string</code></td><td>The current status of the connection.</td></tr>
<tr><td><code>owner_account_id</code></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.</td></tr>
<tr><td><code>provider_type</code></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured. You must specify either a ProviderType or a HostArn.</td></tr>
<tr><td><code>host_arn</code></td><td><code>string</code></td><td>The host arn configured to represent the infrastructure where your third-party provider is installed. You must specify either a ProviderType or a HostArn.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Specifies the tags applied to a connection.</td></tr>
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
connection_arn,
connection_name,
connection_status,
owner_account_id,
provider_type,
host_arn,
tags
FROM aws.codeconnections.connection
WHERE data__Identifier = '<ConnectionArn>';
```

## Permissions

To operate on the <code>connection</code> resource, the following permissions are required:

### Read
```json
codeconnections:GetConnection,
codeconnections:ListTagsForResource
```

### Update
```json
codeconnections:ListTagsForResource,
codeconnections:TagResource,
codeconnections:UntagResource
```

### Delete
```json
codeconnections:DeleteConnection
```

