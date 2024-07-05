---
title: simple_ads_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - simple_ads_list_only
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

Lists <code>simple_ads</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/simple_ads/"><code>simple_ads</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simple_ads_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::DirectoryService::SimpleAD</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.directoryservice.simple_ads_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>The unique identifier for a directory.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>simple_ads</code> in a region.
```sql
SELECT
region,
directory_id
FROM aws.directoryservice.simple_ads_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>simple_ads_list_only</code> resource, see <a href="/providers/aws/directoryservice/simple_ads/#permissions"><code>simple_ads</code></a>


