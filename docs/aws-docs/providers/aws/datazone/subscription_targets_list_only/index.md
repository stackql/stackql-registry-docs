---
title: subscription_targets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_targets_list_only
  - datazone
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

Lists <code>subscription_targets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/subscription_targets/"><code>subscription_targets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_targets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Subscription targets enables one to access the data to which you have subscribed in your projects.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.subscription_targets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="applicable_asset_types" /></td><td><code>array</code></td><td>The asset types that can be included in the subscription target.</td></tr>
<tr><td><CopyableCode code="authorized_principals" /></td><td><code>array</code></td><td>The authorized principals of the subscription target.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the subscription target was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created the subscription target.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target would be created.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target would be created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
<tr><td><CopyableCode code="manage_access_role" /></td><td><code>string</code></td><td>The manage access role that is used to create the subscription target.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the subscription target.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The identifier of the project specified in the subscription target.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the subscription target.</td></tr>
<tr><td><CopyableCode code="subscription_target_config" /></td><td><code>array</code></td><td>The configuration of the subscription target.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the subscription target.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when the subscription target was updated.</td></tr>
<tr><td><CopyableCode code="updated_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who updated the subscription target.</td></tr>
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
Lists all <code>subscription_targets</code> in a region.
```sql
SELECT
region,
domain_id,
environment_id,
id
FROM aws.datazone.subscription_targets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>subscription_targets_list_only</code> resource, see <a href="/providers/aws/datazone/subscription_targets/#permissions"><code>subscription_targets</code></a>


