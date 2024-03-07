---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
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
Retrieves a list of <code>sites</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sites</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.sites</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>site_id</code></td><td><code>string</code></td><td>The ID of the site.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
global_network_id,
site_id
FROM awscc.networkmanager.sites
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>sites</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateSite,
networkmanager:GetSites,
networkmanager:TagResource
```

### List
```json
networkmanager:GetSites
```

