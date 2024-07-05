---
title: ip_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_sets
  - wafv2
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

Creates, updates, deletes or gets an <code>ip_set</code> resource or lists <code>ip_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.ip_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the entity.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the WebACL.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the WebACL</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront WebACL, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
<tr><td><CopyableCode code="ip_address_version" /></td><td><code>string</code></td><td>Type of addresses in the IPSet, use IPV4 for IPV4 IP addresses, IPV6 for IPV6 address.</td></tr>
<tr><td><CopyableCode code="addresses" /></td><td><code>array</code></td><td>List of IPAddresses.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Addresses, IPAddressVersion, Scope, region" /></td>
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
Gets all <code>ip_sets</code> in a region.
```sql
SELECT
region,
arn,
description,
name,
id,
scope,
ip_address_version,
addresses,
tags
FROM aws.wafv2.ip_sets
;
```
Gets all properties from an individual <code>ip_set</code>.
```sql
SELECT
region,
arn,
description,
name,
id,
scope,
ip_address_version,
addresses,
tags
FROM aws.wafv2.ip_sets
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wafv2.ip_sets (
 Scope,
 IPAddressVersion,
 Addresses,
 region
)
SELECT 
'{{ Scope }}',
 '{{ IPAddressVersion }}',
 '{{ Addresses }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wafv2.ip_sets (
 Description,
 Name,
 Scope,
 IPAddressVersion,
 Addresses,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ Scope }}',
 '{{ IPAddressVersion }}',
 '{{ Addresses }}',
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
  - name: ip_set
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Scope
        value: '{{ Scope }}'
      - name: IPAddressVersion
        value: '{{ IPAddressVersion }}'
      - name: Addresses
        value:
          - '{{ Addresses[0] }}'
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
DELETE FROM aws.wafv2.ip_sets
WHERE data__Identifier = '<Name|Id|Scope>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ip_sets</code> resource, the following permissions are required:

### Create
```json
wafv2:CreateIPSet,
wafv2:GetIPSet,
wafv2:ListTagsForResource
```

### Delete
```json
wafv2:DeleteIPSet,
wafv2:GetIPSet
```

### Read
```json
wafv2:GetIPSet,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateIPSet,
wafv2:GetIPSet,
wafv2:ListTagsForResource
```

### List
```json
wafv2:listIPSets
```

