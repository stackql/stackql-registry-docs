---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - customerprofiles
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>domain</code> resource, use <code>domains</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain defined for 3rd party data source in Profile Service</td></tr>
<tr><td><b>Id</b></td><td><code>aws.customerprofiles.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>dead_letter_queue_url</code></td><td><code>string</code></td><td>The URL of the SQS dead letter queue</td></tr>
<tr><td><code>default_encryption_key</code></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><code>default_expiration_days</code></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><code>matching</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>rule_based_matching</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stats</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the domain</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
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
domain_name,
dead_letter_queue_url,
default_encryption_key,
default_expiration_days,
matching,
rule_based_matching,
stats,
tags,
created_at,
last_updated_at
FROM aws.customerprofiles.domain
WHERE data__Identifier = '<DomainName>';
```

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
```json
profile:GetDomain
```

### Update
```json
profile:GetDomain,
profile:UpdateDomain,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteDomain
```

