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
Gets an individual <code>scraper</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scraper</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Scraper</td></tr>
<tr><td><b>Id</b></td><td><code>aws.aps.scraper</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scraper_id</code></td><td><code>string</code></td><td>Required to identify a specific scraper.</td></tr>
<tr><td><code>alias</code></td><td><code>string</code></td><td>Scraper alias.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Scraper ARN.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>IAM role ARN for the scraper.</td></tr>
<tr><td><code>scrape_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>destination</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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
WHERE data__Identifier = '<Arn>';
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

### Delete
```json
aps:DeleteScraper,
aps:DescribeScraper,
aps:DescribeWorkspace,
eks:AssociateAccessPolicy,
eks:DescribeCluster,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
iam:DeleteServiceLinkedRole
```

