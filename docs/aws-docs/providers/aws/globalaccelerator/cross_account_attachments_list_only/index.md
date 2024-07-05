---
title: cross_account_attachments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_account_attachments_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>cross_account_attachments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cross_account_attachments/"><code>cross_account_attachments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cross_account_attachments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::CrossAccountAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.cross_account_attachments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The Friendly identifier of the attachment.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>cross_account_attachments</code> in a region.
```sql
SELECT
region,
attachment_arn
FROM aws.globalaccelerator.cross_account_attachments_list_only
;
```


## Permissions

For permissions required to operate on the <code>cross_account_attachments_list_only</code> resource, see <a href="/providers/aws/globalaccelerator/cross_account_attachments/#permissions"><code>cross_account_attachments</code></a>


