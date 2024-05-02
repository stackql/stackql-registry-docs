---
title: site_to_site_vpn_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - site_to_site_vpn_attachments
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
Used to retrieve a list of <code>site_to_site_vpn_attachments</code> in a region or create a <code>site_to_site_vpn_attachments</code> resource, use <code>site_to_site_vpn_attachment</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>site_to_site_vpn_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::SiteToSiteVpnAttachment Resource Type definition.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.site_to_site_vpn_attachments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>attachment_id</code></td><td><code>string</code></td><td>The ID of the attachment.</td></tr>
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
attachment_id
FROM aws.networkmanager.site_to_site_vpn_attachments
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>site_to_site_vpn_attachments</code> resource, the following permissions are required:

### Create
```json
networkmanager:GetSiteToSiteVpnAttachment,
networkmanager:CreateSiteToSiteVpnAttachment,
ec2:DescribeRegions,
networkmanager:TagResource
```

### List
```json
networkmanager:ListAttachments
```

