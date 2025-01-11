---
title: builds_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - builds_list_only
  - gamelift
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

Lists <code>builds</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/builds/"><code>builds</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GameLift::Build</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.builds_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="build_id" /></td><td><code>string</code></td><td>A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.</td></tr>
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
Lists all <code>builds</code> in a region.
```sql
SELECT
region,
build_id
FROM aws.gamelift.builds_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>builds_list_only</code> resource, see <a href="/providers/aws/gamelift/builds/#permissions"><code>builds</code></a>

