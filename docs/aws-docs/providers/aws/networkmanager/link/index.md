---
title: link
hide_title: false
hide_table_of_contents: false
keywords:
  - link
  - networkmanager
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


Gets or updates an individual <code>link</code> resource, use <code>links</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Link type describes a link.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.link" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="link_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the link.</td></tr>
<tr><td><CopyableCode code="link_id" /></td><td><code>string</code></td><td>The ID of the link.</td></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The ID of the site</td></tr>
<tr><td><CopyableCode code="bandwidth" /></td><td><code>object</code></td><td>The Bandwidth for the link.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the link.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the link.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the link.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the link.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the link.</td></tr>
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
link_arn,
link_id,
global_network_id,
site_id,
bandwidth,
provider,
description,
tags,
type,
created_at,
state
FROM aws.networkmanager.link
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<LinkId>';
```


## Permissions

To operate on the <code>link</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetLinks
```

### Update
```json
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:GetLinks,
networkmanager:UntagResource,
networkmanager:UpdateLink
```

