---
title: location_object_storage
hide_title: false
hide_table_of_contents: false
keywords:
  - location_object_storage
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
Gets an individual <code>location_object_storage</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_object_storage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_object_storage</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_object_storage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_key</code></td><td><code>string</code></td><td>Optional. The access key is used if credentials are required to access the self-managed object storage server.</td></tr>
<tr><td><code>agent_arns</code></td><td><code>array</code></td><td>The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.</td></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td>The name of the bucket on the self-managed object storage server.</td></tr>
<tr><td><code>secret_key</code></td><td><code>string</code></td><td>Optional. The secret key is used if credentials are required to access the self-managed object storage server.</td></tr>
<tr><td><code>server_certificate</code></td><td><code>string</code></td><td>X.509 PEM content containing a certificate authority or chain to trust.</td></tr>
<tr><td><code>server_hostname</code></td><td><code>string</code></td><td>The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.</td></tr>
<tr><td><code>server_port</code></td><td><code>integer</code></td><td>The port that your self-managed server accepts inbound network traffic on.</td></tr>
<tr><td><code>server_protocol</code></td><td><code>string</code></td><td>The protocol that the object storage server uses to communicate.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>The subdirectory in the self-managed object storage server that is used to read data from.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the object storage location that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_key,
agent_arns,
bucket_name,
secret_key,
server_certificate,
server_hostname,
server_port,
server_protocol,
subdirectory,
tags,
location_arn,
location_uri
FROM awscc.datasync.location_object_storage
WHERE region = 'us-east-1'
AND data__Identifier = '{LocationArn}';
```

## Permissions

To operate on the <code>location_object_storage</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationObjectStorage,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationObjectStorage,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
datasync:UpdateLocationObjectStorage
```

### Delete
```json
datasync:DeleteLocation
```

