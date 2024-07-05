---
title: addons_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - addons_list_only
  - eks
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

Lists <code>addons</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/addons/"><code>addons</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addons_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::Addon</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.addons_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of Cluster</td></tr>
<tr><td><CopyableCode code="addon_name" /></td><td><code>string</code></td><td>Name of Addon</td></tr>
<tr><td><CopyableCode code="addon_version" /></td><td><code>string</code></td><td>Version of Addon</td></tr>
<tr><td><CopyableCode code="preserve_on_delete" /></td><td><code>boolean</code></td><td>PreserveOnDelete parameter value</td></tr>
<tr><td><CopyableCode code="resolve_conflicts" /></td><td><code>string</code></td><td>Resolve parameter value conflicts</td></tr>
<tr><td><CopyableCode code="service_account_role_arn" /></td><td><code>string</code></td><td>IAM role to bind to the add-on's service account</td></tr>
<tr><td><CopyableCode code="pod_identity_associations" /></td><td><code>array</code></td><td>An array of pod identities to apply to this add-on.</td></tr>
<tr><td><CopyableCode code="configuration_values" /></td><td><code>string</code></td><td>The configuration values to use with the add-on</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the add-on</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>addons</code> in a region.
```sql
SELECT
region,
cluster_name,
addon_name
FROM aws.eks.addons_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>addons_list_only</code> resource, see <a href="/providers/aws/eks/addons/#permissions"><code>addons</code></a>


