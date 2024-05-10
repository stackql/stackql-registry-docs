---
title: trust_anchor
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_anchor
  - rolesanywhere
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


Gets or updates an individual <code>trust_anchor</code> resource, use <code>trust_anchors</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_anchor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.trust_anchor" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_settings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_anchor_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_anchor_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
enabled,
name,
notification_settings,
source,
tags,
trust_anchor_id,
trust_anchor_arn
FROM aws.rolesanywhere.trust_anchor
WHERE region = 'us-east-1' AND data__Identifier = '<TrustAnchorId>';
```


## Permissions

To operate on the <code>trust_anchor</code> resource, the following permissions are required:

### Read
```json
rolesanywhere:GetTrustAnchor,
rolesanywhere:ListTagsForResource
```

### Update
```json
acm-pca:GetCertificateAuthorityCertificate,
rolesanywhere:ListTagsForResource,
rolesanywhere:TagResource,
rolesanywhere:UntagResource,
rolesanywhere:EnableTrustAnchor,
rolesanywhere:DisableTrustAnchor,
rolesanywhere:UpdateTrustAnchor,
rolesanywhere:GetTrustAnchor,
rolesanywhere:PutNotificationSettings,
rolesanywhere:ResetNotificationSettings
```

