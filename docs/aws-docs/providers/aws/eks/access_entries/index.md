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
Retrieves a list of <code>access_entries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS AccessEntry.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eks.access_entries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>principal_arn</code></td><td><code>string</code></td><td>The principal ARN that the access entry is created for.</td></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>The cluster that the access entry is created for.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
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

