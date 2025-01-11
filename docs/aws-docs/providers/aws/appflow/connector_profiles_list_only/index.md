---
title: connector_profiles_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_profiles_list_only
  - appflow
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

Lists <code>connector_profiles</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/connector_profiles/"><code>connector_profiles</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profiles_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppFlow::ConnectorProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.connector_profiles_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connector_profile_name" /></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
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
Lists all <code>connector_profiles</code> in a region.
```sql
SELECT
region,
connector_profile_name
FROM aws.appflow.connector_profiles_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>connector_profiles_list_only</code> resource, see <a href="/providers/aws/appflow/connector_profiles/#permissions"><code>connector_profiles</code></a>

