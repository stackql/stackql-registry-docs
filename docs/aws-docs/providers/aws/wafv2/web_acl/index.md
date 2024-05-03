---
title: web_acl
hide_title: false
hide_table_of_contents: false
keywords:
  - web_acl
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

Gets or operates on an individual <code>web_acl</code> resource, use <code>web_acls</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.web_acl" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="default_action" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><CopyableCode code="visibility_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="label_namespace" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_response_bodies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="captcha_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="challenge_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="token_domains" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="association_config" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
capacity,
default_action,
description,
name,
id,
scope,
rules,
visibility_config,
tags,
label_namespace,
custom_response_bodies,
captcha_config,
challenge_config,
token_domains,
association_config
FROM aws.wafv2.web_acl
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```

## Permissions

To operate on the <code>web_acl</code> resource, the following permissions are required:

### Delete
```json
wafv2:DeleteWebACL,
wafv2:GetWebACL
```

### Read
```json
wafv2:GetWebACL,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateWebACL,
wafv2:GetWebACL,
wafv2:ListTagsForResource
```

