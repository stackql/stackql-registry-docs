---
title: location_object_storage_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - location_object_storage_tags
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

Expands all tag keys and values for <code>location_object_storages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_object_storage_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationObjectStorage.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_object_storage_tags" /></td></tr>
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
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the object storage location that was described.</td></tr>
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
Expands tags for all <code>location_object_storages</code> in a region.
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
location_arn,
location_uri,
tag_key,
tag_value
FROM aws.datasync.location_object_storage_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>location_object_storage_tags</code> resource, see <a href="/providers/aws/datasync/location_object_storages/#permissions"><code>location_object_storages</code></a>


