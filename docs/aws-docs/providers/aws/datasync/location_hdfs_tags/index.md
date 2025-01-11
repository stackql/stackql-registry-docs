---
title: location_hdfs_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - location_hdfs_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>location_hdfs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_hdfs_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationHDFS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_hdfs_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name_nodes" /></td><td><code>array</code></td><td>An array of Name Node(s) of the HDFS location.</td></tr>
<tr><td><CopyableCode code="block_size" /></td><td><code>integer</code></td><td>Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.</td></tr>
<tr><td><CopyableCode code="replication_factor" /></td><td><code>integer</code></td><td>Number of copies of each block that exists inside the HDFS cluster.</td></tr>
<tr><td><CopyableCode code="kms_key_provider_uri" /></td><td><code>string</code></td><td>The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.</td></tr>
<tr><td><CopyableCode code="qop_configuration" /></td><td><code>object</code></td><td>Configuration information for RPC Protection and Data Transfer Protection. These parameters can be set to AUTHENTICATION, INTEGRITY, or PRIVACY. The default value is PRIVACY.</td></tr>
<tr><td><CopyableCode code="authentication_type" /></td><td><code>string</code></td><td>The authentication mode used to determine identity of user.</td></tr>
<tr><td><CopyableCode code="simple_user" /></td><td><code>string</code></td><td>The user name that has read and write permissions on the specified HDFS cluster.</td></tr>
<tr><td><CopyableCode code="kerberos_principal" /></td><td><code>string</code></td><td>The unique identity, or principal, to which Kerberos can assign tickets.</td></tr>
<tr><td><CopyableCode code="kerberos_keytab" /></td><td><code>string</code></td><td>The Base64 string representation of the Keytab file.</td></tr>
<tr><td><CopyableCode code="kerberos_krb5_conf" /></td><td><code>string</code></td><td>The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.</td></tr>
<tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>ARN(s) of the agent(s) to use for an HDFS location.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the HDFS location.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the HDFS location that was described.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>location_hdfs</code> in a region.
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
agent_arns,
subdirectory,
location_arn,
location_uri,
tag_key,
tag_value
FROM aws.datasync.location_hdfs_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>location_hdfs_tags</code> resource, see <a href="/providers/aws/datasync/location_hdfs/#permissions"><code>location_hdfs</code></a>

