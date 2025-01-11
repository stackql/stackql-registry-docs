---
title: anycast_ip_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - anycast_ip_lists
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

Creates, updates, deletes or gets an <code>anycast_ip_list</code> resource or lists <code>anycast_ip_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anycast_ip_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::CloudFront::AnycastIpList Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.anycast_ip_lists" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="anycast_ip_list" /></td><td><code>object</code></td><td>Definition of AWS::CloudFront::AnycastIpList Resource Type</td></tr>
<tr><td><CopyableCode code="e_tag" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-anycastiplist.html"><code>AWS::CloudFront::AnycastIpList</code></a>.

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
    <td><CopyableCode code="IpCount, Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>anycast_ip_lists</code> in a region.
```sql
SELECT
region,
anycast_ip_list,
e_tag,
id,
ip_count,
name,
tags
FROM aws.cloudfront.anycast_ip_lists
;
```
Gets all properties from an individual <code>anycast_ip_list</code>.
```sql
SELECT
region,
anycast_ip_list,
e_tag,
id,
ip_count,
name,
tags
FROM aws.cloudfront.anycast_ip_lists
WHERE data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>anycast_ip_list</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.anycast_ip_lists (
 IpCount,
 Name,
 region
)
SELECT 
'{{ IpCount }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.anycast_ip_lists (
 IpCount,
 Name,
 Tags,
 region
)
SELECT 
 '{{ IpCount }}',
 '{{ Name }}',
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
  - name: anycast_ip_list
    props:
      - name: IpCount
        value: '{{ IpCount }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          Items:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.anycast_ip_lists
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>anycast_ip_lists</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateAnycastIpList,
cloudfront:TagResource
```

### Delete
```json
cloudfront:DeleteAnycastIpList,
cloudfront:GetAnycastIpList
```

### List
```json
cloudfront:ListAnycastIpLists
```

### Read
```json
cloudfront:GetAnycastIpList,
cloudfront:ListTagsForResource
```
