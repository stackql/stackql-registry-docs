---
title: cross_account_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_account_attachments
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

Used to retrieve a list of <code>cross_account_attachments</code> in a region or create a <code>cross_account_attachments</code> resource, use <code>cross_account_attachment</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cross_account_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::CrossAccountAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.cross_account_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="attachment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the attachment.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
attachment_arn
FROM aws.globalaccelerator.cross_account_attachments

```

## Permissions

To operate on the <code>cross_account_attachments</code> resource, the following permissions are required:

### Create
```json
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:CreateCrossAccountAttachment,
globalaccelerator:TagResource
```

### List
```json
globalaccelerator:ListCrossAccountAttachments
```

