---
title: playback_restriction_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_restriction_policy
  - ivs
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


Gets or updates an individual <code>playback_restriction_policy</code> resource, use <code>playback_restriction_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_restriction_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::PlaybackRestrictionPolicy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.playback_restriction_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Playback-restriction-policy identifier.</td></tr>
<tr><td><CopyableCode code="allowed_countries" /></td><td><code>array</code></td><td>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).</td></tr>
<tr><td><CopyableCode code="allowed_origins" /></td><td><code>array</code></td><td>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at https:&#x2F;&#x2F;developer.mozilla.org&#x2F;en-US&#x2F;docs&#x2F;Web&#x2F;HTTP&#x2F;Headers&#x2F;Origin</td></tr>
<tr><td><CopyableCode code="enable_strict_origin_enforcement" /></td><td><code>boolean</code></td><td>Whether channel playback is constrained by origin site.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Playback-restriction-policy name.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
arn,
allowed_countries,
allowed_origins,
enable_strict_origin_enforcement,
name,
tags
FROM aws.ivs.playback_restriction_policy
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>playback_restriction_policy</code> resource, the following permissions are required:

### Read
```json
ivs:GetPlaybackRestrictionPolicy,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetPlaybackRestrictionPolicy,
ivs:UpdatePlaybackRestrictionPolicy,
ivs:ListTagsForResource,
ivs:UntagResource,
ivs:TagResource
```

