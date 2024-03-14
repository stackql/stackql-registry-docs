---
title: location_hdfs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_hdfs
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
Gets an individual <code>location_hdfs</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_hdfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_hdfs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_hdfs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name_nodes</code></td><td><code>array</code></td><td>An array of Name Node(s) of the HDFS location.</td></tr>
<tr><td><code>block_size</code></td><td><code>integer</code></td><td>Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.</td></tr>
<tr><td><code>replication_factor</code></td><td><code>integer</code></td><td>Number of copies of each block that exists inside the HDFS cluster.</td></tr>
<tr><td><code>kms_key_provider_uri</code></td><td><code>string</code></td><td>The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.</td></tr>
<tr><td><code>qop_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>authentication_type</code></td><td><code>string</code></td><td>The authentication mode used to determine identity of user.</td></tr>
<tr><td><code>simple_user</code></td><td><code>string</code></td><td>The user name that has read and write permissions on the specified HDFS cluster.</td></tr>
<tr><td><code>kerberos_principal</code></td><td><code>string</code></td><td>The unique identity, or principal, to which Kerberos can assign tickets.</td></tr>
<tr><td><code>kerberos_keytab</code></td><td><code>string</code></td><td>The Base64 string representation of the Keytab file.</td></tr>
<tr><td><code>kerberos_krb5_conf</code></td><td><code>string</code></td><td>The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>agent_arns</code></td><td><code>array</code></td><td>ARN(s) of the agent(s) to use for an HDFS location.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the HDFS location.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the HDFS location that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name_nodes,
block_size,
replication_factor,
kms_key_provider_uri,
qop_configuration,
authentication_type,
simple_user,
kerberos_principal,
kerberos_keytab,
kerberos_krb5_conf,
tags,
agent_arns,
subdirectory,
location_arn,
location_uri
FROM awscc.datasync.location_hdfs
WHERE data__Identifier = '<LocationArn>';
```

## Permissions

To operate on the <code>location_hdfs</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationHdfs,
datasync:ListTagsForResource
```

### Update
```json
datasync:UpdateLocationHdfs,
datasync:DescribeLocationHdfs,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```

