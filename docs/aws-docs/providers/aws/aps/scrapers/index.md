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


Used to retrieve a list of <code>scrapers</code> in a region or to create or delete a <code>scrapers</code> resource, use <code>scraper</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scrapers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Scraper</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.scrapers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Scraper ARN.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
arn
FROM aws.aps.scrapers
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ScrapeConfiguration": {
  "ConfigurationBlob": "{{ ConfigurationBlob }}"
 },
 "Source": {
  "EksConfiguration": {
   "ClusterArn": "{{ ClusterArn }}",
   "SecurityGroupIds": [
    "{{ SecurityGroupIds[0] }}"
   ],
   "SubnetIds": [
    "{{ SubnetIds[0] }}"
   ]
  }
 },
 "Destination": {
  "AmpConfiguration": {
   "WorkspaceArn": "{{ WorkspaceArn }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.aps.scrapers (
 ScrapeConfiguration,
 Source,
 Destination,
 region
)
SELECT 
{{ .ScrapeConfiguration }},
 {{ .Source }},
 {{ .Destination }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Alias": "{{ Alias }}",
 "ScrapeConfiguration": {
  "ConfigurationBlob": "{{ ConfigurationBlob }}"
 },
 "Source": {
  "EksConfiguration": {
   "ClusterArn": "{{ ClusterArn }}",
   "SecurityGroupIds": [
    "{{ SecurityGroupIds[0] }}"
   ],
   "SubnetIds": [
    "{{ SubnetIds[0] }}"
   ]
  }
 },
 "Destination": {
  "AmpConfiguration": {
   "WorkspaceArn": "{{ WorkspaceArn }}"
  }
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.aps.scrapers (
 Alias,
 ScrapeConfiguration,
 Source,
 Destination,
 Tags,
 region
)
SELECT 
 {{ .Alias }},
 {{ .ScrapeConfiguration }},
 {{ .Source }},
 {{ .Destination }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

