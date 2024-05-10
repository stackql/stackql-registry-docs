---
title: link
hide_title: false
hide_table_of_contents: false
keywords:
  - link
  - oam
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
<tr><td><b>Description</b></td><td>Definition of AWS::Oam::Link Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.oam.link" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="label" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="label_template" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_types" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sink_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="link_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Tags to apply to the link</td></tr>
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
arn,
label,
label_template,
resource_types,
sink_identifier,
link_configuration,
tags
FROM aws.oam.link
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>link</code> resource, the following permissions are required:

### Read
```json
oam:GetLink
```

### Update
```json
oam:GetLink,
oam:UpdateLink,
cloudwatch:Link,
logs:Link,
xray:Link,
applicationinsights:Link,
internetmonitor:Link,
oam:TagResource,
oam:UntagResource
```

