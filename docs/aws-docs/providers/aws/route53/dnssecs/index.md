---
title: dnssecs
hide_title: false
hide_table_of_contents: false
keywords:
  - dnssecs
  - route53
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


Used to retrieve a list of <code>dnssecs</code> in a region or to create or delete a <code>dnssecs</code> resource, use <code>dnssec</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dnssecs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource used to control (enable&#x2F;disable) DNSSEC in a specific hosted zone.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.dnssecs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="hosted_zone_id" /></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
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
hosted_zone_id
FROM aws.route53.dnssecs
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>dnssec</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- dnssec.iql (required properties only)
INSERT INTO aws.route53.dnssecs (
 HostedZoneId,
 region
)
SELECT 
'{{ HostedZoneId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- dnssec.iql (all properties)
INSERT INTO aws.route53.dnssecs (
 HostedZoneId,
 region
)
SELECT 
 '{{ HostedZoneId }}',
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
  - name: dnssec
    props:
      - name: HostedZoneId
        value: '{{ HostedZoneId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53.dnssecs
WHERE data__Identifier = '<HostedZoneId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dnssecs</code> resource, the following permissions are required:

### Create
```json
route53:GetDNSSEC,
route53:EnableHostedZoneDNSSEC,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### Delete
```json
route53:GetDNSSEC,
route53:DisableHostedZoneDNSSEC,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### List
```json
route53:GetDNSSEC,
route53:ListHostedZones
```

