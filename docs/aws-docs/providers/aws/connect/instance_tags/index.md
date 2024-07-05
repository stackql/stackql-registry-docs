---
title: instance_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_tags
  - connect
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

Expands all tag keys and values for <code>instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.instance_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>An instanceId is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An instanceArn is automatically generated on creation based on instanceId.</td></tr>
<tr><td><CopyableCode code="identity_management_type" /></td><td><code>string</code></td><td>Specifies the type of directory integration for new instance.</td></tr>
<tr><td><CopyableCode code="instance_alias" /></td><td><code>string</code></td><td>Alias of the new directory created as part of new instance creation.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>Timestamp of instance creation logged as part of instance creation.</td></tr>
<tr><td><CopyableCode code="service_role" /></td><td><code>string</code></td><td>Service linked role created as part of instance creation.</td></tr>
<tr><td><CopyableCode code="instance_status" /></td><td><code>string</code></td><td>Specifies the creation status of new instance.</td></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>Existing directoryId user wants to map to the new Connect instance.</td></tr>
<tr><td><CopyableCode code="attributes" /></td><td><code>object</code></td><td>The attributes for the instance.</td></tr>
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
Expands tags for all <code>instances</code> in a region.
```sql
SELECT
region,
id,
arn,
identity_management_type,
instance_alias,
created_time,
service_role,
instance_status,
directory_id,
attributes,
tag_key,
tag_value
FROM aws.connect.instance_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>instance_tags</code> resource, see <a href="/providers/aws/connect/instances/#permissions"><code>instances</code></a>


