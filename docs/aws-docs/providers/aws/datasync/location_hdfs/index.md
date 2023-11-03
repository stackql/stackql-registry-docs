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
<tr><td><b>Id</b></td><td><code>aws.datasync.location_hdfs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>NameNodes</code></td><td><code>array</code></td><td>An array of Name Node(s) of the HDFS location.</td></tr><tr><td><code>BlockSize</code></td><td><code>integer</code></td><td>Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.</td></tr><tr><td><code>ReplicationFactor</code></td><td><code>integer</code></td><td>Number of copies of each block that exists inside the HDFS cluster.</td></tr><tr><td><code>KmsKeyProviderUri</code></td><td><code>string</code></td><td>The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.</td></tr><tr><td><code>QopConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AuthenticationType</code></td><td><code>string</code></td><td>The authentication mode used to determine identity of user.</td></tr><tr><td><code>SimpleUser</code></td><td><code>string</code></td><td>The user name that has read and write permissions on the specified HDFS cluster.</td></tr><tr><td><code>KerberosPrincipal</code></td><td><code>string</code></td><td>The unique identity, or principal, to which Kerberos can assign tickets.</td></tr><tr><td><code>KerberosKeytab</code></td><td><code>string</code></td><td>The Base64 string representation of the Keytab file.</td></tr><tr><td><code>KerberosKrb5Conf</code></td><td><code>string</code></td><td>The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>AgentArns</code></td><td><code>array</code></td><td>ARN(s) of the agent(s) to use for an HDFS location.</td></tr><tr><td><code>Subdirectory</code></td><td><code>string</code></td><td>The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.</td></tr><tr><td><code>LocationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the HDFS location.</td></tr><tr><td><code>LocationUri</code></td><td><code>string</code></td><td>The URL of the HDFS location that was described.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.datasync.location_hdfs
WHERE region = 'us-east-1' AND data__Identifier = '{LocationArn}'
```
