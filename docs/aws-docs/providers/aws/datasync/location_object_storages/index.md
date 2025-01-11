---
title: location_object_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - location_object_storages
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

Creates, updates, deletes or gets a <code>location_object_storage</code> resource or lists <code>location_object_storages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_object_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationObjectStorage.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_object_storages" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_key" /></td><td><code>string</code></td><td>Optional. The access key is used if credentials are required to access the self-managed object storage server.</td></tr>
<tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.</td></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>The name of the bucket on the self-managed object storage server.</td></tr>
<tr><td><CopyableCode code="secret_key" /></td><td><code>string</code></td><td>Optional. The secret key is used if credentials are required to access the self-managed object storage server.</td></tr>
<tr><td><CopyableCode code="server_certificate" /></td><td><code>string</code></td><td>X.509 PEM content containing a certificate authority or chain to trust.</td></tr>
<tr><td><CopyableCode code="server_hostname" /></td><td><code>string</code></td><td>The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.</td></tr>
<tr><td><CopyableCode code="server_port" /></td><td><code>integer</code></td><td>The port that your self-managed server accepts inbound network traffic on.</td></tr>
<tr><td><CopyableCode code="server_protocol" /></td><td><code>string</code></td><td>The protocol that the object storage server uses to communicate.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>The subdirectory in the self-managed object storage server that is used to read data from.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the object storage location that was described.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html"><code>AWS::DataSync::LocationObjectStorage</code></a>.

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
    <td><CopyableCode code="AgentArns, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>location_object_storages</code> in a region.
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
FROM aws.datasync.location_object_storages
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>location_object_storage</code>.
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
FROM aws.datasync.location_object_storages
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>location_object_storage</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datasync.location_object_storages (
 AgentArns,
 region
)
SELECT 
'{{ AgentArns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.location_object_storages (
 AccessKey,
 AgentArns,
 BucketName,
 SecretKey,
 ServerCertificate,
 ServerHostname,
 ServerPort,
 ServerProtocol,
 Subdirectory,
 Tags,
 region
)
SELECT 
 '{{ AccessKey }}',
 '{{ AgentArns }}',
 '{{ BucketName }}',
 '{{ SecretKey }}',
 '{{ ServerCertificate }}',
 '{{ ServerHostname }}',
 '{{ ServerPort }}',
 '{{ ServerProtocol }}',
 '{{ Subdirectory }}',
 '{{ Tags }}',
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
  - name: location_object_storage
    props:
      - name: AccessKey
        value: '{{ AccessKey }}'
      - name: AgentArns
        value:
          - '{{ AgentArns[0] }}'
      - name: BucketName
        value: '{{ BucketName }}'
      - name: SecretKey
        value: '{{ SecretKey }}'
      - name: ServerCertificate
        value: '{{ ServerCertificate }}'
      - name: ServerHostname
        value: '{{ ServerHostname }}'
      - name: ServerPort
        value: '{{ ServerPort }}'
      - name: ServerProtocol
        value: '{{ ServerProtocol }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datasync.location_object_storages
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_object_storages</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationObjectStorage,
datasync:DescribeLocationObjectStorage,
datasync:ListTagsForResource,
datasync:TagResource
```

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

### List
```json
datasync:ListLocations
```
