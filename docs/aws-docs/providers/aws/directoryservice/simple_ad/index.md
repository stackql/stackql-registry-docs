---
title: simple_ad
hide_title: false
hide_table_of_contents: false
keywords:
  - simple_ad
  - directoryservice
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


Gets or updates an individual <code>simple_ad</code> resource, use <code>simple_ads</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simple_ad</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::DirectoryService::SimpleAD</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.directoryservice.simple_ad" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>The unique identifier for a directory.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The alias for a directory.</td></tr>
<tr><td><CopyableCode code="dns_ip_addresses" /></td><td><code>array</code></td><td>The IP addresses of the DNS servers for the directory, such as &#91; "172.31.3.154", "172.31.63.203" &#93;.</td></tr>
<tr><td><CopyableCode code="create_alias" /></td><td><code>boolean</code></td><td>The name of the configuration set.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description for the directory.</td></tr>
<tr><td><CopyableCode code="enable_sso" /></td><td><code>boolean</code></td><td>Whether to enable single sign-on for a Simple Active Directory in AWS.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The fully qualified domain name for the AWS Managed Simple AD directory.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password for the default administrative user named Admin.</td></tr>
<tr><td><CopyableCode code="short_name" /></td><td><code>string</code></td><td>The NetBIOS name for your domain.</td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>string</code></td><td>The size of the directory.</td></tr>
<tr><td><CopyableCode code="vpc_settings" /></td><td><code>object</code></td><td>VPC settings of the Simple AD directory server in AWS.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
directory_id,
alias,
dns_ip_addresses,
create_alias,
description,
enable_sso,
name,
password,
short_name,
size,
vpc_settings
FROM aws.directoryservice.simple_ad
WHERE region = 'us-east-1' AND data__Identifier = '<DirectoryId>';
```


## Permissions

To operate on the <code>simple_ad</code> resource, the following permissions are required:

### Read
```json
ds:DescribeDirectories
```

### Update
```json
ds:EnableSso,
ds:DisableSso,
ds:DescribeDirectories
```

