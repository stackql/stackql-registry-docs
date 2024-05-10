---
title: scraper
hide_title: false
hide_table_of_contents: false
keywords:
  - scraper
  - aps
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


Gets or updates an individual <code>scraper</code> resource, use <code>scrapers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scraper</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Scraper</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.scraper" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="scraper_id" /></td><td><code>string</code></td><td>Required to identify a specific scraper.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>Scraper alias.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Scraper ARN.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>IAM role ARN for the scraper.</td></tr>
<tr><td><CopyableCode code="scrape_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="destination" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
scraper_id,
alias,
arn,
role_arn,
scrape_configuration,
source,
destination,
tags
FROM aws.aps.scraper
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>scraper</code> resource, the following permissions are required:

### Read
```json
aps:DescribeScraper,
aps:ListTagsForResource
```

### Update
```json
aps:DescribeScraper,
aps:TagResource,
aps:UntagResource,
aps:ListTagsForResource
```

