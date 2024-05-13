---
title: distribution
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution
  - cloudfront
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


Gets or updates an individual <code>distribution</code> resource, use <code>distributions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.distribution" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="distribution_config" /></td><td><code>object</code></td><td>The distribution's configuration.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A complex type that contains zero or more <code>Tag</code> elements.</td></tr>
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
distribution_config,
domain_name,
id,
tags
FROM aws.cloudfront.distribution
WHERE data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>distribution</code> resource, the following permissions are required:

### Read
```json
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig
```

### Update
```json
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig,
cloudfront:UpdateDistribution,
cloudfront:UpdateDistributionWithStagingConfig,
cloudfront:ListTagsForResource,
cloudfront:TagResource,
cloudfront:UntagResource
```

