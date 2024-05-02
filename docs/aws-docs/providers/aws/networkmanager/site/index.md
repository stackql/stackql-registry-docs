---
title: site
hide_title: false
hide_table_of_contents: false
keywords:
  - site
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>site</code> resource, use <code>sites</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>site</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Site type describes a site.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.site</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>site_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the site.</td></tr>
<tr><td><code>site_id</code></td><td><code>string</code></td><td>The ID of the site.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the site.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the site.</td></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>location</code></td><td><code>object</code></td><td>The location of the site.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the site.</td></tr>
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
site_arn,
site_id,
description,
tags,
global_network_id,
location,
created_at,
state
FROM aws.networkmanager.site
WHERE data__Identifier = '<GlobalNetworkId>|<SiteId>';
```

## Permissions

To operate on the <code>site</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetSites
```

### Update
```json
networkmanager:GetSites,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
networkmanager:UpdateSite
```

### Delete
```json
networkmanager:GetSites,
networkmanager:DeleteSite
```

