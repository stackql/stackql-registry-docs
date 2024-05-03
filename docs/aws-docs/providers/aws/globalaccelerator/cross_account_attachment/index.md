---
title: cross_account_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_account_attachment
  - globalaccelerator
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

Gets or operates on an individual <code>cross_account_attachment</code> resource, use <code>cross_account_attachments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cross_account_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::CrossAccountAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.cross_account_attachment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The Friendly identifier of the attachment.</td></tr>
<tr><td><CopyableCode code="attachment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the attachment.</td></tr>
<tr><td><CopyableCode code="principals" /></td><td><code>array</code></td><td>Principals to share the resources with.</td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td>Resources shared using the attachment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
name,
attachment_arn,
principals,
resources,
tags
FROM aws.globalaccelerator.cross_account_attachment
WHERE data__Identifier = '<AttachmentArn>';
```

## Permissions

To operate on the <code>cross_account_attachment</code> resource, the following permissions are required:

### Read
```json
globalaccelerator:DescribeCrossAccountAttachment
```

### Update
```json
globalaccelerator:UpdateCrossAccountAttachment,
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:TagResource,
globalaccelerator:UntagResource
```

### Delete
```json
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:DeleteCrossAccountAttachment
```
