---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - mediapackage
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

Used to retrieve a list of <code>channels</code> in a region or create a <code>channels</code> resource, use <code>channel</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Channel.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.mediapackage.channels
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
```json
mediapackage:CreateChannel,
mediapackage:DescribeChannel,
mediapackage:UpdateChannel,
mediapackage:TagResource,
mediapackage:ConfigureLogs,
iam:CreateServiceLinkedRole
```

### List
```json
mediapackage:ListChannels
```

