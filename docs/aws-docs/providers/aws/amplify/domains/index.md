---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplify.domains</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.amplify.domains
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
amplify:CreateDomainAssociation,
route53:ListHostedZones,
route53:ChangeResourceRecordSets,
iam:PassRole,
amplify:TagResource
```

### List
```json
amplify:ListDomainAssociations,
iam:PassRole,
amplify:ListTagsForResource
```

