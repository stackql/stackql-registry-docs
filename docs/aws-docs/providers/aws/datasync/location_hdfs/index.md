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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>location_hdf</code> resource or lists <code>location_hdfs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_hdfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationHDFS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_hdfs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name_nodes" /></td><td><code>array</code></td><td>An array of Name Node(s) of the HDFS location.</td></tr>
<tr><td><CopyableCode code="block_size" /></td><td><code>integer</code></td><td>Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.</td></tr>
<tr><td><CopyableCode code="replication_factor" /></td><td><code>integer</code></td><td>Number of copies of each block that exists inside the HDFS cluster.</td></tr>
<tr><td><CopyableCode code="kms_key_provider_uri" /></td><td><code>string</code></td><td>The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.</td></tr>
<tr><td><CopyableCode code="qop_configuration" /></td><td><code>Configuration information for RPC Protection and Data Transfer Protection. These parameters can be set to AUTHENTICATION, INTEGRITY, or PRIVACY. The default value is PRIVACY.</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication_type" /></td><td><code>string</code></td><td>The authentication mode used to determine identity of user.</td></tr>
<tr><td><CopyableCode code="simple_user" /></td><td><code>string</code></td><td>The user name that has read and write permissions on the specified HDFS cluster.</td></tr>
<tr><td><CopyableCode code="kerberos_principal" /></td><td><code>string</code></td><td>The unique identity, or principal, to which Kerberos can assign tickets.</td></tr>
<tr><td><CopyableCode code="kerberos_keytab" /></td><td><code>string</code></td><td>The Base64 string representation of the Keytab file.</td></tr>
<tr><td><CopyableCode code="kerberos_krb5_conf" /></td><td><code>string</code></td><td>The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>ARN(s) of the agent(s) to use for an HDFS location.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the HDFS location.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the HDFS location that was described.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="NameNodes, AuthenticationType, AgentArns, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>location_hdfs</code> in a region.
```sql
SELECT
region,
location_arn
FROM aws.datasync.location_hdfs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>location_hdf</code>.
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
FROM aws.datasync.location_hdfs
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>location_hdf</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.datasync.location_hdfs (
 NameNodes,
 AuthenticationType,
 AgentArns,
 region
)
SELECT 
'{{ NameNodes }}',
 '{{ AuthenticationType }}',
 '{{ AgentArns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.location_hdfs (
 NameNodes,
 BlockSize,
 ReplicationFactor,
 KmsKeyProviderUri,
 QopConfiguration,
 AuthenticationType,
 SimpleUser,
 KerberosPrincipal,
 KerberosKeytab,
 KerberosKrb5Conf,
 Tags,
 AgentArns,
 Subdirectory,
 region
)
SELECT 
 '{{ NameNodes }}',
 '{{ BlockSize }}',
 '{{ ReplicationFactor }}',
 '{{ KmsKeyProviderUri }}',
 '{{ QopConfiguration }}',
 '{{ AuthenticationType }}',
 '{{ SimpleUser }}',
 '{{ KerberosPrincipal }}',
 '{{ KerberosKeytab }}',
 '{{ KerberosKrb5Conf }}',
 '{{ Tags }}',
 '{{ AgentArns }}',
 '{{ Subdirectory }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: location_hdf
    props:
      - name: NameNodes
        value:
          - Hostname: '{{ Hostname }}'
            Port: '{{ Port }}'
      - name: BlockSize
        value: '{{ BlockSize }}'
      - name: ReplicationFactor
        value: '{{ ReplicationFactor }}'
      - name: KmsKeyProviderUri
        value: '{{ KmsKeyProviderUri }}'
      - name: QopConfiguration
        value:
          RpcProtection: '{{ RpcProtection }}'
          DataTransferProtection: '{{ DataTransferProtection }}'
      - name: AuthenticationType
        value: '{{ AuthenticationType }}'
      - name: SimpleUser
        value: '{{ SimpleUser }}'
      - name: KerberosPrincipal
        value: '{{ KerberosPrincipal }}'
      - name: KerberosKeytab
        value: '{{ KerberosKeytab }}'
      - name: KerberosKrb5Conf
        value: '{{ KerberosKrb5Conf }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AgentArns
        value:
          - '{{ AgentArns[0] }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datasync.location_hdfs
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_hdfs</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationHdfs,
datasync:DescribeLocationHdfs,
datasync:TagResource,
datasync:ListTagsForResource
```

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

### List
```json
datasync:ListLocations
```

