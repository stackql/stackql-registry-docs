---
title: studio_components_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_components_list_only
  - nimblestudio
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

Lists <code>studio_components</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/studio_components/"><code>studio_components</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_components_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio component that connects a non-Nimble Studio resource in your account to your studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studio_components_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td><p>The configuration of the studio component, based on component type.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>The description.</p></td></tr>
<tr><td><CopyableCode code="ec2_security_group_ids" /></td><td><code>array</code></td><td><p>The EC2 security groups that control access to the studio component.</p></td></tr>
<tr><td><CopyableCode code="initialization_scripts" /></td><td><code>array</code></td><td><p>Initialization scripts for studio components.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td><p>The name for the studio component.</p></td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="script_parameters" /></td><td><code>array</code></td><td><p>Parameters for the studio component scripts.</p></td></tr>
<tr><td><CopyableCode code="secure_initialization_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_component_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td><p>The studio ID. </p></td></tr>
<tr><td><CopyableCode code="subtype" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>studio_components</code> in a region.
```sql
SELECT
region,
studio_component_id,
studio_id
FROM aws.nimblestudio.studio_components_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>studio_components_list_only</code> resource, see <a href="/providers/aws/nimblestudio/studio_components/#permissions"><code>studio_components</code></a>


