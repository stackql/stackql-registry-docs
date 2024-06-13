---
title: scrapers
hide_title: false
hide_table_of_contents: false
keywords:
  - scrapers
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

Creates, updates, deletes or gets a <code>scraper</code> resource or lists <code>scrapers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scrapers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Scraper</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.scrapers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scraper_id" /></td><td><code>string</code></td><td>Required to identify a specific scraper.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>Scraper alias.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Scraper ARN.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>IAM role ARN for the scraper.</td></tr>
<tr><td><CopyableCode code="scrape_configuration" /></td><td><code>object</code></td><td>Scraper configuration</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td>Scraper metrics source</td></tr>
<tr><td><CopyableCode code="destination" /></td><td><code>object</code></td><td>Scraper metrics destination</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ScrapeConfiguration, Source, Destination, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>scrapers</code> in a region.
```sql
SELECT
region,
arn
FROM aws.aps.scrapers
WHERE region = 'us-east-1';
```
Gets all properties from a <code>scraper</code>.
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
FROM aws.aps.scrapers
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scraper</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.aps.scrapers (
 ScrapeConfiguration,
 Source,
 Destination,
 region
)
SELECT 
'{{ ScrapeConfiguration }}',
 '{{ Source }}',
 '{{ Destination }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.aps.scrapers (
 Alias,
 ScrapeConfiguration,
 Source,
 Destination,
 Tags,
 region
)
SELECT 
 '{{ Alias }}',
 '{{ ScrapeConfiguration }}',
 '{{ Source }}',
 '{{ Destination }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: scraper
    props:
      - name: Alias
        value: '{{ Alias }}'
      - name: ScrapeConfiguration
        value:
          ConfigurationBlob: '{{ ConfigurationBlob }}'
      - name: Source
        value:
          EksConfiguration:
            ClusterArn: '{{ ClusterArn }}'
            SecurityGroupIds:
              - '{{ SecurityGroupIds[0] }}'
            SubnetIds:
              - '{{ SubnetIds[0] }}'
      - name: Destination
        value:
          AmpConfiguration:
            WorkspaceArn: '{{ WorkspaceArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.aps.scrapers
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scrapers</code> resource, the following permissions are required:

### Create
```json
aps:CreateScraper,
aps:DescribeScraper,
aps:DescribeWorkspace,
aps:TagResource,
eks:CreateAccessEntry,
eks:AssociateAccessPolicy,
eks:DescribeCluster,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
iam:CreateServiceLinkedRole
```

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

### List
```json
aps:ListScrapers,
aps:ListTagsForResource
```

