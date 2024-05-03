---
title: access_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - access_entries
  - eks
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

Used to retrieve a list of <code>access_entries</code> in a region or create a <code>access_entries</code> resource, use <code>access_entry</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS AccessEntry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.access_entries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN that the access entry is created for.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The cluster that the access entry is created for.</td></tr>
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
principal_arn,
cluster_name
FROM aws.eks.access_entries
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>access_entries</code> resource, the following permissions are required:

### Create
```json
eks:CreateAccessEntry,
eks:DescribeAccessEntry,
eks:AssociateAccessPolicy,
eks:TagResource,
eks:ListAssociatedAccessPolicies
```

### List
```json
eks:ListAccessEntries
```

