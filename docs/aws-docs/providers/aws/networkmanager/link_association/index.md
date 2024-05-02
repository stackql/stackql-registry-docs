---
title: link_association
hide_title: false
hide_table_of_contents: false
keywords:
  - link_association
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
Gets an individual <code>link_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>link_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::LinkAssociation type associates a link to a device. The device and link must be in the same global network and the same site.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.link_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>device_id</code></td><td><code>string</code></td><td>The ID of the device</td></tr>
<tr><td><code>link_id</code></td><td><code>string</code></td><td>The ID of the link</td></tr>
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
global_network_id,
device_id,
link_id
FROM aws.networkmanager.link_association
WHERE data__Identifier = '<GlobalNetworkId>|<DeviceId>|<LinkId>';
```

## Permissions

To operate on the <code>link_association</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetLinkAssociations
```

### Delete
```json
networkmanager:DisassociateLink
```

