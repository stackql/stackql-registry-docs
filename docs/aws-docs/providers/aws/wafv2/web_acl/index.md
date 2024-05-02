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
Gets or operates on an individual <code>web_acl</code> resource, use <code>web_acls</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wafv2.web_acl</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>default_action</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rules</code></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><code>visibility_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>label_namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_response_bodies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>captcha_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>challenge_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>token_domains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>association_config</code></td><td><code>object</code></td><td></td></tr>
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

